import camelot

tables = camelot.read_pdf('foo.pdf', pages ='1')
print(tables)

tables.export('foo.csv', f='csv' , compress=True)
tables[0].df.to_csv("foo.csv", index=False)
# represnts the 1st table (there is only one table in this pdf as well)
# table is extracted from pdf and foo.csv is created 

#print(tables[0].df)


    
