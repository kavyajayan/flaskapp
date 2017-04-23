import dbconnect

datas=dbconnect.fetch()
for row in datas:
	print(row[0], row[1])
print ("Ended for loop")
