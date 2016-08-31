#!/usr/bin/python

import sqlite3

def avg(list):
    sum = 0
    for i in list:
        sum+=i
    return sum//len(list)

conn = sqlite3.connect('../../chinese_stock.db')

tablename = "sse_composite_index"
exchangedate = "2016-07-01"
number = 30
sqlstring = "select end_index from " + tablename + " where exchange_date < date('" + exchangedate + "') order by exchange_date desc limit " + str(number)
cursor = conn.execute(sqlstring) 

list = []
for row in cursor:
    list.append(float(row[0]))

print list
print('avg %d is %.4f'%(number, avg(list)))
conn.close()
