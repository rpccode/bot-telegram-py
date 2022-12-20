import pandas as pd
import pyodbc as pyodbc
import asyncio

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-LT26I1H\SQLEXPRESS;"
            "Database=adventureworks;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

result = cursor.execute("SELECT * FROM SalesLT.Product").fetchall()


def traer_productos():
    data = pd.read_sql("SELECT * FROM SalesLT.Product", cnxn)
    return data



