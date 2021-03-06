#IMPORTING KEY MODULES

import os
import pandas as pd
import streamlit as st
import pdftotext # For pdfto text conversion
import docx2txt # for converting docx to .txt format

# FOR NER

from spacy.pipeline import EntityRuler
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm', disable = ['ner'])


#  Wrapper for spacy visuals
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


#FOR NLP INSTANCE ANALYSIS
#@st.cache(allow_output_mutation=True)
def analyze_text(text):
	return nlp(text)


# Our Main logic

def main():
    """Summary AND NER App"""

    st.title("LEGAL TECH")

    activities = ['Extract MetaData From TEXT',
                  "Extract Metadata From Text File",
                  "Extract MetaData from .docx File",
                  "Extract MetaData from .pdf File",
                  "Find key entities in document"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Extract MetaData From TEXT':
        st.subheader("Extract MetaData from Legal Documents")
        raw_text = st.text_area("Enter Text Here", "Type Here")

        # Read text as spacy token instant

        def analyze_text(text):
            return nlp(text)

        # Add all CUSTOM patterns in respective entity
        # PATTERN FOR TITLES

        # Applying NLP ideas

        title1 = ["Agreement on contract1"]
        title2 = ["Agreement on contract2"]
        title3 = ["Agreement on contract3"]
        title4 = ["Agreement on contract4"]
        title5 = ["Agreement on contract5"]
        title6 = ["Agreement on contract6"]
        title7 = ["Agreement on contract7"]
        title8 = ["Agreement on contract8"]
        title9 = ["Agreement on contract9"]
        suppliers1 = ["FACEBOOK", "Facebook", "FACEBOOK GLOBAL INVEST AG", "Facebook Global Invest AG"]
        suppliers2 = ["BIRD", "BIRDS Deutschland GmbH", "Birds Deutschland GmbH"]
        suppliers3 = ["Google GmbH", "GOOGLE"]
        suppliers4 = ["EBAY Deutschland AG", "EBAY", "ebay"]
        suppliers5 = ["AMAZON SERVICES GMBH", "Amazon Services GmbH", "AMAZON LIMITED", "Amazon Limited"]
        clients = ["BOL.com", "bol.com", "BOL.COM BUSINESS SERVICES GMBH", "BOL.com Business Services GmbH"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018", " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["termination after a period of 48 months"]
        dates4 = ["31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]


        # Define rulerAll for all entities
        rulerAll = EntityRuler(nlp, overwrite_ents=True)

        # Add all patterns in respective entity
        for tit1 in title1:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

        for tit2 in title2:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

        for tit3 in title3:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

        for tit4 in title4:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

        for tit5 in title5:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

        for tit6 in title6:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

        for tit7 in title7:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

        for tit8 in title8:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

        for tit9 in title9:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

        # for supplier

        for s1 in suppliers1:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        # for clients

        for c1 in clients:
            rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

        for t2 in dates2:
            rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

        for t3 in dates3:
            rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

        for t4 in dates4:
            rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

        for t5 in dates5:
            rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # for countries

        for count1 in countries1:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

        for count2 in countries2:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Define Ruler for All

        rulerAll.name = 'rulerAll'
        nlp.add_pipe(rulerAll)

        # Getting text input

        if st.button("Extract"):
            docx2 = analyze_text(raw_text)
            html = displacy.render(docx2, style="ent")
            html = html.replace("\n\n", "\n")
            # st.write(html, unsafe_allow_html=True)
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)

# FOR SECOND CHALLENGE....reading from file

    if choice == 'Extract Metadata From Text File':
        st.subheader("Extract MetaData from Given Text File")
        def file_selector(folder_path='.'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Please only Select a Text File', filenames)
            return os.path.join(folder_path, selected_filename)

        filename = file_selector()


        f = open(filename)
        st.write('You have selected `%s`' % filename)

        raw=f.read()
        raw_text2 = st.text_area("your file contains following text", raw)  # for storing in raw text

        # DEFINE ANALYISIS FUNCTION

        def analyze_text(text):
            return nlp(text)

        # Applying NLP ideas

        title1 = ["Agreement on contract1"]
        title2 = ["Agreement on contract2"]
        title3 = ["Agreement on contract3"]
        title4 = ["Agreement on contract4"]
        title5 = ["Agreement on contract5"]
        title6 = ["Agreement on contract6"]
        title7 = ["Agreement on contract7"]
        title8 = ["Agreement on contract8"]
        title9 = ["Agreement on contract9"]
        suppliers1 = ["FACEBOOK", "Facebook", "FACEBOOK GLOBAL INVEST AG", "Facebook Global Invest AG"]
        suppliers2 = ["BIRD", "BIRDS Deutschland GmbH", "Birds Deutschland GmbH"]
        suppliers3 = ["Google GmbH", "GOOGLE"]
        suppliers4 = ["EBAY Deutschland AG", "EBAY", "ebay"]
        suppliers5 = ["AMAZON SERVICES GMBH", "Amazon Services GmbH", "AMAZON LIMITED", "Amazon Limited"]
        clients = ["BOL.com", "bol.com", "BOL.COM BUSINESS SERVICES GMBH", "BOL.com Business Services GmbH"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018", " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["termination after a period of 48 months"]
        dates4 = ["31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]

        # Define rulerAll for all entities
        rulerAll = EntityRuler(nlp, overwrite_ents=True)

        # Add all patterns in respective entity
        for tit1 in title1:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

        for tit2 in title2:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

        for tit3 in title3:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

        for tit4 in title4:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

        for tit5 in title5:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

        for tit6 in title6:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

        for tit7 in title7:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

        for tit8 in title8:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

        for tit9 in title9:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

        # for supplier

        for s1 in suppliers1:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        # for clients

        for c1 in clients:
            rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

        for t2 in dates2:
            rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

        for t3 in dates3:
            rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

        for t4 in dates4:
            rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

        for t5 in dates5:
            rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # for countries

        for count1 in countries1:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

        for count2 in countries2:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Define Ruler for All

        rulerAll.name = 'rulerAll'
        nlp.add_pipe(rulerAll)

        # analysis from loaded file

        if st.button("Extract"):
            document = analyze_text(raw_text2)
            html = displacy.render(document, style="ent")
            html = html.replace("\n\n", "\n")
            # st.write(html, unsafe_allow_html=True)
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)

    # FOR THIRD CHALLENGE....reading from file

    if choice == 'Extract MetaData from .docx File':
        st.subheader("Extract MetaData from .docx File")

        def file_selector(folder_path='.'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Please only Select a .docx File', filenames)
            return os.path.join(folder_path, selected_filename)

        filename = file_selector()

        f = open(filename)
        st.write('You have selected `%s`' % filename)
        docx_file = docx2txt.process(filename)
        #raw = docx_file.read()
        raw_text3 = st.text_area("your file contains following text", docx_file)  # for storing in raw text

        # DEFINE ANALYISIS FUNCTION

        def analyze_text(text):
            return nlp(text)

        # Applying NLP ideas

        title1 = ["Agreement on contract1"]
        title2 = ["Agreement on contract2"]
        title3 = ["Agreement on contract3"]
        title4 = ["Agreement on contract4"]
        title5 = ["Agreement on contract5"]
        title6 = ["Agreement on contract6"]
        title7 = ["Agreement on contract7"]
        title8 = ["Agreement on contract8"]
        title9 = ["Agreement on contract9"]
        suppliers1 = ["FACEBOOK", "Facebook", "FACEBOOK GLOBAL INVEST AG", "Facebook Global Invest AG"]
        suppliers2 = ["BIRD", "BIRDS Deutschland GmbH", "Birds Deutschland GmbH"]
        suppliers3 = ["Google GmbH", "GOOGLE"]
        suppliers4 = ["EBAY Deutschland AG", "EBAY", "ebay"]
        suppliers5 = ["AMAZON SERVICES GMBH", "Amazon Services GmbH", "AMAZON LIMITED", "Amazon Limited"]
        clients = ["BOL.com", "bol.com", "BOL.COM BUSINESS SERVICES GMBH", "BOL.com Business Services GmbH"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018", " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["termination after a period of 48 months"]
        dates4 = ["31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]

        # Define rulerAll for all entities
        rulerAll = EntityRuler(nlp, overwrite_ents=True)

        # Add all patterns in respective entity
        for tit1 in title1:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

        for tit2 in title2:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

        for tit3 in title3:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

        for tit4 in title4:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

        for tit5 in title5:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

        for tit6 in title6:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

        for tit7 in title7:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

        for tit8 in title8:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

        for tit9 in title9:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

        # for supplier

        for s1 in suppliers1:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        # for clients

        for c1 in clients:
            rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

        for t2 in dates2:
            rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

        for t3 in dates3:
            rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

        for t4 in dates4:
            rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

        for t5 in dates5:
            rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # for countries

        for count1 in countries1:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

        for count2 in countries2:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Define Ruler for All

        rulerAll.name = 'rulerAll'
        nlp.add_pipe(rulerAll)


    # analysis from loaded file


        if st.button("Extract"):

            document3 = analyze_text(raw_text3)
            html = displacy.render(document3, style="ent")
            html = html.replace("\n\n", "\n")
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)


    # FOR FOURTH CHALLENGE....reading from PDF file

    if choice == 'Extract MetaData from .pdf File':
        st.subheader("Extract MetaData from .pdf File")

        def file_selector(folder_path='.'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Please only Select a .docx File', filenames)
            return os.path.join(folder_path, selected_filename)

        filename = file_selector()

        f = open(filename)
        st.write('You have selected `%s`' % filename)

        with open(filename, "rb") as pdf:
            pdf_file = pdftotext.PDF(pdf)
        # converting pdftotext.PDF to string type
        pdf_text = ("\n\n".join(pdf_file))
        raw_text4 = st.text_area("your file contains following text", pdf_text)  # for storing in raw text

        # DEFINE ANALYISIS FUNCTION

        def analyze_text(text):
            return nlp(text)
        # Applying NLP ideas

        title1 = ["Agreement on contract1"]
        title2 = ["Agreement on contract2"]
        title3 = ["Agreement on contract3"]
        title4 = ["Agreement on contract4"]
        title5 = ["Agreement on contract5"]
        title6 = ["Agreement on contract6"]
        title7 = ["Agreement on contract7"]
        title8 = ["Agreement on contract8"]
        title9 = ["Agreement on contract9"]
        suppliers1 = ["FACEBOOK", "Facebook", "FACEBOOK GLOBAL INVEST AG", "Facebook Global Invest AG"]
        suppliers2 = ["BIRD", "BIRDS Deutschland GmbH", "Birds Deutschland GmbH"]
        suppliers3 = ["Google GmbH", "GOOGLE"]
        suppliers4 = ["EBAY Deutschland AG", "EBAY", "ebay"]
        suppliers5 = ["AMAZON SERVICES GMBH", "Amazon Services GmbH", "AMAZON LIMITED", "Amazon Limited"]
        clients = ["BOL.com", "bol.com", "BOL.COM BUSINESS SERVICES GMBH", "BOL.com Business Services GmbH"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018", " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["termination after a period of 48 months"]
        dates4 = ["31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]

        # Define rulerAll for all entities
        rulerAll = EntityRuler(nlp, overwrite_ents=True)

        # Add all patterns in respective entity
        for tit1 in title1:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

        for tit2 in title2:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

        for tit3 in title3:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

        for tit4 in title4:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

        for tit5 in title5:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

        for tit6 in title6:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

        for tit7 in title7:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

        for tit8 in title8:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

        for tit9 in title9:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

        # for supplier

        for s1 in suppliers1:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        # for clients

        for c1 in clients:
            rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

        for t2 in dates2:
            rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

        for t3 in dates3:
            rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

        for t4 in dates4:
            rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

        for t5 in dates5:
            rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # for countries

        for count1 in countries1:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

        for count2 in countries2:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Define Ruler for All

        rulerAll.name = 'rulerAll'
        nlp.add_pipe(rulerAll)

        # analysis from loaded file

        if st.button("Extract"):
            document4 = analyze_text(raw_text4)
            html = displacy.render(document4, style="ent")
            html = html.replace("\n\n", "\n")
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)

        # FOR FIFTH CHALLENGE....reading from file

    if choice == 'Find key entities in document':
        st.subheader("Extract MetaData from Given Text File")

        def file_selector(folder_path='.'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Please only Select a Text File', filenames)
            return os.path.join(folder_path, selected_filename)

        filename = file_selector()

        f = open(filename)
        st.write('You have selected `%s`' % filename)

        raw = f.read()
        raw_text5 = st.text_area("your file contains following text", raw)  # for storing in raw text

        # DEFINE ANALYISIS FUNCTION

        def analyze_text(text):
            return nlp(text)

        # Applying NLP ideas

        title1 = ["Agreement on contract1"]
        title2 = ["Agreement on contract2"]
        title3 = ["Agreement on contract3"]
        title4 = ["Agreement on contract4"]
        title5 = ["Agreement on contract5"]
        title6 = ["Agreement on contract6"]
        title7 = ["Agreement on contract7"]
        title8 = ["Agreement on contract8"]
        title9 = ["Agreement on contract9"]
        suppliers1 = ["FACEBOOK", "Facebook", "FACEBOOK GLOBAL INVEST AG", "Facebook Global Invest AG"]
        suppliers2 = ["BIRD", "BIRDS Deutschland GmbH", "Birds Deutschland GmbH"]
        suppliers3 = ["Google GmbH", "GOOGLE"]
        suppliers4 = ["EBAY Deutschland AG", "EBAY", "ebay"]
        suppliers5 = ["AMAZON SERVICES GMBH", "Amazon Services GmbH", "AMAZON LIMITED", "Amazon Limited"]
        clients = ["BOL.com", "bol.com", "BOL.COM BUSINESS SERVICES GMBH", "BOL.com Business Services GmbH"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018", " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["termination after a period of 48 months"]
        dates4 = ["31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023", "19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]

        # Define rulerAll for all entities
        rulerAll = EntityRuler(nlp, overwrite_ents=True)

        # Add all patterns in respective entity
        for tit1 in title1:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit1}])

        for tit2 in title2:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit2}])

        for tit3 in title3:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit3}])

        for tit4 in title4:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit4}])

        for tit5 in title5:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit5}])

        for tit6 in title6:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit6}])

        for tit7 in title7:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit7}])

        for tit8 in title8:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit8}])

        for tit9 in title9:
            rulerAll.add_patterns([{"label": "TITLE", "pattern": tit9}])

        # for supplier

        for s1 in suppliers1:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerAll.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        # for clients

        for c1 in clients:
            rulerAll.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerAll.add_patterns([{"label": "Effective-DATES", "pattern": t1}])

        for t2 in dates2:
            rulerAll.add_patterns([{"label": "Signature-DATES", "pattern": t2}])

        for t3 in dates3:
            rulerAll.add_patterns([{"label": "Termination-DATES", "pattern": t3}])

        for t4 in dates4:
            rulerAll.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])

        for t5 in dates5:
            rulerAll.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # for countries

        for count1 in countries1:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

        for count2 in countries2:
            rulerAll.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

         # Define Ruler for All

        rulerAll.name = 'rulerAll'
        nlp.add_pipe(rulerAll)

        # analysis from loaded file

        if st.button("Extract"):
            doc5 = analyze_text(raw_text5)
            # Adding a Dataframe
            df_ent = pd.DataFrame({'TEXT': [], 'ENT_LABEL': [], 'START': [], 'END': []})
            df_ent['TEXT'] = [x.text for x in doc5.ents]
            df_ent['ENT_LABEL'] = [x.label_ for x in doc5.ents]
            df_ent['START'] = [x.start_char for x in doc5.ents]
            df_ent['END'] = [x.end_char for x in doc5.ents]
            # Filering entities to be shown
            df_table = df_ent[
                (df_ent.ENT_LABEL == "TITLE") | (df_ent.ENT_LABEL == "CLIENT") | (df_ent.ENT_LABEL == "SUPPLIER")
                | (df_ent.ENT_LABEL == "COUNTRIES") | (df_ent.ENT_LABEL == "Effective-DATES") | (
                            df_ent.ENT_LABEL == "Signature-DATES")
                | (df_ent.ENT_LABEL == "Termination-DATES") | (df_ent.ENT_LABEL == "Commencement-DATES") | (
                            df_ent.ENT_LABEL == "END-DATES")
                | (df_ent.ENT_LABEL == "CLIENT_CONTRACT_MANAGER") | (df_ent.ENT_LABEL == "SUPPLIER_CONTRACT_MANAGER")]
            df_ent_dup = df_table.copy()
            df_ent_dup = df_ent_dup.drop_duplicates(subset=["ENT_LABEL"])
            # Output shown on app
            st.write('Key Entities Found in Contract : ', df_ent_dup)


if __name__ == '__main__':
    main()