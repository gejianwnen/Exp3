# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:02:19 2020

@author: gejianwen
"""
import pandas as pd
import numpy as np
import time


def fit_units(df):
#     unit I and U
    df["Ic"] = df["Ic"]*10
    df["Uce"] = df["Uce"]*30-1.65
    # reset time base
    t_base = "2019/10/01 00:00:00"
    stamp_base = time.mktime(time.strptime(t_base,"%Y/%m/%d %H:%M:%S"))
    df["t"] = df["t"]-stamp_base
    # round to meaningful values
    df["Ic"] = df["Ic"].round(4)
    df["Uce"] = df["Uce"].round(4)
    df["Tbase_Cu"] = df["Tbase_Cu"].round(2)
    df["Tsink_IGBT3_1"] = df["Tsink_IGBT3_1"].round(2)
    df["Tj_IGBT3_1"] = df["Tj_IGBT3_1"].round(2)
    try:
        df["Tsink_IGBT3_1"] = df["Tsink_IGBT3_1"].round(2)
        df["Tj_IGBT3_1"] = df["Tj_IGBT3_1"].round(2)
    except:
        pass
    
    return df