# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:58:51 2020

@author: gejianwen
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_hist(df):
    for col in df.columns.values:
        plt.figure(figsize = (7,4))
        plt.hist(df[col].values,bins = 10)
        plt.title(col)
        plt.show()