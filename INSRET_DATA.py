# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:52:07 2024

@author: Ming Yao
"""
import pyodbc
import pandas as pd

df = pd.read_csv("C:\\Users\\user\\Desktop\\HW.csv")
df = df.fillna(0)
print(df)

try:
    conn1 = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=YYAAOO;'
                            'Database=mingyao;'
                            'Trusted_Connection=yes;')
    cursor1 = conn1.cursor()

    #INSERT
    col_names = [f"[DateTime]"] + [f"[{col}]" for col in df.columns if col != 'DateTime']
    placeholder = ', '.join(['?' for _ in df.columns])
    sql = f'''
    INSERT INTO HW1 ({', '.join(col_names)})
    VALUES ({placeholder})
    '''
    # 插入數據
    for row in df.itertuples(index=False):
        values = tuple(row)
        cursor1.execute(sql, values)
    
    conn1.commit()
    print("OK!")

except pyodbc.Error as ex:
    print("Error:", ex)

finally:
    conn1.close()