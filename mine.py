import spacy
import scispacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import CONFIG
from data_management import text_2df

def unique(arr_list):
  new_list = []

  for one_arr_choice in arr_list:
      if one_arr_choice not in new_list:
          new_list.append(one_arr_choice)
  return new_list

def diseaseExtract(text):
  dataofx = CONFIG.nlp_obj(text)
  results = [ent.text for ent in dataofx.ents if ent.label_ == 'DISEASE']
  return unique(results)

def chemicalExtract(text):
  dataofx = CONFIG.nlp_obj(text)
  results = [ent.text for ent in dataofx.ents if ent.label_ == 'CHEMICAL']
  return unique(results)

def organExtract(text):
  dataofxobj2 = CONFIG.nlp_obj2(text)
  results = [ent.text for ent in dataofxobj2.ents if ent.label_ == 'ORGAN']
  return unique(results)

def get_common_disease(df,x):
  disease_list = df['Key Disease'].tolist()
  disease_list = [i for j in disease_list for i in j]
  return unique(disease_list)

def plot_disease_cloud(text):
  mywordcloud = WordCloud().generate(text)
  plt.imshow(mywordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.show()

def get_common_chemicals(df,x):
  chemical_list = df['Key Chemicals'].tolist()
  chemical_list = [i for j in chemical_list for i in j]
  return unique(chemical_list)


def spacy_mine():
    df = text_2df()
    df['Key Disease'] = df['Text'].apply(lambda x:diseaseExtract(x))
    df['Key Chemicals'] = df['Text'].apply(lambda x:chemicalExtract(x))
    surgery_disease = get_common_disease(df,'Surgery')
    chemicals = get_common_chemicals(df,'Chemicals')
    df['Affected Organ'] = df['Text'].apply(lambda x:organExtract(x))
    df['Past Key Disease'] = df['PAST MEDICAL HISTORY :'].apply(lambda x:diseaseExtract(x))
    return df

# print(spacy_mine())

