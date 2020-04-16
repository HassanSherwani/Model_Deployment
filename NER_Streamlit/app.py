#IMPORTING KEY MODULES

import os
import pandas as pd
import streamlit as st
import pdftotext # For pdfto text conversion
import docx2txt # for converting docx to .txt format
import re
import string
from collections import Counter
import sys
import pandas as pd
from collections import defaultdict
# FOR NER
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
nlp = English() # this will disable all normal NERs


# define CUSTOM ENTITY RULER
rulerTitle = EntityRuler(nlp, overwrite_ents=True)
rulerSupplier = EntityRuler(nlp, overwrite_ents=True)
rulerClient = EntityRuler(nlp, overwrite_ents=True)
rulerDate = EntityRuler(nlp, overwrite_ents=True)
rulerCountries = EntityRuler(nlp, overwrite_ents=True)

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

    activities = ['Extract MetaData From TEXT',"Extract Metadata From Text File",
                  "Extract MetaData from .docx File","Extract MetaData from .pdf ","Find key entities in document"]
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

        title1 = ["Agreement on Managed Data Center Services"]
        title2 = ["Master Services Agreement on the Provision of IT Services",
                      "Master Services Agreement on the Provision of IT Services (“Agreement“ or “Master Services Agreement”)"]
        title3 = ["MASTER SERVICES AGREEMENT ON THE PROVISION OF MANAGED SERVICES IN PUBLIC COULDS",
                      "Master Services Agreement (“Agreement“ or “Master Services Agreement”) on the provision of Managed Services in Public Clouds"]
        title4 = ["Agreement on the Provision of MANAGED PRINT Services",
                      "Agreement on the Provision of MPS (Managed Print Services)"]
        title5 = ["Agreement for Security Operation Center Services"]
        title6 = ["AGREEMENT ON PROVISIONING OF IT AND COMMUNICATION SERVICES"]
        title7 = ["Agreement on Managed Data Center Services"]
        title8 = ["Master Project, Support and Maintenance Agreement"]

        suppliers2 = ["TEASYS", "Teasys", "TEASYS GLOBAL INVEST AG", "Teasys Global Invest AG"]
        suppliers3 = ["FTP", "FTP Deutschland GmbH", "FTP Deutschland GmbH"]
        suppliers4 = ["Wisniewski & Sohn GmbH", "Contractor", "contractor", "FBS"]
        suppliers5 = ["Horizon Deutschland AG", "Horizon", "Harpe", "Harpe Deutschland GmbH"]
        suppliers6 = ["ADVENTURE SERVICES GMBH", "Adventure Services GmbH", "SWIPERO LIMITED", "Swipero Limited",
                          "Swipero"]
        clients = ["F.UN", "FUN", "F.UN BUSINESS SERVICES GMBH", "F.UN Business Services GmbH", "FBS","Anonymous company"]
        dates1 = ["29 September 2018", "01 January 2015", "01.07.2018",
                      " August 2017"]
        dates2 = ["31. July 2018"]
        dates3 = ["after a period of 48 months","19.01.2020"]
        dates4 = [ "31.01.2017", "31.03.2019", "1 October 2018"]
        dates5 = ["31.12.2018", "Apr 11th 2023"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India","Poland"]
        countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania"]

        # Add all CUSTOM patterns in respective entity
        # PATTERN FOR TITLES

        for tit1 in title1:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit1}])
        for tit2 in title2:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit2}])
        for tit3 in title3:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit3}])
        for tit4 in title4:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit4}])
        for tit5 in title5:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit5}])
        for tit6 in title6:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit6}])
        for tit7 in title7:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit7}])
        for tit8 in title8:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit8}])

        # PATTERN FOR SUPPLIER

        for s2 in suppliers2:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        for s6 in suppliers6:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s6}])

        # PATTERN FOR CLIENT

        for c1 in clients:
            rulerClient.add_patterns([{"label": "CLIENT", "pattern": c1}])

        # Pattern for DATES

        for t1 in dates1:
            rulerDate.add_patterns([{"label": "Effective-DATES", "pattern": t1}])
        for t2 in dates2:
            rulerDate.add_patterns([{"label": "Signature-DATES", "pattern": t2}])
        for t3 in dates3:
            rulerDate.add_patterns([{"label": "Termination-DATES", "pattern": t3}])
        for t4 in dates4:
            rulerDate.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])
        for t5 in dates5:
            rulerDate.add_patterns([{"label": "END-DATES", "pattern": t5}])

        # PATTERN FOR COUNTRIES

        for count1 in countries1:
            rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count1}])
        for count2 in countries2:
            rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Give a holistic name for ruler

        rulerTitle.name = 'rulerTitle'
        rulerSupplier.name = 'rulerSupplier'
        rulerClient.name = 'rulerClient'
        rulerDate.name = 'rulerDate'
        rulerCountries.name = 'rulerCountries'

        # Add ruler to pipeline

        nlp.add_pipe(rulerTitle)
        nlp.add_pipe(rulerSupplier)
        nlp.add_pipe(rulerClient)
        nlp.add_pipe(rulerDate)
        nlp.add_pipe(rulerCountries)

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

        title1 = ["Agreement on Managed Data Center Services"]
        title2=["Master Services Agreement on the Provision of IT Services","Master Services Agreement on the Provision of IT Services (“Agreement“ or “Master Services Agreement”)"]
        title3=["MASTER SERVICES AGREEMENT ON THE PROVISION OF MANAGED SERVICES IN PUBLIC COULDS","Master Services Agreement (“Agreement“ or “Master Services Agreement”) on the provision of Managed Services in Public Clouds"]
        title4=["Agreement on the Provision of MANAGED PRINT Services","Agreement on the Provision of MPS (Managed Print Services)"]
        title5=["Agreement for Security Operation Center Services"]
        title6 = ["AGREEMENT ON PROVISIONING OF IT AND COMMUNICATION SERVICES"]
        title7=["Agreement on Managed Data Center Services"]
        title8=["Master Project, Support and Maintenance Agreement"]

        suppliers2 = ["TEASYS", "Teasys", "TEASYS GLOBAL INVEST AG","Teasys Global Invest AG"]
        suppliers3 = ["FTP", "FTP Deutschland GmbH", "FTP Deutschland GmbH"]
        suppliers4 = ["Wisniewski & Sohn GmbH", "Contractor","contractor","FBS"]
        suppliers5 = ["Horizon Deutschland AG" , "Horizon", "Harpe" , "Harpe Deutschland GmbH"]
        suppliers6=["ADVENTURE SERVICES GMBH","Adventure Services GmbH" ,"SWIPERO LIMITED","Swipero Limited","Swipero"]
        clients = ["F.UN", "FUN", "F.UN BUSINESS SERVICES GMBH", "F.UN Business Services GmbH","FBS","Anonymous company"]
        dates1 = ["effective date", "Effective Date","29 September 2018","01 January 2015","01.07.2018"," August 2017"]
        dates2 = ["signature date", "Signature Date","31. July 2018"]
        dates3 = ["termination date", "Termination Date","termination after a period of 48 months"]
        dates4 = ["Commencement Date", "Service Commencement Date","31.01.2017","31.03.2019","1 October 2018"]
        dates5=["END Dates","31.12.2018","Apr 11th 2023","19.01.2020"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia","Hungary","India"]
        countries2=["Slovakia","Czech","Australia","Vietnam","Japan","Philippines","Romania","Poland"]

        # Add all CUSTOM patterns in respective entity
        # PATTERN FOR TITLES

        for tit1 in title1:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit1}])
        for tit2 in title2:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit2}])
        for tit3 in title3:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit3}])
        for tit4 in title4:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit4}])
        for tit5 in title5:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit5}])
        for tit6 in title6:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit6}])
        for tit7 in title7:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit7}])
        for tit8 in title8:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit8}])

        # PATTERN FOR SUPPLIER


        for s2 in suppliers2:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

        for s5 in suppliers5:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

        for s6 in suppliers6:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s6}])

        #PATTERN FOR CLIENT
        for c1 in clients:
            rulerClient.add_patterns([{"label": "CLIENT", "pattern": c1}])
        # Pattern for DATES
        for t1 in dates1:
            rulerDate.add_patterns([{"label": "Effective-DATES", "pattern": t1}])
        for t2 in dates2:
            rulerDate.add_patterns([{"label": "Signature-DATES", "pattern": t2}])
        for t3 in dates3:
            rulerDate.add_patterns([{"label": "Termination-DATES", "pattern": t3}])
        for t4 in dates4:
            rulerDate.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])
        for t5 in dates5:
            rulerDate.add_patterns([{"label": "END-DATES", "pattern": t5}])
        # PATTERN FOR COUNTRIES

        for count1 in countries1:
            rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count1}])
        for count2 in countries2:
            rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

        # Give a holistic name for ruler

        rulerTitle.name = 'rulerTitle'
        rulerSupplier.name = 'rulerSupplier'
        rulerClient.name = 'rulerClient'
        rulerDate.name = 'rulerDate'
        rulerCountries.name = 'rulerCountries'

        # Add ruler to pipeline

        nlp.add_pipe(rulerTitle)
        nlp.add_pipe(rulerSupplier)
        nlp.add_pipe(rulerClient)
        nlp.add_pipe(rulerDate)
        nlp.add_pipe(rulerCountries)

        # analysis from loaded file

        if st.button("Extract"):
            document = analyze_text(raw_text2)
            html = displacy.render(document, style="ent")
            html = html.replace("\n\n", "\n")
            # st.write(html, unsafe_allow_html=True)
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)

        # FOR THIRD CHALLENGE....reading from file

        if choice == 'Extract MetaData from .docx File':
            st.subheader("Extract MetaData from .docx")

            def file_selector(folder_path='.'):
                filenames = os.listdir(folder_path)
                selected_filename = st.selectbox('Please only Select a .docx File', filenames)
                return os.path.join(folder_path, selected_filename)

            filename = file_selector()

            f = open(filename)
            st.write('You have selected `%s`' % filename)
            doc=docx2txt.process(f)
            raw = doc.read()
            raw_text3 = st.text_area("your file contains following text", raw)  # for storing in raw text

            # DEFINE ANALYISIS FUNCTION

            def analyze_text(text):
                return nlp(text)

            # Applying NLP ideas

            title1 = ["Agreement on Managed Data Center Services"]
            title2 = ["Master Services Agreement on the Provision of IT Services",
                      "Master Services Agreement on the Provision of IT Services (“Agreement“ or “Master Services Agreement”)"]
            title3 = ["MASTER SERVICES AGREEMENT ON THE PROVISION OF MANAGED SERVICES IN PUBLIC COULDS",
                      "Master Services Agreement (“Agreement“ or “Master Services Agreement”) on the provision of Managed Services in Public Clouds"]
            title4 = ["Agreement on the Provision of MANAGED PRINT Services",
                      "Agreement on the Provision of MPS (Managed Print Services)"]
            title5 = ["Agreement for Security Operation Center Services"]
            title6 = ["AGREEMENT ON PROVISIONING OF IT AND COMMUNICATION SERVICES"]
            title7 = ["Agreement on Managed Data Center Services"]
            title8 = ["Master Project, Support and Maintenance Agreement"]

            suppliers2 = ["TEASYS", "Teasys", "TEASYS GLOBAL INVEST AG", "Teasys Global Invest AG"]
            suppliers3 = ["FTP", "FTP Deutschland GmbH", "FTP Deutschland GmbH"]
            suppliers4 = ["Wisniewski & Sohn GmbH", "Contractor", "contractor", "FBS"]
            suppliers5 = ["Horizon Deutschland AG", "Horizon", "Harpe", "Harpe Deutschland GmbH"]
            suppliers6 = ["ADVENTURE SERVICES GMBH", "Adventure Services GmbH", "SWIPERO LIMITED", "Swipero Limited",
                          "Swipero"]
            clients = ["F.UN", "FUN", "F.UN BUSINESS SERVICES GMBH", "F.UN Business Services GmbH", "FBS",
                       "Anonymous company"]
            dates1 = ["effective date", "Effective Date", "29 September 2018", "01 January 2015", "01.07.2018",
                      " August 2017"]
            dates2 = ["signature date", "Signature Date", "31. July 2018"]
            dates3 = ["termination date", "Termination Date", "termination after a period of 48 months"]
            dates4 = ["Commencement Date", "Service Commencement Date", "31.01.2017", "31.03.2019", "1 October 2018"]
            dates5 = ["END Dates", "31.12.2018", "Apr 11th 2023", "19.01.2020"]
            countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia", "Hungary", "India"]
            countries2 = ["Slovakia", "Czech", "Australia", "Vietnam", "Japan", "Philippines", "Romania", "Poland"]

            # Add all CUSTOM patterns in respective entity
            # PATTERN FOR TITLES

            for tit1 in title1:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit1}])
            for tit2 in title2:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit2}])
            for tit3 in title3:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit3}])
            for tit4 in title4:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit4}])
            for tit5 in title5:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit5}])
            for tit6 in title6:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit6}])
            for tit7 in title7:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit7}])
            for tit8 in title8:
                rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit8}])

            # PATTERN FOR SUPPLIER

            for s2 in suppliers2:
                rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

            for s3 in suppliers3:
                rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

            for s4 in suppliers4:
                rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s4}])

            for s5 in suppliers5:
                rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s5}])

            for s6 in suppliers6:
                rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s6}])

            # PATTERN FOR CLIENT
            for c1 in clients:
                rulerClient.add_patterns([{"label": "CLIENT", "pattern": c1}])
            # Pattern for DATES
            for t1 in dates1:
                rulerDate.add_patterns([{"label": "Effective-DATES", "pattern": t1}])
            for t2 in dates2:
                rulerDate.add_patterns([{"label": "Signature-DATES", "pattern": t2}])
            for t3 in dates3:
                rulerDate.add_patterns([{"label": "Termination-DATES", "pattern": t3}])
            for t4 in dates4:
                rulerDate.add_patterns([{"label": "Commencement-DATES", "pattern": t4}])
            for t5 in dates5:
                rulerDate.add_patterns([{"label": "END-DATES", "pattern": t5}])
            # PATTERN FOR COUNTRIES

            for count1 in countries1:
                rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count1}])
            for count2 in countries2:
                rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count2}])

            # Give a holistic name for ruler

            rulerTitle.name = 'rulerTitle'
            rulerSupplier.name = 'rulerSupplier'
            rulerClient.name = 'rulerClient'
            rulerDate.name = 'rulerDate'
            rulerCountries.name = 'rulerCountries'

            # Add ruler to pipeline

            nlp.add_pipe(rulerTitle)
            nlp.add_pipe(rulerSupplier)
            nlp.add_pipe(rulerClient)
            nlp.add_pipe(rulerDate)
            nlp.add_pipe(rulerCountries)

            # analysis from loaded file

            if st.button("Extract"):
                document = analyze_text(raw_text3)
                html = displacy.render(document, style="ent")
                html = html.replace("\n\n", "\n")
                # st.write(html, unsafe_allow_html=True)
                st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)


if __name__ == '__main__':
    main()