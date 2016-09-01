#!/usr/bin/python

import sqlite3
import sys

def avg(list):
    sum = 0
    for i in list:
        sum+=i
    return sum//len(list)


conn = sqlite3.connect('../../chinese_stock.db')

tablename = "sse_composite_index"
exchangedate = "2016-07-01"
number = 30
sqlstring = "select exchange_date, end_index from " + tablename + " where exchange_date < date('" + exchangedate + "') order by exchange_date desc limit " + str(number)
cursor = conn.execute(sqlstring) 

list = []
print('%20s %20s'%('exchange_date', 'end_index'))
for row in cursor:
    print('%20s %20s'%(row[0], row[1]))
    list.append(float(row[1]))

print list
print('avg %d is %.4f'%(number, avg(list)))
conn.close()
