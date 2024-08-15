import pyodbc
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv("C:\\Users\\user\\Desktop\\HW.csv")
df = df.fillna(0)
print(df)

# 建立連線
try:
    conn1 = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=YYAAOO;'
                            'Database=mingyao;'
                            'Trusted_Connection=yes;')
    cursor1 = conn1.cursor()

    #CREATE
    col_defs = [f"[{col}] FLOAT" for col in df.columns if col != 'DateTime']
    col_defs.insert(0, "[DateTime] NVARCHAR(50)")
    print(col_defs)
    _sql = f'''
    CREATE TABLE HW1 (
        {', '.join(col_defs)}
    );
    '''
    cursor1.execute(_sql)
    conn1.commit()
    print("OK!")
    
except pyodbc.Error as ex:
    print("Error:", ex)

finally:
    conn1.close()