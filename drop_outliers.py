# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:59:06 2020

@author: gejianwen
"""
import pandas as pd
import numpy as np

def drop_outliers(s, filter_size = 30,threshold = 2):
    data_size = s.shape[0]
    n = int(np.floor(data_size/filter_size))
    ix = np.array([])
    for i in range(n):
        s1 = s[filter_size*i:filter_size*(i+1)].values
        m = np.mean(s1)
        std = np.std(s1)
        outliers = np.any([s1 > m+threshold*std,s1 < m-threshold*std], axis = 0)
        ix = np.append(ix,outliers,axis = 0)
    s1 = s[filter_size*i+filter_size:].values
    m = np.mean(s1)
    std = np.std(s1)
    print(m)
    outliers = np.any([s1 > m+threshold*std,s1 < m-threshold*std], axis = 0)
    ix = np.append(ix,outliers,axis = 0)
    s = s[np.logical_not(ix)]
    
    return s,ix