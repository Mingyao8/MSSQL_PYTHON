# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:52:07 2024

@author: Ming Yao
"""
import pyodbc
import pandas as pd

try:
    conn1 = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=YYAAOO;'
                            'Database=mingyao;'
                            'Trusted_Connection=yes;')
    cursor1 = conn1.cursor()
    # SELECT
    sql = '''
        SELECT * FROM [mingyao].[dbo].[HW1]
        WHERE DateTime = '1922/11/27 08:01:40'
    '''
    cursor1.execute(sql)
    res = cursor1.fetchall()
    conn1.commit()
    print(res)

except pyodbc.Error as ex:
    print("Error:", ex)

finally:
    conn1.close()