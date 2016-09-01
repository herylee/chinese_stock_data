#!/usr/bin/python

############################################
#
# description: caculate ma line
#
###########################################

import sqlite3
from collections import deque


def avg(list):
    sum = 0
    for i in list:
        sum+=i[1]
    return round(sum/len(list), 4)

def main():
    conn = sqlite3.connect('../../chinese_stock.db')

    tablename = "sse_composite_index"
    matimes = 90
    sqlstring = "select exchange_date, end_index from " + tablename + " order by exchange_date desc" 
    cursor = conn.execute(sqlstring) 

    list = []
    for row in cursor:
        list.append((row[0], float(row[1])))

    count = len(list)
    if count < matimes:
        return

    queue = deque()
    for i in range(0, matimes-1):
        queue.append(list.pop())
    count-=(matimes-1)
    lastavgindex = 0
    while count > 0:
        tail = list.pop()
        queue.append(tail)
        avgindex = avg(queue)
        exchangedate = tail[0]
        begindate = queue.popleft()[0]
        item = (exchangedate, begindate, avgindex, lastavgindex)
        print('%10s %10s %.4f %.4f'%item)
        
        tablename = "sse_composite_index_ma" + str(matimes)
        sqlstring = "insert into " + tablename + "(exchange_date, begin_date, avg_index, last_avg_index) values(?, ?, ?, ?)"
        conn.execute(sqlstring, item)
        lastavgindex = avgindex

        count-=1
        
    conn.commit()
    
    conn.close()


if __name__ == '__main__':
    main()
