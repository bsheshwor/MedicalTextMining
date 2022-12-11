import spacy
import scispacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import CONFIG
from data_management import text_2df

def plot_cloud(text, num):
  mywordcloud = WordCloud().generate(text)
  plt.imshow(mywordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.savefig(f"clouds/cloud{num}.png")

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

def geneExtract(text):
  dataofxobj2 = CONFIG.nlp_obj2(text)
  results = [ent.text for ent in dataofxobj2.ents if ent.label_ == 'GENE_OR_GENE_PRODUCT']
  return unique(results)

def get_common_disease(df):
  disease_list = df['Disease'].tolist()
  disease_list = [i for j in disease_list for i in j]
  return disease_list

def get_common_gene(df):
  gene_list = df['Gene'].tolist()
  gene_list = [i for j in gene_list for i in j]
  return gene_list

def get_common_organ(df):
  organ_list = df['Organ'].tolist()
  organ_list = [i for j in organ_list for i in j]
  return organ_list

def get_common_chemicals(df):
  chemical_list = df['Chemicals'].tolist()
  chemical_list = [i for j in chemical_list for i in j]
  return chemical_list

def plot_disease_cloud(text):
  mywordcloud = WordCloud().generate(text)
  plt.imshow(mywordcloud, interpolation='bilinear')
  plt.axis('off')
  plt.show()

def spacy_mine():
  df = text_2df()
  df['Disease'] = df['Text'].apply(lambda x:diseaseExtract(x))
  df['Chemicals'] = df['Text'].apply(lambda x:chemicalExtract(x))
  df['Organ'] = df['Text'].apply(lambda x:organExtract(x))
  df['Gene'] = df['Text'].apply(lambda x:geneExtract(x))
  surgery_disease = get_common_disease(df)
  chemicals = get_common_chemicals(df)
  organs = get_common_organ(df)
  genes = get_common_gene(df)
  plot_cloud(' '.join(surgery_disease),1)
  plot_cloud(' '.join(chemicals),2)
  plot_cloud(' '.join(organs),3)
  plot_cloud(' '.join(genes),4)
  return df

# print(spacy_mine())

