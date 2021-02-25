import openpyxl as excel
wb = excel.Workbook()
ws = wb.active
ws["A1"] = "hello"
wb.save("hello.xlsx")