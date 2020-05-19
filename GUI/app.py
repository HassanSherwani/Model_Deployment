from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flaskext.markdown import Markdown
from flask_dropzone import Dropzone
from flask_basicauth import BasicAuth

from script_api import extracts
from script_json import extract_json

import os, json, ast
import glob
import docx2txt
import requests
from json2html import *

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'legal'
app.config['BASIC_AUTH_PASSWORD'] = 'tech'
app.config['BASIC_AUTH_FORCE'] = True

Markdown(app)
basic_auth = BasicAuth(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_CUSTOM=True,
    DROPZONE_ALLOWED_FILE_TYPE=".pdf, .docx, .txt",
    DROPZONE_MAX_FILE_SIZE=30,
    DROPZONE_MAX_FILES=30,
)

dropzone = Dropzone(app)

PATH_UPLOAD = os.path.join(os.getcwd()+"/uploads/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/extract_metadata")
def extract_metadata():
    return render_template("extract.html")

@app.route('/extract', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':

        raw_text = request.form['rawtext']
        result = extracts(raw_text)
        result_json = extract_json(raw_text)

        formated_json = json.dumps(json.loads(result_json), indent=4)
        json_dict = ast.literal_eval(result_json)

        dict_list = list()

        for key in json_dict.keys():
            json_ = {"CONFIDENCE":json_dict[key]["CONFIDENCE"], "ENT_DETECT":json_dict[key]["ENT_DETECT"], "ENT_LABEL":json_dict[key]["ENT_LABEL"]}
            dict_list.append(json_)

        extraction = (result, dict_list, formated_json)


        return render_template('result.html', rawtext=raw_text, result=extraction)

    else:
        return render_template('result.html', rawtext="raw_text", result="result")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('upload.html')

@app.route('/documents')
def documents():
    files = [file for file in glob.glob(PATH_UPLOAD+"*.*")]
    return render_template("documents.html", files=files)

@app.route("/saved_extracts")
def saved_extracts():
    return render_template("saved_extracts.html", files=[1, 2, 3, 4])

@app.route("/browser")
def browser():
    ready_files = list()

    for file in glob.glob(PATH_UPLOAD+"*.*"):
        file_name = file.split("/")[-1]
        file_type = file.split(".")[-1]
        if os.path.getsize(file) < 1000000:
            file_size = '{:,.0f}'.format(
                os.path.getsize(file)/float(1 << 10))+" KB"
        else:
            file_size = '{:,.0f}'.format(
                os.path.getsize(file)/float(1 << 20))+" MB"

        if file_type == "txt":
            file_icon = "<i class=\"fa fa-file\"></i>"
        elif file_type == "xlsx" or file_type == "xls":
            file_icon = "<i class=\"fa fa-bar-chart-o\"></i>"
        else:
            file_icon = "<i class=\"fa fa-file\"></i>"

        file_content = read_files(file)

        ready_file = {"file_name": file_name, "file_type": file_type,
                      "file_size": file_size, "file_icon": file_icon, "file_content": file_content}
        ready_files.append(ready_file)

    return render_template("browser.html", files=ready_files)

@app.route("/file/<string:filename>")
def file(filename):

    output = read_files(filename)

    output_object = {"file_name": filename, "text": output,
                     "type": str(filename).split(".")[-1]}
    return render_template("file.html", file=output_object)


def read_files(filename):

    if "/" in filename:
        if str(filename).endswith("txt"):
            with open(filename, "r") as reader:
                output = reader.read()

        elif str(filename).endswith("docx"):
            output = docx2txt.process(filename)

        else:
            output = "Diese Datei kann nicht im Browser angezeigt werden."
    else:
        if str(filename).endswith("txt"):
            with open("uploads/"+filename, "r") as reader:
                output = reader.read()

        elif str(filename).endswith("docx"):
            output = docx2txt.process("uploads/"+filename)

        else:
            output = "Diese Datei kann nicht im Browser angezeigt werden."

    return output

@app.route("/saveresult", methods=['GET', 'POST'])
def saveresult():

    return redirect("saved_extracts")



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
