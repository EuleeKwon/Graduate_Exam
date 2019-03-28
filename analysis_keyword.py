import os
import pandas as pd
import xlwt
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

file_list = os.listdir('./keys_per_year/')
print(file_list)

list_all=[]
#df = pd.read_excel('./keys_per_year/keyword_year1.xlsx')

for i in range(len(file_list)):
    data = pd.read_excel('./keys_per_year/' + file_list[i])
    # erase year and pid
    df = data.drop([0], axis=1)
    df = data.drop([1], axis=1)
    print(pd.DataFrame(df))
    print(df.columns)

# load column2 to max(82), and save as list
# 75 doesn't work
# 64 doesn't work, 63 works
    for k in range(2, 63):
        list_df = df[k].tolist()
        list_all += list_df
    # erase same value in list
    list_all_final = list(set(list_all))
    # erase nan value in list
    list_all_clean = [x for x in list_all_final if str(x) != 'nan']
    print(list_all_clean)

    # save list as excel
for i, e in enumerate(list_all_clean):
    sheet1.write(i, 0, e)
book.save("keyword_list.xls")

