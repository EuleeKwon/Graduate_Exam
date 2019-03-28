# merge every xlsx file to one
# just use program..
import pandas as pd
from pandas import ExcelWriter
import numpy as np
import os


file_list = os.listdir('./keys_per_year/')
print(file_list)

all_data = pd.DataFrame()
for i in range(len(file_list)):
    print(i)
    data = pd.read_excel('./keys_per_year/' + file_list[i])
    all_data = all_data.append(data, ignore_index=True)

print(all_data.shape)
all_data.to_excel('D:/dataset/PUBMED/Combining_Data.xlsx', index=False)
print("Done")