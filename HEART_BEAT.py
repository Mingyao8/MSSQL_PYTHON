import time
import pyodbc
import pandas as pd
import random
count = 0
while(count < 10):
    time.sleep(3)
    beat = random.randint(50, 100)
    try:
        conn1 = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=YYAAOO;'
                                'Database=mingyao;'
                                'Trusted_Connection=yes;')
        cursor1 = conn1.cursor()
    
        # UPDATE 語句
        sql = '''
            UPDATE heart
            SET heart_beat = ?
            WHERE id = 1;
        '''
        # 執行 SQL 語句
        cursor1.execute(sql, beat)
        conn1.commit()
        print("update OK!")
    except pyodbc.Error as ex:
        print("Error:", ex)
    
    finally:
        conn1.close()
    
    
    try:
        conn2 = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=YYAAOO;'
                                'Database=mingyao;'
                                'Trusted_Connection=yes;')
        cursor2 = conn2.cursor()
    
        # UPDATE 語句
        sql = '''
            SELECT heart_beat FROM heart
        '''
        cursor2.execute(sql)
        conn2.commit()
        # 執行 SQL 語句
        cursor2.execute(sql)
        print('beat: ' + str(cursor2.fetchall()[0][0]))
    except pyodbc.Error as ex:
        print("Error:", ex)
    
    finally:
        conn2.close()
    count += 1