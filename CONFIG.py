import os
import spacy
import scispacy

#paths
BASE_DIR = os.getcwd()
TEMP_DIR = os.path.join(BASE_DIR, "data")
DATA_DIR = os.path.join(TEMP_DIR,"smokers_surrogate_train_all_version2.xml")
JSON_PATH = 'data/mined_json.json'

#LOAD MODELS
nlp_obj = spacy.load("en_ner_bc5cdr_md")
nlp_obj2 = spacy.load("en_ner_bionlp13cg_md")
