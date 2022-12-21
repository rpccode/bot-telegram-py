from pymssql import _mssql
conn = _mssql.connect(server='SQLEXPRESS', user='sa', password='1234',
                      database='adventureworks')


conn.execute_non_query('CREATE TABLE persons(id INT, name VARCHAR(100))')
conn.execute_non_query("INSERT INTO persons VALUES(1, 'John Doe')")
conn.execute_non_query("INSERT INTO persons VALUES(2, 'Jane Doe')")


# how to fetch rows from a table
conn.execute_query('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
for row in conn:
    print "ID=%d, Name=%s" % (row['id'], row['name'])


# examples of other query functions
numemployees = conn.execute_scalar("SELECT COUNT(*) FROM employees")
# note that '%' is not a special character here
numemployees = conn.execute_scalar(
    "SELECT COUNT(*) FROM employees WHERE name LIKE 'J%'")
employeedata = conn.execute_row("SELECT * FROM employees WHERE id=%d", 13)


# how to fetch rows from a stored procedure
# sp_spaceused without arguments returns 2 result sets
conn.execute_query('sp_spaceused')
res1 = [row for row in conn]       # 1st result
res2 = [row for row in conn]       # 2nd result


# how to get an output parameter from a stored procedure
sqlcmd = """
DECLARE @res INT
EXEC usp_mystoredproc @res OUT
SELECT @res
"""
res = conn.execute_scalar(sqlcmd)


# how to get more output parameters from a stored procedure
sqlcmd = """
DECLARE @res1 INT, @res2 TEXT, @res3 DATETIME
EXEC usp_getEmpData %d, %s, @res1 OUT, @res2 OUT, @res3 OUT
SELECT @res1, @res2, @res3
"""
res = conn.execute_row(sqlcmd, (13, 'John Doe'))
conn.close()
