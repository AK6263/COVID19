# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:22:07 2020

@author: Abhay Kshirsagar
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

data = pd.read_csv('c:/Users/Abhay Kshirsagar/Desktop/data.csv')


#cleaning for china data as we want for the entire mainland
China = data.loc[data["Country/Region"] == 'China']
provinces = pd.unique(China["Province/State"]).tolist()
dates = pd.unique(China["Date"]).tolist()
conf_china = []
for i in dates:
    count = [] # count for each country on ith date
    for j in provinces:
        a = China.loc[(China["Province/State"] == j) & (China["Date"] == i)]
        b = a["Confirmed"].tolist()
        count.append(b[0])
    conf_china.append(sum(count))

cols = ['India','Korea','US']
India = data.loc[data["Country/Region"] == 'India']
Korea = data.loc[data["Country/Region"] == 'Korea']
US = data.loc[data["Country/Region"] == 'US']
india = India['Confirmed'].tolist()
korea = Korea['Confirmed'].tolist()
us = US['Confirmed'].tolist()
"""
India.plot(x ='Date')
Korea.plot(x='Date')
"""
def logit(l): #helps us log each value of a list
    a = []
    for i in l:
        if i==0.0:
            a.append(i)
        else:
            a.append(math.log(i))
    return a
i = logit(india)
k = logit(korea)
u = logit(us)
c = logit(conf_china)
days = range(1,82)
plt.plot(days,i,label = 'India')
plt.plot(days,k,label='Korea')
plt.plot(days,u,label ='US')
plt.plot(days,c,label = 'China')
plt.legend(loc="down right")

"""
import numpy as np
i = np.array(i)
k = np.array(k)
u = np.array(u)
deri = np.diff(i)/np.diff(days)
derk = np.diff(k)/np.diff(days)
deru = np.diff(u)/np.diff(days)
days = range(1,81)
plt.plot(days,deri,label="deri")
plt.plot(days,derk,label="derk")
plt.plot(days,deru,label="deru")
plt.legend(loc="down right")
"""
