import matplotlib.pyplot as plt

import ydata_profiling as pp 
from ydata_profiling import profile_report
import pandas as pd

data = pd.read_csv("baggagecomplaints.csv")
'''
ppd=pp.ProfileReport(data)
ppd.to_file('index.html')
print(data.head())
print('----------------------')
print(data.info())
print('----------------------')
print(data.describe())
print('----------------------')
print(data.tail())
'''
#Normal distribution Test

years=list(set(data['Year']))
totallist=[]
a=0
b=0
c=0
d=0
e=0
f=0
g=0
for k in range(len(data)): 
    if data['Year'][k]==2004: 
        a+=data['Cancelled'][k]
    if data['Year'][k]==2005: 
        b+=data['Cancelled'][k]
    if data['Year'][k]==2006: 
        c+=data['Cancelled'][k]
    if data['Year'][k]==2007: 
        d+=data['Cancelled'][k]
    if data['Year'][k]==2008: 
        e+=data['Cancelled'][k]
    if data['Year'][k]==2009: 
        f+=data['Cancelled'][k]   
    if data['Year'][k]==2010: 
        g+=data['Cancelled'][k]                   
totallist.append(a) 
totallist.append(b) 
totallist.append(c) 
totallist.append(d) 
totallist.append(e) 
totallist.append(f)
totallist.append(g)  

print(years,totallist)   
     

plt.plot(years,totallist)
plt.show()

#shapiro test
import scipy 
import numpy as np
from scipy.stats import shapiro


#formal test-total
data = [24497, 23111, 30481, 34959, 29507, 17647, 17146]
stat, p_value = shapiro(data)

alpha = 0.05
if p_value > alpha:
    print("Data is normally distributed.")
else:
    print("Data is not normally distributed.")
    
#Individual-Tests
AmEag=[17787,
16746,
19990,
22792,
18331,
11119,
12075,
]   
stat,p_value=shapiro(AmEag)
if p_value>alpha: 
    print('Am-Eag Data is normally Distributed') 
else: 
    print("Data is not normally distributed.") 

Hawain=[162,
69,
253,
238,
570,
150,
61
]  

stat,p_value=shapiro(Hawain)
if p_value>alpha: 
    print('Hawaiin Data is normally Distributed') 
else: 
    print("Data is not normally distributed.")   


United=[6548,
6296,
10238,
11929,
10606,
6378,
5010,
]    

stat,p_value=shapiro(United)
if p_value>alpha: 
    print('United Data is normally Distributed') 
else: 
    print("Data is not normally distributed.")
    
        