import streamlit as st
import os

import os
import streamlit as st
# FOR NER
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
def main():
    st.title("LEGAL TECH")

    def file_selector(folder_path='.'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox('Please only Select a Text File', filenames)
        return os.path.join(folder_path, selected_filename)
    filename = file_selector()
    st.write('You have selected `%s`' % filename)
    # Reading data from this file
    f = open(filename)
    raw = f.read()
    raw_text2 = st.text_area("your file contains following text", raw)  # for storing in raw text
    #raw_text = st.text_area("Enter Text Here", "Type Here")

    def analyze_text(text):
        return nlp(text)
    if st.button("Analyze"):
        docx = analyze_text(raw_text2)
        html = displacy.render(docx, style="ent")
        html = html.replace("\n\n", "\n")
        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)

if __name__ == '__main__':
    main()