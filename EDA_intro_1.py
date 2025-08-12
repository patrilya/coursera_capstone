# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:03:23 2025

@author: patri
"""

import pandas as pd
file_name = 'Sales.xlsx'
data = pd.ExcelFile(file_name)
sheets = data.sheet_names
df = data.parse(sheets[0])
cols = df.columns
df.values # returns an array of arrays: [[el1],[el2] etc]
# where each el made up of all the cells of a respective row
# can index each el: df.values[0]; and df.values[0][0] to 
# get a cell's value

import seaborn as sns
import matplotlib.pyplot as plt

#sns.histplot(df,x='ItemPrice',binwidth=0.5)

#sns.histplot(df,x='ItemCost',binwidth=0.1)

x = df.dtypes # returns a Series

df1 = df[df['ProductSubcategory'].isin(['Gloves','Shorts'])]

df.select_dtypes('number').head()
df.select_dtypes('object').head()
df.select_dtypes('datetime').head()

import numpy as np
y = df.groupby('ProductSubcategory')['ItemPrice'].agg(
    [np.mean,np.median,'count'])


dct = {'ItemPrice':['mean','median','std'],
       'ItemCost':['mean','median'],
       }
df.agg(dct)


df.groupby('ProductCategory').agg(
    price_mean = ('ItemPrice','mean'),
    price_std = ('ItemPrice', 'std'),
    count = ('OrderNo','count')) # use when want to rename cols

# handling nans

df_original = df.iloc[:,:]
length = len(df)

threshold = 0.05 * length

condition_nan = df.isna().sum() <= threshold # returns a boolean Series

cols_to_drop = df.columns[condition_nan] # an index obj 
# w/ the columns that have less nans than the threshold.
4# here, all the cols except for ProductColor

df.dropna(subset=cols_to_drop, inplace=True) # drops rows 
# w/ nans in the cols that are mentioned in the subset arg

dct = df.groupby('ProductCategory')['ItemPrice'].mean().to_dict()
# returns a dict, where the keys are product categories and 
# the values are respective means.

series_1 = pd.Series([2,4,5], index=['a','b','c'])
# index is optional

lst = [1,5,7]
res = map(lambda x: x*2, lst) # 
res_lst = list(res)

data = {'name':['john','mary','harry'],
       'phone':[123,312,314],
       'city':['madrid','barcelona','valencia'],
       'grade_1':[42,24,56]}
df1 = pd.DataFrame(data)
series_dct = df1.to_dict('series')
# returns a dict, where the values are a series

dct_2 = df1.to_dict('dict')
# the values of each key are a dictionary: key = index value,
# value = the content of a cell

lst_dct = df1.to_dict('list')
# dict of lists. the col names are keys, and a list 
# of the col values are values

dct_1 = df.groupby(
    'ProductCategory')['ItemPrice'].agg([np.mean,np.median]).to_dict()


series_1.to_dict()


# mean imputation example

data = {'airline':['vueling','ryanair','easyjet','luft hansa'],
        'price':[100, np.nan ,120, np.nan]}

df1 = pd.DataFrame(data)

dct_impute = {'vueling':200,'ryanair':300,
              'easyjet':400,'luft hansa':800}

series_prices = df1['airline'].map(dct_impute)
df1['price'] = df1['price'].fillna(series_prices)
