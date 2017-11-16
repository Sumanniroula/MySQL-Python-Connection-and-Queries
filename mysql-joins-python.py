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

#sql inner join on orders.ordername=customers.firstname
sql_inner_join = "SELECT orders.orderid, customers.firstname, orders.ordername FROM orders INNER JOIN customers ON orders.ordername=customers.firstname"
cur.execute(sql_inner_join)
get_result = cur.fetchall()
print get_result

#sql left outer join on orders.ordername=customers.firstname
sql_left_join = "SELECT customers.id, customers.firstname, orders.ordername FROM customers LEFT JOIN orders ON customers.firstname = orders.ordername ORDER BY customers.firstname"
cur.execute(sql_left_join)
get_left_result = cur.fetchall()
print get_left_result

#sql right join on orders.ordername=customers.firstname
sql_right_join = "SELECT customers.id, customers.firstname, orders.ordername FROM orders RIGHT JOIN customers ON customers.firstname = orders.ordername ORDER BY customers.firstname"
cur.execute(sql_right_join)
get_right_result = cur.fetchall()
print get_right_result