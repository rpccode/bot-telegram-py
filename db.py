import pandas as pd
import pyodbc as pyodbc
import asyncio
import base64

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=RUDY\MSSQLSERVER1;"
            "Database=adventureworks;"
            "UID=user;"
            "PWD=password;"
            )
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

result = cursor.execute("SELECT * FROM SalesLT.Product").fetchall()


def traer_productos():
    data = pd.read_sql("SELECT * FROM SalesLT.Product", cnxn)
    return data


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
            cursor.execute(f"SELECT TOP 5 * FROM SalesLT.Product as p where p.ProductNumber='{num}'")

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


def traer_productos_por_categoria(cat):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"select TOP 10  p.ProductNumber,p.Name,p.Color,p.ListPrice,p.Size,p.Weight,c.Name from SalesLT.Product AS P "
                f"LEFT JOIN SalesLT.ProductCategory as c on p.ProductCategoryID = c.ProductCategoryID where c.Name "
                f"like('%{cat}');")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "


def traer_username(text):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"select top 1 * from dbo.LoginU where UserName = '{text}';")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "


def login(text, pas):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"select top 1 * from SalesLT.LoginU where UserName = '{text}' and Password = '{pas}';")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "


def estado_orden(user, estado):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"Select oh.SalesOrderNumber,a.AddressLine1,oh.ShipMethod,oh.SubTotal,oh.TaxAmt,oh.Freight,"
                f"oh.TotalDue from SalesLT.SalesOrderHeader as oh left join SalesLT.Address as a on "
                f"oh.ShipToAddressID = a.AddressID where oh.CustomerID = '{user}' and oh.Status ='{estado}';")

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "


def registrar_usuario_nuevo(user,pas,emal,id):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            consulta="INSERT INTO SalesLT.LoginU(UserName,Password,Email,idcliente)  VALUES(?, ?,?,?);"
            cursor.execute(consulta,(f'{user}',f'{pas}',f'{emal}',f'{id}'))

            # Con fetchall traemos todas las filas
            productos = cursor.fetchall()

            return productos
    except Exception as e:
        return f"Ocurrió un error al consultar: {e} "