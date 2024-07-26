"""
Base de datos de Northwind

La base de datos Northwind es una base de datos de muestra creada originalmente por Microsoft y utilizada como base para sus tutoriales en 
una variedad de productos de bases de datos durante décadas. La base de datos de Northwind contiene datos de ventas de una empresa ficticia 
llamada "Northwind Traders", que importa y exporta alimentos especiales de todo el mundo. La base de datos Northwind es un excelente esquema 
tutorial para un ERP de pequeñas empresas, con clientes, pedidos, inventario, compras, proveedores, envíos, empleados y contabilidad de 
entrada única. Desde entonces, la base de datos Northwind ha sido trasladada a una variedad de bases de datos que no son de Microsoft, 
incluido PostgreSQL.

El conjunto de datos de Northwind incluye datos de muestra para lo siguiente.

Proveedores: Proveedores y vendedores de Northwind
Clientes: Clientes que compran productos de Northwind
Empleados: detalles de los empleados de los comerciantes de Northwind
Productos: Información del producto
Transportistas: los detalles de los transportistas que envían los productos desde los comerciantes a los clientes finales.
Órdenes y detalles del pedido: Transacciones de órdenes de venta que tienen lugar entre los clientes y la empresa.


Base de datos de Chinook

Chinook es una base de datos de muestra disponible para SQL Server, Oracle, MySQL, etc. Se puede crear y ejecutar un único script SQL. La base 
de datos Chinook es una alternativa a la base de datos Northwind, siendo ideal para demostraciones y pruebas de herramientas ORM dirigidas a 
servidores de bases de datos únicos o múltiples.

El modelo de datos Chinook representa una tienda de medios digitales, que incluye tablas para artistas, álbumes, pistas multimedia, facturas 
y clientes.

Los datos relacionados con los medios se crearon utilizando datos reales de una biblioteca de iTunes. La información de clientes y empleados 
se creó manualmente utilizando nombres ficticios, direcciones que se pueden ubicar en mapas de Google y otros datos bien formateados (teléfono, 
fax, correo electrónico, etc.). La información de ventas se genera automáticamente utilizando datos aleatorios durante un período de cuatro 
años.

¿Por qué el nombre Chinook?
El nombre de esta base de datos de ejemplo se basó en la base de datos Northwind. Los chinooks son vientos en el interior oeste de América 
del Norte, donde las praderas canadienses y las grandes llanuras se encuentran con varias cadenas montañosas. Los chinooks son más frecuentes 
en el sur de Alberta y Canadá. Chinook es una buena opción de nombre para una base de datos que pretende ser una alternativa a Northwind.

"""

#Curso SQL completo
#SQL significa "Structured Query Language" (Lenguaje de Consultas Estructuradas). Nos permite trabajar con Bases de Datos relacionales.

#Internamente, funciona con algebra lineal. Con SQL podemos:

#Crear y Admisionar Bases de Datos.
#Consultar datos.
#Modificar y actualizar los datos.
#Agregar restrcciones y reglas de integridad : agregar condiciones para asegurarnos de que los datos cumplen con ciertos criterios.
#Generar informes, análisis de datos, etc...
#Administrar usuarios y permisos.
#Voy a realizar el siguiente curso con consultas de SQL, dentro de Python.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# Creamos una variable a la que se va a asignar el objeto de conexión a la base de datos.
con = sqlite3.connect('company.db')

# Si quisieramos guardarla en la carpeta "DataBase" del escritorio, no olvides la doble barra:
## con = sqlite3.connect('C:\\Users\\Usuario\\Desktop\\DataBase\\company.db')

# Para ejecutar sentencias SQL debemos usar un cursor:
cursor = con.cursor()

# Este cursor cuenta con el método execute, donde podemos poner la sentencia SQL.
# Creamos la primera tabla para esa base de datos:
cursor.execute('''CREATE TABLE IF NOT EXISTS Empleados(id integer primary key,
                   nombre text, departamento text, salario integer)''')

# Cualquier cambio en la base de datos, debe consolidarse con un commit()
con.commit()
# Vamos a insertar valores dentro de la tabla:

cursor.execute('''INSERT INTO Empleados (nombre, departamento, salario)
                VALUES ("Neoma", "Ventas", 1000), ("Maria", "Ventas", 1100),
                ("Yesika", "Publicidad", 900), ("Fabiola", "800", 800), ("Julian", "Publicidad", 1000)''')
con.commit()
# Veamos la tabla completa con los datos:

# Ejemplo de ejecución de una sentencia SQL
query = 'SELECT * FROM Empleados'

tabla = pd.read_sql(query, con)
print(tabla)

def mostrar_todo():
    cursor.execute('SELECT * FROM Empleados')
    print(cursor.fetchall())
    
mostrar_todo()
# Nos devuelve una lista de tuplas, una por registro (fila).

# Para que muestre sólo unos pocos registros, utilizamos fetchmany(número de registros)
def mostrar_todo():
    cursor.execute('SELECT * FROM Empleados')
    print(cursor.fetchmany(3))
    
mostrar_todo()

#En la tabla tenemos el campo Departamento en el registro de Fabiola erroneo. Debería ser Publicidad, no 800. Para esto utilizamos la siguiente sentencia:

#UPDATE nombre_tabla SET campo_actualizar = new_valor WHERE condición

def actualizar(ident, new_valor):
    cursor.execute(f'''UPDATE Empleados SET departamento = '{new_valor}' WHERE id = '{ident}' ''')
    con.commit()

actualizar(4, "Ventas")

# Comprobamos que ahora está correcto:
query = 'SELECT * FROM Empleados'

tabla = pd.read_sql(query, con)
print(tabla)

# Para eliminar un registro de una tabla SQL tenemos la sentencia:
## SELECT FROM nombre_tabla WHERE condición

def eliminar_registro(ident):
    cursor.execute(f'''DELETE FROM Empleados WHERE id = '{ident}' ''')
    con.commit()

eliminar_registro(2)
query = 'SELECT * FROM Empleados'
tabla = pd.read_sql(query, con)
print(tabla)

#Cerrando conexión y cursor¶
#Cuando establecemos una conexión, abrimos una base de datos. Lo que tenemos que hacer al terminar es cerrar la conexión de la base de datos con:

con.close()

#También podemos cerrar el cursor y crear uno nuevo cuando vayamos a ejecutar una nueva sentencia SQL mediante:

#cursor.close()

#De cualquier manera, deberíamos terminar nuestra sesión de trabajo cerrando la base de datos.

con.close()

#Para continuar con las consultas de SQL, vamos a utilizar la Base de Datos Northwind, que podemos obtener en la web:

#Northwind (https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite)

#El primer paso es importar las librerías y crear el acceso a la base de datos. Voy a poner también el acceso a la Base de Datos Chinook para 
# dejarla preparada para cuando la necesitemos.

# Creamos una DataBase donde poner nuestra tabla:
pathNorthwind = "Northwind.db"
pathChinook = "Chinook.db"
Northwind = pathNorthwind
Chinook = pathChinook

# Creamos la conexión con la BD y listaremos las tablas con las que contamos
conC = sqlite3.connect(Chinook)
conN = sqlite3.connect(Northwind)

# Listar las tablas de cada DataBase:
tablesC = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conC)

tablesN = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table';""", conN)
# Tablas en la Base de Datos Chinook
tablesC

# Tablas en la Base de Datos Northwind
tablesN

# Cambiar el nombre de una columna con AS
query = '''SELECT LastName AS apellido, FirstName AS nombre
        FROM Employees'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Multiplicar los valores de una columna por 2
query = '''SELECT Price, Price*2 AS precio_doble
        FROM Products'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Suma de todos los precios de la columna Price
query = '''SELECT SUM(Price) AS suma_precios
        FROM Products'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Ordenar las filas por el precio de forma ascendente

query = '''SELECT *
        FROM Products
        ORDER BY Price ASC'''

# Para orden descendente tenemos DESC
# Si hubiera registros NULL, estos son los que "menos valen"
consulta = pd.read_sql(query, conN)
print(consulta)

# Si hubieran muchos registros nulos, y queremos que se muestren al final:

query = '''SELECT *
        FROM Products
        ORDER BY ProductName ASC NULLS LAST'''

# Para poner los nulos al principio en orden descendente tenemos:
## ORDER BY ProductName DESC NULLS FIRST

consulta = pd.read_sql(query, conN)
print(consulta)

# Para realizar una búsqueda y que se ordene de forma aleatoria:
query = '''SELECT * FROM Products
        ORDER BY RANDOM()'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Ordenar por dos campos:
query = '''SELECT * FROM Products
        ORDER BY ProductName, SupplierID DESC'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Si hay valores repetidos, y quiero ver los que hay sin repetición:

query = '''SELECT DISTINCT ProductName
        FROM Products
        ORDER BY ProductName ASC'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Clausula WHERE (condiciones)
query = '''SELECT ProductName
        FROM Products
        WHERE ProductID = 14'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Recuerda que para utilizarlo con string, hay que ponerlo entre comillas
query = '''SELECT *
        FROM Products
        WHERE ProductName = "Tofu" '''

consulta = pd.read_sql(query, conN)
print(consulta)

# Productos con precio igual o menos a 40
query = '''SELECT *
        FROM Products
        WHERE Price <= 40
        ORDER BY Price DESC'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Operadores lógicos AND, OR y NOT¶
#Utilizamos "and" y "or" para aplicar varias condiciones.

query = '''SELECT *
        FROM Customers
        WHERE CustomerID >= 50 AND CustomerID < 55'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Con la clausula OR muestra todos los registros que cumplen alguna de las condiciones, primero una y luego la otra.

query = '''SELECT *
        FROM Employees
        WHERE FirstName = "Nancy" OR FirstName = "Anne" '''

consulta = pd.read_sql(query, conN)
print(consulta)

#Para agrupar condiciones utilizamos parentesis. Ejemplo: quiero la lista de productos, donde el precio sea menor a 20 o que la categoría sea 6 
# (aunque cueste más), pero sea de una condición o de la otra, el proveedor (supplier) tiene que ser el 7:

query = '''SELECT *
        FROM Products
        WHERE (Price<20 OR CategoryID=6) AND SupplierID=7'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Con la clausula NOT filtramos los productos que no cumplen alguna condición.

query = '''SELECT * FROM Products WHERE NOT Price>40'''

#Esta consulta no tendría mucho sentido ya que es lo mismo que WHERE Price<=40. Veamoslo entonces con la siguiente consulta: filtrar todos los 
# registros de USA y de France (que no se muestren estos)

query = '''SELECT *
        FROM Customers
        WHERE NOT Country="USA" AND NOT Country="France" '''

consulta = pd.read_sql(query, conN)
print(consulta)

# Mostrar los 5 primeros registros que cumplan las condiciones:
## Customer>=50 y que no sean de Alemania

query = '''SELECT *
        FROM Customers
        WHERE CustomerID >= 50
        AND NOT Country = "Germany"
        LIMIT 5'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Buscar 3 opciones aleatorias, que tengan Categoría 6, que no tengan al proveedor 1, y que el precio sea menor o igual a 30.

query = '''SELECT *
        FROM Products
        WHERE NOT CategoryID = 6
        AND NOT SupplierID = 1 AND Price <= 30
        ORDER BY RANDOM()
        LIMIT 3'''

consulta = pd.read_sql(query, conN)
print(consulta)

#DISTINCT vs NOT
#El operador "distinto de" es !=

#Es un operador de comparación, no lógico. Los operadores lógicos son los Booleanos. Ejm:

#SELECT * FROM Customers WHERE NOT TRUE

#No devolvería nada porque es FALSE.

#Operador BETWEEN
#Es un operador de comparación, que se utiliza para seleccionar valores en un rango específico.

# Productos con precios entre 20 y 30
query = '''SELECT *
        FROM Products
        WHERE Price BETWEEN 20 AND 30'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Listado de empleados nacidos entre 1960 y 1970:
query = '''SELECT *
        FROM Employees
        WHERE BirthDate BETWEEN "1960-0-1"
        AND "1970-0-1" '''

consulta = pd.read_sql(query, conN)
print(consulta)

#Recordar que BETWEEN incluye los dos rangos buscados, y que el primer valor tiene que ser menor que el segundo, no puedo poner:

#WHERE EmploeeID BETWEEN 6 AND 3

#En SQL el Booleano TRUE es equivalente a 1, y el FALSE es equivalente a 0, de forma que:

#WHERE 1 es equivalente a WHERE TRUE

#Operador LIKE
#Es un operador de comparación, que se utiliza para buscar y filtrar, en función de ciertos patrones de cadenas de texto.

#Permite realizar búsquedas de texto parcial, utilizando los llamados "comodines". Son dos: % y _

#a) Con % indicamos que puede haber algo antes:

#WHERE LastName LIKE "%uller"

#Le indico como termina, pero no como empieza. No diferencia entre mayúsculas y minúsculas.

#b) Con _ le indicamos "cualquer cosa", un guión bajo por cada caracter:

#WHERE LastName LIKE "F____r"

#Operador IS NULL o IS NOT NULL
query = '''SELECT *
        FROM Products
        WHERE ProductName IS NOT NULL
        ORDER BY ProductName ASC
        LIMIT 3'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Operador IN
#Se utiliza como una abreviación del operador OR

query = '''SELECT *
        FROM Products
        WHERE SupplierID IN (3,4,5,6)'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Simplemente le pasamos una tupla para que vea si nuestro resultado está en alguno de esos valores.

#Se puede utilizar en la clausula SELECT, UPDATE y en DELETE.

#Para verlo con caracteres utilizamos comillas:

#WHERE LastName IN ("Fuller", "King")

#También podemos utilizarlo con NOT:

#WHERE SupplierID NOT IN (3,4,5)

#Podemos utilizar IN para hacer una subconsulta, que es una consulta dentro de otra consulta.

#Funciones de Agregación
#Nos permiten agrupar datos, resumirlos, o trabajar con estadísticas de los datos. Se utilizan con la clausula SELECT con el formato: SELECT 
# funcion()

#Cuando usamos una función de agregación, nos va a crear un nuevo campo, que muestre el resultado de esta función. Tipos:

# COUNT -> contar cuantos registros hay en un campo:
query = '''SELECT COUNT (FirstName)
        FROM Employees'''

consulta = pd.read_sql(query, conN)
print(consulta)

# SUM -> sumar los valores de un campo:
query = '''SELECT SUM(Price) AS Sumatorio
        FROM Products'''

consulta = pd.read_sql(query, conN)
print(consulta)

# AVG -> promedio
query = '''SELECT AVG(Price) AS Media
        FROM Products'''

consulta = pd.read_sql(query, conN)
print(consulta)

# ROUND -> Redondear un valor. Si ponemos dos argunmentos separados por coma,
# el segundo indica el número de decimales que queremos.
# Redondea a la alza.
query = '''SELECT ROUND(AVG(Price),2)
        FROM Products'''

consulta = pd.read_sql(query, conN)
print(consulta)

# MIN y MAX -> para ver el registro de menor o mayor valor
query = '''SELECT ProductName, MIN(Price)
        FROM Products
        WHERE ProductName IS NOT NULL'''

consulta = pd.read_sql(query, conN)
print(consulta)

#GROUP BY y HAVING¶
#La clausula GROUP BY se utiliza para agrupar uno o varios registros, según uno o varios valores de las columnas (campos)Group by.jpg

# Media de los precios de los productos que vende cada proveedor,
# ordenados por ese promedio

query = '''SELECT SupplierID, AVG(Price) AS Promedio
        FROM Products
        GROUP BY SupplierID
        ORDER BY Promedio DESC
        LIMIT 10'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Si quiero una condición, SIEMPRE antes que agrupación
query = '''SELECT CategoryID, AVG(Price)
        FROM Products
        WHERE ProductName IS NOT NULL
        GROUP BY CategoryID'''

consulta = pd.read_sql(query, conN)
print(consulta)

#La clausula WHERE nos filtra los resultados mostrados, los cuales podemos agrupar, por eso va antes.

#Para filtrar los resultados agrupados tenemos la clausula HAVING

query = '''SELECT SupplierID, AVG(Price) AS Promedio
        FROM Products
        GROUP BY SupplierID
        HAVING promedio > 40'''

consulta = pd.read_sql(query, conN)
print(consulta)

# Los 5 productos que menos se venden,
# de los que venden más de 50:
query = '''SELECT ProductID, SUM(Quantity) AS Cantidad
        FROM OrderDetails
        GROUP BY ProductID
        HAVING Cantidad > 50
        LIMIT 5'''

consulta = pd.read_sql(query, conN)
print(consulta)

#No podemos agregarle una función de agregación a otra función de agregación. No puedo:

#GROUP BY ProductID HAVING MAX(Cantidad)

#Resulta que "Cantidad" es el resultado de una función de agregación.

#Orden de las clausulas: SELECT ... FROM, WHERE, GROUP BY, HAVING, ORDER BY, y por último LIMIT.

#Subconsultas (SUBQUERIES)
#Es una consulta que está dentro de otra consulta. Se ejecuta primero una consulta, cuyos resultados se van a utilizar para realizar otra 
# consulta. La subconsulta sólamente recupera datos.

#La suconsulta tiene que ser un SELECT, no puede ser algo que modifique la base de datos.

#Pero la subconsulta si puede estar en WHERE, la utilizamos como una condición.

#Vamos a utilizar una subconsulta para comparar el ProductID de la tabla OrderDetails (que aquí llamaremos pID), con el ProductID de la 
# tabla Products:

query = '''SELECT ProductID AS pID, Quantity, (SELECT ProductName FROM Products WHERE pID = ProductID) AS Nombre FROM OrderDetails'''

#Esta consulta tiene 2 grandes errores:

#1) En la subconsulta tengo que decirle de donde viene pID, es decir, se pone en su lugar: OrderDetails.pID

#2) Pero, no podemos utilizar un alias dentro de una subconsulta, por lo tanto hay que poner: OrderDetails.ProductID

#De esta forma hacemos referencia a datos de otra tabla.

#IMPORTANTE: Cada subconsulta devuelve una sola columna.

#Ejemplo: queremos el ProductID, el total de vendidos de ese producto, su nombre, su precio, y el total de su venta:

query = '''SELECT ProductID, SUM(Quantity) AS Total_Vendidos,
            (SELECT ProductName FROM Products
            WHERE OrderDetails.ProductID = ProductID) AS Nombre,
            (SELECT Price FROM Products
            WHERE ProductID = OrderDetails.ProductID
            GROUP BY ProductID) AS Precio,
            SUM(Quantity)*(SELECT Price FROM Products
            WHERE ProductID = OrderDetails.ProductID
            GROUP BY ProductID) AS Venta_Total
        FROM OrderDetails
        GROUP BY ProductID
        ORDER BY ProductID'''

consulta = pd.read_sql(query, conN)
print(consulta)

#Cuando hago consultas y subconsultas, a la tabla principal (la de fuera de la subconsulta) si puedo ponerle un alias que utilizar dentro de 
# la subconsulta:

#FROM OrderDetails AS OD

#Podemos meter una subconsulta dentro de otra subconsulta, ya que no nos permite utilizar para buscar:

#(SELECT SupplierName FROM Suppliers

#WHERE SupplierID = (SELECT SupplierID FROM Products

#WHERE ProductID = OrderDetails.ProductID)) AS Vendedor

#Podemos tomar la subconsulta que hemos llamado "Precio", eliminarla, y añadir después del FROM principal la línea WHERE "(subconsulta precio)>40".

#Tenemos Dos formas de dar alias a una tabla principal:

#1) FROM OrderDetails AS OD

#2) FROM [OrderDetails] OD

#Subconsultas en FROM: Lo que ponemos en FROM es una tabla, aquella de la que se van a sacar los datos, por lo que esta tabla puede estar 
# compuesta de varias subconsultas -> Cada subconsulta es una columna:
#SELECT Nombre, Venta_Total, Vendedor

#FROM (Subconsultas con su SELECT, FROM, WHERE, GROUP BY, etc...)

# Nombre, apellido y unidades_vendidas por cada vendedor
query = '''SELECT FirstName, LastName,
            (SELECT SUM(od.Quantity)
            FROM [Orders] o, [OrderDetails] od
            WHERE o.EmployeeID = e.EmployeeID
            AND od.OrderID = o.OrderID) AS unidades_vendidas
        FROM [Employees] e'''

consulta = pd.read_sql(query, conN)
print(consulta)

#JOINS
#Son una operación que utilizamos para poder combinar la información de 2 o más tablas, pero que esa información se devuelva en una sola tabla.

#Los JOIN principales son 4, más otro especial:

#1) INNER JOIN: los más comunes.

#2) LEFT JOIN

#3) RIGHT JOIN

#4) FULL JOIN, y los

#5) CROSS JOIN

#INNER JOIN nos devuelve la coincidencia entre ambas tablas. Podemos hacerlo de forma implicita o explicita:

#a) Implicita: sin utilizar la palabra JOIN

#SELECT * FROM [Employees] e, [Orders] o

#WHERE e.EmployeeID = o.EmployeeID

#CROSS JOIN nos devuelve todos los campos de ambas tablas multiplicadas, es decir, son equivalentes a:

#SELECT * FROM [Employees] e, [Orders] o

#Es exactamente igual a escribir:

#SELECT * FROM [Employees] e CROSS JOIN [Orders] o

#b) Para hacer un INNER JOIN explicito, en lugar de WHERE utilizamos ON para indicar la condición:

#SELECT * FROM Employees e

#INNER JOIN Orders o ON e.EmployeeID = EmployeeID

#En el caso explicito, podemos seleccionar que columnas queremos en lugar del asterísco tras el SELECT.

# Creamos una nueva base de datos que podamos modificar en Kaggle:
con = sqlite3.connect('NorthwindBD.db')

# Y con el método backup para copiamos dentro el contenido
with con:
    conN.backup(con)
# Crear una tabla:
# Primero tenemos que crear un cursor para esta DataBase:
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Rewards(RewardID integer primary key,
    EmployeeID integer, Reward integer, Month text)''')

# Ahora introducimos valores en esa tabla

cur.execute('''INSERT INTO Rewards (EmployeeID, Reward, Month)
            VALUES (3,200,"January"), (2,180,"February"),
            (5,250,"March"), (1,280,"April"),
            (8,160,"May"), (NULL, NULL, "June")''')

# Para consolidar los datos necesitamos hacer un commit:
con.commit()

# Y comprobamos que la tabla esté correcta:
query = '''SELECT * FROM Rewards'''

consulta = pd.read_sql(query, con)
print(consulta)

# Realicemos un JOIN entre Employees y Rewards
query = '''SELECT * FROM Employees e
        JOIN Rewards r ON e.EmployeeID = r.EmployeeID'''

consulta = pd.read_sql(query, con)
print(consulta)

#Nos muestra toda la información de aquellos empleados que tuvieron una recompensa (reward)

#LEFT JOIN nos devuelve la tabla A y parte de la información de B (los coindidentes)
#En nuestro ejemplo, si un empleado tiene recompensas se las pone al lado, sino lo rellenaría con NULL.

#SELECT * FROM Employees e
#LEFT JOIN Rewards r ON e.EmployeeID = r.EmployeeID

#Aquí nos devuelve a todos los empleados (tabla A) con las recompensas (tabla B), en quienes las tienen.

#RIGHT JOIN nos devuelve toda la tabla B (recompensas), y si hay algún empleado asociado (tabla A) lo añade.
#Puesto que no permite hacer un RIGHT JOIN, lo que hacemos simplemente es invertir las tablas. NOTA: si quiero que muestre justo el campo 
# utilizado para comparar, necesito decirle que lo tome de una de las dos tablas.

#SELECT r.EmployeeID, Reward, Month FROM Rewards r
#LEFT JOIN Employees e ON e.EmployeeID = r.EmployeeID

#FULL JOIN: puesto que SQL tampoco permite el FULL, tenemos que simularlo, utilizaremos UNION.
#Lo que hacemos es poner la consulta LEFT, un espacio, la palabra UNION, y la "consulta RIGHT", que es cambiando de lugar las dos tablas.

query = '''SELECT * FROM Employees e
    LEFT JOIN Reward r ON
    UNION
    SELECT * FROM Rewards r
    LEFT JOIN Employees e ON... '''
# Encuentra los 10 productos con mayor rentabilidad o ganancia (Revenue)
query = '''SELECT ProductName, SUM(Price*Quantity) AS Revenue
        FROM OrderDetails od
        JOIN Products p ON p.ProductID = od.ProductID
        GROUP BY od.ProductID
        ORDER BY Revenue DESC
        LIMIT 10'''

consulta = pd.read_sql(query, con)
print(consulta)


# Creamos un plot de barras (Kind) con tamaño (figsize) 10 y 5
consulta.plot(x="ProductName", y="Revenue", kind="bar",
             figsize=(10,5), legend=False, color = "fuchsia", edgecolor = "white")
# Configuramos el título del gráfico
plt.title("10 productos más rentables\n", fontsize = '16', fontweight = 'bold')
# Nombramos al eje X y al Y
plt.xlabel("Productos\n")
plt.ylabel("Ganancia\n")
# Nos aseguramos que los nombres del eje x estén a 45 grados
plt.xticks(rotation=45)
# Por último pedimos que muestre el gráfico
plt.show()

# Encuentra los 10 empleados más efectivos
query = '''SELECT (FirstName|| " " || LastName) AS Empleado,
            COUNT(*) AS Total
        FROM Orders o
        JOIN Employees e ON e.EmployeeID = o.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY Total DESC'''

consulta = pd.read_sql(query, con)
print(consulta)

# Creamos un plot de barras (Kind) con tamaño (figsize) 10 y 5
consulta.plot(x="Empleado", y="Total", kind="bar",
             figsize=(10,5), legend=False, color = "cyan", edgecolor = "blue")
# Configuramos el título del gráfico
plt.title("Empleados más efectivos\n", fontsize = '16', fontweight = 'bold')
# Nombramos al eje X y al Y
plt.xlabel("Empleados\n")
plt.ylabel("Total_Vendido\n")
# Nos aseguramos que los nombres del eje x estén a 45 grados
plt.xticks(rotation=45)
# Por último pedimos que muestre el gráfico
plt.show()

print(conN.close())
print(conC.close())
print(con.close())
