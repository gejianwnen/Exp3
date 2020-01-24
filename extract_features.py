# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:04:21 2020

@author: gejianwen
"""
import pandas as pd


def extract_features(df):
    # extract power and Rth
    df["Power"] = df["Ic"]*df["Uce"]
    df["dT_IGBT3_1"] = df["Tj_IGBT3_1"]-df["Tsink_IGBT3_1"]
    df["Rth_IGBT3_1"] = df["dT_IGBT3_1"]/df["Power"]
    try:
        df["dT_IGBT3_2"] = df["Tj_IGBT3_2"]-df["Tsink_IGBT3_2"]
        df["Rth_IGBT3_2"] = df["dT_IGBT3_2"]/df["Power"]
    except:
        pass

    return df