import os
import pandas as pd
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

file_list = os.listdir('./keys_per_year/')
print(file_list)

list_all=[]
#df = pd.read_excel('./keys_per_year/keyword_year1.xlsx')

#only open year data in file
for i in range(len(file_list)):
    data = pd.read_excel('./keys_per_year/' + file_list[i])
    # erase year and pid
    data_column1 = data.iloc[:,1]
    df = data_column1.drop_duplicates()
    list_df = df.values.tolist()
    print("New List")
    print(list_df)

    list_all += list_df
    list_all_final = list(set(list_all))
    print("Merged List")
    print(list_all_final)

# save list as excel
for i, e in enumerate(list_all_final):
    sheet1.write(i, 0, e)
book.save("year_list.xls")
