import pandas as pd
import openpyxl

# path of the excel file
my_file = r'C:\Users\Pro\Desktop\excelmarj\xldata.xlsx'
df = pd.read_excel(my_file, sheet_name=None)

df1 = pd.concat(df)

# path were to want master file
writer = pd.ExcelWriter(r'C:\Users\Pro\Desktop\excelmarj\master2.xlsx')

df1.to_excel(writer)
writer.save()