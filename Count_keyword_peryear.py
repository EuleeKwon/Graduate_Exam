import os
import pandas as pd
import numpy as np

#import list to use
df1 = pd.read_excel('./saved_result/keyword_list(63).xlsx',header=None)
df2 = pd.read_excel('./saved_result/year_list.xlsx',header=None)
list_keyword = df1.values.tolist()
list_year = df2.values.tolist()

#import data(combined)
#df = pd.read_excel(r'D:/dataset/PUBMED/Combining_Data.xlsx')
df = pd.read_excel('./keys_per_year/keyword_year1.xlsx')

# print(len(list_keyword))
# print(len(list_year))
# print(pd.DataFrame(df))

keyword_per_year = []
for i in range(1):
    print(list_keyword[i][0].encode("utf-8"))
    list_temp = list_keyword[i][0].encode("utf-8")
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            if df.get_value(row,col) == list_temp:
                print(df.iloc[row,1])
                print(type(df.iloc[row,1]))
                keyword_per_year += df.iloc[row,1]
                break
print(keyword_per_year)