import os
import pandas as pd
import numpy as np
import xlsxwriter
workbook = xlsxwriter.Workbook('./saved_result/keyword_per_year.xlsx')
worksheet = workbook.add_worksheet()

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

# make dictionary
a = {}

#len(df)
for i in range(1):
    print(list_keyword[i][0].encode("utf-8"))
    list_temp = list_keyword[i][0].encode("utf-8")
    key = list_temp
    a.setdefault(key,[])
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            if df.get_value(row,col) == list_temp:  # compare keyword and whole file
                year = df.iloc[row,1]
                a[key].append(year)  # save years in dictionary with key(keyword)
                break
    print(a)


row = 0
col = 0
for keyword in a.keys():
    worksheet.write(row, col, keyword)
    for item in a[keyword]:
        worksheet.write(row, col, keyword)
        worksheet.write(row, col+1, item)
        row += 1
workbook.close()
