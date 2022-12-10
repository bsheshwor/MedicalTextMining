import os
import pandas
from data_management import text_2df
from mine import spacy_mine


def df_2json():
    df = spacy_mine()
    df.to_json("data/mined_json.json")


if __name__ == "__main__":
    df_2json()