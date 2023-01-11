import pandas as pd
import pyodbc as pyodbc
import asyncio
import base64
from smtp import *

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=RUDY\MSSQLSERVER1;"
            "Database=adventureworks;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cursor = cnxn.cursor()

result = cursor.execute("SELECT * FROM SalesLT.Product").fetchall()


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

def traer_productos_por_num1(num):
    try:
        with cnxn.cursor() as cursor:
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(f"SELECT TOP 1 * FROM SalesLT.Product as p where p.ProductNumber='{num}'")

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
                f"select  top 10 * from SalesLT.Product as p where  p.ListPrice >={desde} and p.ListPrice <= {hasta};")

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
                f"select top 1 * from SalesLT.LoginU where UserName = '{text}';")

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


def registrar_usuario_nuevo(user, pas, emal, id):
    try:
        with cnxn.cursor() as cursor:
            noCount = " SET NOCOUNT ON; "
            # En este caso no necesitamos limpiar ningún dato
            consulta = "INSERT into SalesLT.LoginU(UserName,Password,Email,idcliente)  VALUES(?, ?,?,?);"
            cursor.execute(consulta, (f'{user}', f'{pas}', f'{emal}', f'{id}'))
            cnxn.commit()

            email_registro(emal)
            return 1

    except Exception as e:
        return 1, f"Ocurrió un error al consultar: {e} "


def Cancel_orden(num,emal):
    try:
        with cnxn.cursor() as cursor:
            noCount = " SET NOCOUNT ON; "
            # En este caso no necesitamos limpiar ningún dato
            cursor.execute(
                f"Select oh.SalesOrderNumber,a.AddressLine1,oh.ShipMethod,oh.SubTotal,oh.TaxAmt,oh.Freight,"
                f"oh.TotalDue from SalesLT.SalesOrderHeader as oh left join SalesLT.Address as a on "
                f"oh.ShipToAddressID = a.AddressID where oh.SalesOrderNumber = '{num}';")

            # Con fetchall traemos todas las filas
            producto = cursor.fetchall()
            email_cancelacion_orden(emal,producto)

            consulta = f"update SalesLT.SalesOrderHeader set Status = 6 where SalesOrderNumber ='{num}';"
            cursor.execute(consulta)
            cnxn.commit()
            return 1


    except Exception as e:
        return 0 ,  f"Ocurrió un error al consultar: {e} "

# INSERT[SalesLT].[SalesOrderHeader]([SalesOrderID], [RevisionNumber], [OrderDate], [DueDate], [ShipDate], [Status],
#                                    [OnlineOrderFlag], [PurchaseOrderNumber], [AccountNumber], [CustomerID],
#                                    [ShipToAddressID], [BillToAddressID], [ShipMethod], [CreditCardApprovalCode],
#                                    [SubTotal], [TaxAmt], [Freight], [Comment], [rowguid], [ModifiedDate])
# VALUES(71947, 2, CAST(N
# '2008-06-01T00:00:00.000'
# AS
# DateTime), CAST(N
# '2008-06-13T00:00:00.000'
# AS
# DateTime), CAST(N
# '2008-06-08T00:00:00.000'
# AS
# DateTime), 5, 0, N
# 'PO8468183315', N
# '10-4020-000016', 29975, 635, 635, N
# 'CARGO TRANSPORT 5', NULL, 88812.8625, 7105.0290, 2220.3216, NULL, N
# 'a36ee74a-cf0d-4024-a1ce-4eaffd1f85f6', CAST(N
# '2008-06-08T00:00:00.000'
# AS
# DateTime))