import tablib

# create a dataset
data = tablib.Dataset()

# Add rows
data.append(["A", 1])
data.append(["B", 2])
data.append(["C", 3])

# save as csv
with open('test.csv', 'wb') as f:
    f.write(data.csv)

# save as Excel
with open('test.xls', 'wb') as f:
    f.write(data.xls)

# save as Excel 07+
with open('test.xlsx', 'wb') as f:
    f.write(data.xlsx)


#  tablib library is a small little library to work with tabular data and write csv and Excel files.