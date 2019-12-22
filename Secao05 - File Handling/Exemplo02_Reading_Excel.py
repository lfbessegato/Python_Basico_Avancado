import pandas as pd
import xlrd
file = pd.ExcelFile("Sales.xls")
print(file.sheet_names)

sheet = file.parse('sales')
print(sheet)
print(type(sheet))
print("Date: ", sheet.Date)
print("Soma total de Amount: ", sheet.Amount.sum())
print("Localizar: ", sheet.loc[0])
print("Localizar segundo elemento: ", sheet.loc[0, "Amount"])

sheet.set_index("Customer", inplace=True)
print(sheet.loc["MMC Inc."])

sheet = sheet.reset_index()
print(sheet["Invoice"])
print(type(sheet["Invoice"]))

print(sheet.loc[sheet["Invoice"] == 99])
print(sheet.loc[sheet["Amount"] > 2000])
print(sheet.loc[sheet["Amount"].idxmax()])
print(sheet.loc[sheet["Amount"].idxmax()]["Customer"])
print(sheet.loc[sheet["Amount"] > 1800])
print(sheet.loc[sheet["Amount"] > 1800]["Customer"])
print(sheet.loc[sheet["Amount"] > 1800]["Customer"].unique())
print(sheet.loc[sheet["Amount"] > 1800]["Customer"].unique()[0])

for customer in sheet.loc[sheet["Amount"] > 1800]["Customer"].unique():
    print(customer)