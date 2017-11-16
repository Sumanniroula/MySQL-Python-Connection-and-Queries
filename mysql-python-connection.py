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
db_connection = pymysql.connect(host = 'localhost', #database host
                             user = 'suman', #database username
                             password='99999999', #database password
                             db='shop', #database name
                             )

cur = db_connection.cursor()
