import openpyxl

book = openpyxl.load_workbook(r'C:\Users\pmantiuk\Desktop\267.xlsm')
sheet = book['query']

print(sheet['A11'].value)