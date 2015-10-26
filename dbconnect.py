import MySQLdb

# mysql --user=root -p
def connection():
    conn = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="pythonprogramming") # name of the data base
    c = conn.cursor()

    return c, conn
