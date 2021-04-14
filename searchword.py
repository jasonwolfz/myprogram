import re
import prettytable as pt

#1
filename_1 = 'doc1'
searchword_1 = 'he'

openfile_1 = open(filename_1+'.txt','r')
readfile1 = openfile_1.read()

count = 0

#2
lines = re.split(r'([.!?])',readfile1)
lines = ["".join(i) for i in zip(lines[0::2],lines[1::2])]

table_1 = pt.PrettyTable()
table_1.field_names = ['Word (Total Occurrences)','Documents','Sentences containing the word']

#3
for line in lines:
   res = re.findall(searchword_1,line,re.I)
   if res == []:
      continue
   else:
      count = count+1
      table_1.add_row(['','',line])

#4      
count = str(count)
table_1.align = 'c'
table_1.valign = 'm'
table_1.add_row([searchword_1+'('+count+')',filename_1,''])
print(table_1)
