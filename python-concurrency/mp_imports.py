### This is to solve issues in Windows related to running MP on a Jupyter Notebook

import requests
import pandas as pd
import time

def download_single_page_mp(url, index):
    status = requests.get(url)
    print(status)
    return (index, status)


def convert_to_date_mp(df, columns_list):
    for col in columns_list:
        df[col] = pd.to_datetime(df[col])
    return df


def sleep_test_mp(param):
    time.sleep(param)
    return param*2