import os
import CONFIG
import pandas as pd
from bs4 import BeautifulSoup

def xml_2text(text_path):
    with open(text_path, 'r') as f:
        data = f.read()

    bs_data = BeautifulSoup(data, 'xml')
    b_text = bs_data.find_all('TEXT')
    return b_text

def attr_valmap():
    b_text = xml_2text(CONFIG.DATA_DIR)
    cache = []
    memory = []
    bag_ofwords = []
    attr_val = []

    for ele in b_text:
        cache.append(str(ele))

    for ele in cache:
        memory.append(ele.split("\n"))

    for i in range(len(memory)):
        attr_cache = {}
        for j in range(len(memory[i])):
            cache_str = ''
            if (memory[i][j] != '') & (memory[i][j][-1] == ':'):
                bag_ofwords.append(memory[i][j])
                k = j+1
                
                cond = True
                try:
                    while (k<len(memory[i])) & (memory[i][k][-1] != ':'):
                        cache_str = cache_str + memory[i][k]
                        k = k + 1
                except:
                    continue
    #             print(cache_str)
                attr_cache[memory[i][j]] = cache_str
        attr_val.append(attr_cache)
    return attr_val

def text_2df():
    features = ["PRINCIPAL DIAGNOSIS :","ASSOCIATED DIAGNOSIS :","HISTORY OF PRESENT ILLNESS :",
            "PAST MEDICAL HISTORY :","PHYSICAL EXAMINATION :", "LABORATORY DATA :"
            ]
    
    b_text = xml_2text(CONFIG.DATA_DIR)
    attr_val = attr_valmap()
    temp = []
    indx = []
    new_text = []
    for idx,ele0 in enumerate(attr_val):
        new_data = {}
        try:
            for ele in features:
                new_data[ele] = ele0[ele]
            temp.append(new_data)
            indx.append(idx)
        except:
            continue
    
    dict_2df = pd.DataFrame.from_dict(temp)
    for idx in range(len(indx)):
        new_text.append(b_text[indx[idx]])
    
    text_df = pd.DataFrame(new_text,columns=["Text"])
    dict_2df = dict_2df.merge(text_df,left_index=True, right_index=True)
    return dict_2df
