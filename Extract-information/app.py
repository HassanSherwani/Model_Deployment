#IMPORTING KEY MODULES


import streamlit as st
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



#@st.cache(allow_output_mutation=True)
def analyze_text(text):
	return nlp(text)


# Our Main logic

def main():
    """Summary AND NER App"""

    st.title("LEGAL TECH")

    activities = ["load file","Named Entity Recognition",'Extract MetaData']
    choice = st.sidebar.selectbox("Select Activity", activities)


    if choice == 'load file':
        st.subheader("Extract MetaData from Given File")

    # def file_selector(folder_path='.'):
    #    filenames = os.listdir(folder_path)
    #    selected_filename = st.selectbox('Select a file', filenames)
    #    return os.path.join(folder_path, selected_filename)

    # filename = file_selector()
    # st.write('You selected `%s`' % filename)


    if choice == 'Named Entity Recognition':
        st.subheader("Named Entity Recognition")
   #     raw_text = st.text_area("Enter Text Here", "Type Here")
   #     if st.button("Analyze"):
   #         docx = analyze_text(raw_text)
   #         html = displacy.render(docx, style="ent")
   #         html = html.replace("\n\n", "\n")
            #st.write(html, unsafe_allow_html=True)
   #         st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)

    if choice == 'Extract MetaData':
        st.subheader("Extract MetaData from Legal Documents")
        raw_text = st.text_area("Enter Text Here", "Type Here")

        title1 = ["Agreement on Managed Data Center Services"]
        suppliers1 = ["supplier", "SUPPLIER", "Supplier", "SuP"]
        suppliers2 = ["TEASYS", "Teasys", "TEASYS GLOBAL INVEST AG"]
        suppliers3 = ["FTP", "FTP Deutschland GmbH", "FTP Deutschland GmbH"]
        suppliers4 = ["Wisniewski & Sohn GmbH", "Contractor","FBS"]
        clients = ["F.UN", "FUN", "F.UN BUSINESS SERVICES GMBH", "F.UN Business Services GmbH"]
        dates1 = ["effective date", "Effective Date"]
        dates2 = ["signature date", "Signature Date"]
        dates3 = ["termination date", "Termination Date"]
        dates4 = ["Commencement Date", "Service Commencement Date"]
        countries1 = ["UK", "Germany", "France", "Italy", "Netherlands", "Russia"]

        # Add all CUSTOM patterns in respective entity
        # PATTERN FOR TITLES

        for tit1 in title1:
            rulerTitle.add_patterns([{"label": "TITLE", "pattern": tit1}])
        # PATTERN FOR SUPPLIER

        for s1 in suppliers1:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s1}])

        for s2 in suppliers2:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s2}])

        for s3 in suppliers3:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s3}])

        for s4 in suppliers4:
            rulerSupplier.add_patterns([{"label": "SUPPLIER", "pattern": s4}])
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
        # PATTERN FOR COUNTRIES

        for count1 in countries1:
            rulerCountries.add_patterns([{"label": "COUNTRIES", "pattern": count1}])

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


        if st.button("Analyze"):
            docx2 = analyze_text(raw_text)
            html = displacy.render(docx2, style="ent")
            html = html.replace("\n\n", "\n")
            # st.write(html, unsafe_allow_html=True)
            st.markdown(HTML_WRAPPER.format(html), unsafe_allow_html=True)
# for loading a file




if __name__ == '__main__':
    main()
# to render our NER in spacy we will be using displacy and wrap our result within an html

#HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""