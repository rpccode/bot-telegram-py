import pandas as pd


data = pd.read_csv(
    'marketing_sample_for_amazon_com-ecommerce__20200101_20200131__10k_data.csv')


def datos():
    print(data.head(10))
