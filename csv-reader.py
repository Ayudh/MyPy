# reads the data from a csv and processes accordingly
import csv

myfile = open('payumoney.csv', 'r')
reader = csv.reader(myfile)
data = list(reader)
myfile.close()

dict = {}
i = 1
# while data[i][0] != '':
# 	print data[i][1]
# 	i = i+ 1
# print data[i][0]
while i<len(data) and data[i][0] != '':
  if data[i][5] == "Payment Failed" or data[i][5] == "Payment Pending" or data[i][5] == "User Cancelled" or data[i][5] == "Settlement In Progress" or data[i][5] == "Payment Successful":
    i = i + 1
    continue
  if len(data[i][15].split('.')) != 9 + 1:
    i = i + 1
    continue
  if data[i][1] in dict:
    dict[data[i][1]] = dict[data[i][1]] + float(str(data[i][3]))
  else:
    dict[data[i][1]] = float(str(data[i][3]))
  i = i + 1

output = open('output.txt', 'w')

sum = 0
for i in dict.keys():
  sum = sum + float(str(dict[i]))

output.write(str(sum))
output.close()