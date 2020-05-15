from __future__ import unicode_literals
from spacy.scorer import Scorer
from flask import Flask, render_template, request
from spacy import displacy
import pytextrank
import spacy
from collections import defaultdict
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
from spacy.matcher import Matcher
from spacy.tokens import Span
import pandas as pd
import docx2txt
from collections import Counter
import re
import string
import codecs

nlp = spacy.load('en_core_web_sm')

scorer = Scorer()


def extract_json(raw_text):


	# TITLE
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

	rulerAll = EntityRuler(nlp, overwrite_ents=True)

	# Add all patterns in respective entity
	# Title

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

	# Add rulerAll to patterns

	rulerAll = EntityRuler(nlp, overwrite_ents=True)



	# For Title entity

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


	# HOLISTIC NAME FOR RULER
	rulerAll.name = 'rulerAll'
	if 'rulerAll' not in nlp.pipe_names:
	 	nlp.add_pipe(rulerAll)



	with nlp.disable_pipes('ner'):
		doc = nlp(raw_text)
	threshold = 0.2
	beams = nlp.entity.beam_parse([doc], beam_width=3, beam_density=0.0001)
	entity_scores = defaultdict(float)
	for beam in beams:
		for score, ents in nlp.entity.moves.get_beam_parses(beam):
			for start, end, label in ents:
				entity_scores[(start, end, label)] += score
	ent_custom = []
	ent_label = []
	ent_score = []
	for key in entity_scores:
		start, end, label = key
		score = entity_scores[key]
		if (score > threshold):
			ent_custom.append(label)
			ent_label.append(str(doc[start:end]))
			ent_score.append(score)
	df_ent_score = pd.DataFrame({'ENT_DETECT': [], 'ENT_LABEL': [], 'CONFIDENCE': []})
	df_ent_score['ENT_DETECT']=ent_custom
	df_ent_score['ENT_LABEL']=ent_label
	df_ent_score['CONFIDENCE']=ent_score
	df_custom_ent=df_ent_score[(df_ent_score.ENT_DETECT=="TITLE") | (df_ent_score.ENT_DETECT=="CLIENT") |(df_ent_score.ENT_DETECT=="SUPPLIER")
		| (df_ent_score.ENT_DETECT=="COUNTRIES")| (df_ent_score.ENT_DETECT=="Effective-DATES")| (df_ent_score.ENT_DETECT=="Signature-DATES")
		| (df_ent_score.ENT_DETECT=="Termination-DATES")| (df_ent_score.ENT_DETECT=="Commencement-DATES")| (df_ent_score.ENT_DETECT=="END-DATES")
		| (df_ent_score.ENT_DETECT=="CLIENT_CONTRACT_MANAGER")| (df_ent_score.ENT_DETECT=="SUPPLIER_CONTRACT_MANAGER")
		| (df_ent_score.ENT_DETECT=="DATE")]
	df_ent_dup=df_custom_ent.copy()
	df_ent_dup = df_ent_dup.drop_duplicates(subset=["ENT_DETECT"])
	df_ent_dup=df_ent_dup.reset_index(drop=True)
	df_ent_dup.index = df_ent_dup.index + 1
	json_table = df_ent_dup.to_json(orient='index')

	return json_table

