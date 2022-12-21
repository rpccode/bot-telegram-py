# import pandas as pd
import pyodbc as pyodbc
import asyncio
import base64

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=RUDY\MSSQLSERVER1;"
            "Database=adventureworks;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

result = cursor.execute("SELECT * FROM SalesLT.Product").fetchall()


# def traer_productos():
#     data = pd.read_sql("SELECT * FROM SalesLT.Product", cnxn)
#     return data


def traer_productos_formateados():
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute("select top 10 * from SalesLT.Product;")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_color(color):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 10 * FROM SalesLT.Product as p where p.Color  LIKE('%{color}%');")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "


def traer_productos_por_size(size):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 10 * FROM SalesLT.Product as p where p.Size  LIKE('%{size}%');")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_weight(weight):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 10 * FROM SalesLT.Product as p where p.Weight  LIKE('%{weight}%')")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_num(num):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 5 * FROM SalesLT.Product as p where p.ProductNumber  LIKE('%{num}%')")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_nombre(nombre):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 5 * FROM SalesLT.Product as p where p.Name  LIKE('%{nombre}%')")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_precio(desde, hasta):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"select  ListPrice from SalesLT.Product as p where  p.ListPrice >={desde} and p.ListPrice <= {hasta};")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "



def traer_productos_por_categoria():
    cat = 'bikes'
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"select p.ProductNumber,p.Name,p.Color,p.ListPrice,p.Size,p.Weight,c.Name from SalesLT.Product AS P "
                f"INNER JOIN SalesLT.ProductCategory as c on p.ProductCategoryID = c.ProductCategoryID where c.Name "
                f"like('%{cat}');")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "
    
