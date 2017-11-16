"""I assume that you have created a database and table yourself:
   mysql> CREATE DATABASE shop;
   mysql> CREATE TABLE customers(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
          firstname VARCHAR(30),
          lastname VARCHAR(30),
          email VARCHAR(30));
   mysql> CREATE TABLE orders(orderid INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
          ordername VARCHAR(30),
          id INT(6) UNSIGNED,
          FOREIGN KEY (id) REFERENCES customers(id));
"""
# Install pymysql package and import it
import pymysql
import pymysql.cursors

#making a database connection
#making a database connection
db_connection = pymysql.connect(host = 'localhost', #database host
                             user = 'suman', #database username
                             password='99999999', #database password
                             db='shop', #database name
                             )

cur = db_connection.cursor()

#Insreting values to table customers
sql = "INSERT INTO customers (firstname, lastname, email) VALUES (%s, %s, %s)"
cur.execute(sql, ('suman', 'niroula', 'sum'))
cur.execute(sql,('sumji', 'niro', 'email'))
cur.execute(sql,('sumane', 'nir', 'ji'))
db_connection.commit()

#Inserting values to table orders
sql = "INSERT INTO orders (ordername) VALUES (%s)"
cur.execute(sql, ('book',))
cur.execute(sql,('suman',))
cur.execute(sql,('sumane',))
db_connection.commit()

#delete all values from customers and orders table
delete_cus = "DELETE FROM customers"
delete_ord = "DELETE FROM orders"
cur.execute(delete_cus)
cur.execute(delete_ord)
db_connection.commit()

#Insreting values to table customers
sql = "INSERT INTO customers (firstname, lastname, email) VALUES (%s, %s, %s)"
cur.execute(sql, ('suman', 'niroula', 'sum'))
cur.execute(sql,('sumji', 'niro', 'email'))
cur.execute(sql,('sumane', 'nir', 'ji'))
db_connection.commit()

#Inserting values to table orders
sql = "INSERT INTO orders (ordername) VALUES (%s)"
cur.execute(sql, ('book',))
cur.execute(sql,('suman',))
cur.execute(sql,('sumane',))
db_connection.commit()

#Selecting the rows whose email is 'sum'
"""sql3 = "SELECT * FROM customers WHERE email = %s"
cur.execute(sql3,('sum',))
result = cur.fetchall()
"""
#selecting all values
result = "SELECT * FROM customers"
cur.execute(result)
final = cur.fetchall()

#printing result after fetching
for i in final:
    print i