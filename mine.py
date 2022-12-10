import spacy
import scispacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import CONFIG
from data_management import text_2df


def diseaseExtract(text):
  dataofx = CONFIG.nlp_obj(text)
  results = [ent.text for ent in dataofx.ents if ent.label_ == 'DISEASE']
  return results

def chemicalExtract(text):
  dataofx = CONFIG.nlp_obj(text)
  results = [ent.text for ent in dataofx.ents if ent.label_ == 'CHEMICAL']
  return results

def organExtract(text):
  dataofxobj2 = CONFIG.nlp_obj2(text)
  results = [ent.text for ent in dataofxobj2.ents if ent.label_ == 'ORGAN']
  return results

def get_common_disease(df,x):
  disease_list = df['Disease'].tolist()
  disease_list = [i for j in disease_list for i in j]
  return disease_list

def plot_disease_cloud(text):
  mywordcloud = WordCloud().generate(text)
  plt.imshow(mywordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.show()

def get_common_chemicals(df,x):
  chemical_list = df['Chemicals'].tolist()
  chemical_list = [i for j in chemical_list for i in j]
  return chemical_list


def spacy_mine():
    df = text_2df()
    # for i in range(df.shape[0]):
    #     x = df['Text'][i]
    #     dataofx= CONFIG.nlp_obj(x)
    #     df.loc[i,['Disease','Chemicals']] = [diseaseExtract(x),chemicalExtract(x)]
    
    df['Disease'] = df['Text'].apply(lambda x:diseaseExtract(x))
    df['Chemicals'] = df['Text'].apply(lambda x:chemicalExtract(x))

    surgery_disease = get_common_disease(df,'Surgery')
    chemicals = get_common_chemicals(df,'Chemicals')

    df['Organ'] = df['Text'].apply(lambda x:organExtract(x))


    return df
