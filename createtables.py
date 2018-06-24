# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:45:42 2018

@author: Mfundo Bright Shabalala
"""

import sys
import MySQLdb
#from warnings import filterwarnings

#filterwarnings("ignore", category = MySQLdb.Warning)
conn=MySQLdb.connect(host="localhost", user="root", passwd="password", db="prml")
cursor=conn.cursor()

try:
    cursor.execute("""
    DROP TABLE IF EXISTS stocks
                    """)
    print("Affected: %d " %cursor.rowcount)

except MySQLdb.Error, e:
    print("Error occured: %s " %e.args[0])
    print(e)

try:
    cursor.execute("""
    create table stocks(stock_id int unsigned primary key AUTO_INCREMENT, 
    ticker char(11) NOT NULL, stock_name char(100))
                   """)

except MySQLdb.Error:
    print("Error in creating stocks table")
    sys.exit(1)
cursor.close()
conn.close()
