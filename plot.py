import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import ast

keys_list = ['Key Disease','Key Chemicals','Key Organ','Key Gene']
def frequency_plot():

    df = pd.read_csv("data/dataframecsv.csv")
    organ_list = []

    for ele in df['Organ'].tolist():
        organ_list.append(ast.literal_eval(ele))

    organs = []
    for ele in organ_list:
        for ele0 in ele:
            organs.append(ele0)

    size = len(organs)

    organ_df = pd.DataFrame(organs, columns=['organ'])
    organ_df = organ_df.groupby(['organ']).size().reset_index(name='frequency')
    organ_df['Percent'] = np.round(organ_df['frequency']*100/size,2)

# ax = organ_df.plot.bar(x='organ', y='Percent', rot=0)
