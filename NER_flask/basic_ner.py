from flask import Flask,url_for,render_template,request
### Load for spacy
from spacy.pipeline import EntityRuler
import spacy
from spacy import displacy


nlp = spacy.load('en_core_web_sm', disable = ['ner'])
rulerPlants = EntityRuler(nlp, overwrite_ents=True)

# For API

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


# def analyze_text(text):
# 	return nlp(text)

@app.route('/')
def index():
	# raw_text = "Bill Gates is An American Computer Scientist since 1986"
	# docx = nlp(raw_text)
	# html = displacy.render(docx,style="ent")
	# html = html.replace("\n\n","\n")
	# result = HTML_WRAPPER.format(html)

	return render_template('index.html')

@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		rulerPlants = EntityRuler(nlp, overwrite_ents=True)
		flowers = ["rose","tulip","african daisy"]
		for f in flowers:
			rulerPlants.add_patterns([{"label": "flower", "pattern": f}])
		# for animal entity
		animals = ["cat", "dog", "artic fox"]
		rulerAnimals = EntityRuler(nlp, overwrite_ents=True)
		for a in animals:
			rulerAnimals.add_patterns([{"label": "animal", "pattern": a}])

		# for adding ruler name
		rulerPlants.name = 'rulerPlants'
		rulerAnimals.name = 'rulerAnimals'
		# adding entity to pipeline
		nlp.add_pipe(rulerPlants)
		nlp.add_pipe(rulerAnimals)
		# Reading document
		docx = nlp(raw_text)
		html = displacy.render(docx,style="ent")
		html = html.replace("\n\n","\n")
		result = HTML_WRAPPER.format(html)

		return render_template('result.html',rawtext=raw_text,result=result)


@app.route('/previewer')
def previewer():
	return render_template('previewer.html')

@app.route('/preview',methods=["GET","POST"])
def preview():
	if request.method == 'POST':
		newtext = request.form['newtext']
		result = newtext

	return render_template('preview.html',newtext=newtext,result=result)


if __name__ == '__main__':
	app.run(debug=True)
