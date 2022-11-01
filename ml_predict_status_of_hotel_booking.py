# -*- coding: utf-8 -*-
"""ML-Predict status of Hotel Booking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11OXSWwo1z_Ms0rE6zX-oT7F0jd3FWnRS

**data cleaning and data prepeartion for modeling **
"""

#IMPORT library 
# for extraction, manipulation and validation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

"""url = 'https://github.com/thatsme10001/ML-Predict-status-of-Hotel-Booking/blob/hotel_booking.csv'
df = pd.read_csv(url)"""

df = pd.read_csv('/content/hotel_booking.csv')   #data that you need to read
                                                 # df --- anonymized  data form object.

df.head   #call a head to get a preview how exactly my data looks like

df.shape #number of rows  and number of columns

df.isna()   #check how many missing value we have
           # na means is null value available
          # is na -- is null

df.isna().sum    # .sum -- summation of all the missing values in your data 
                 #figure out you have that much huge number of missing values available in the data

def data_clean(df):             #define data_clean function over dara so that we can deal with missinf or null values
  df.fillna(0,inplace=True)   #fill my missing values with zero and then update them (inplace=True)
  print(df.isnull().sum())    #after  all the manipulations of data whether I have any null value or not so far

data_clean(df)    #don't have any missing value in your data   
                  #exactly what we want

df.columns   # show all cloumns in the dataset 
             #we need perprocessing of data 
             # for exapmple in this data set 'adults', 'children', 'babies' cant be zero at the same time

list = ['adults', 'children', 'babies']   #create a list.

for i in list:
  print("{} has unique vallues as {}".format(i,df[i].unique()))   #check how many unique values //  df[i].unique()- find unique value
                   
                                                             # we can notice that in this data adult and these children and these babies can't have zero value and we have that in  our data 
                                                            # we will remove this data from dataset using a filter

filter = (df['children']==0) & (df['adults']==0) & (df['babies']==0) 
df[filter]

"""above setion we observed that we dont have your all the columns.
let me display my all the columns over here.
"""

pd.set_option ('display.max_columns',32)  #here I have 32 columns

filter = (df['children']==0) & (df['adults']==0) & (df['babies']==0) 
df[filter]   


    #here I have adult children, babies and all and these are zero.
    """But if you think logically, it is not possible that adults, children and babies at a time can be zero
    simultaneously.it means these are exactly your #noise."""

  #have to remove this.

data = df[~filter]    #negation of this filter. we use ~ to negotiate the data
data.head                     # data == ata on which you have to perform all your analysis on which you have to build

"""***analysis of data***

***visualize data on a map to ***
"""

def odd(n,m) :
  while m :
    n,m = m, n%m
    print(n)
  print("the last :", n)  

odd(35,12)

a = [1,2,3]
print(a[1:1])