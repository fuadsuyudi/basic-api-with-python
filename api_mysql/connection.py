import MySQLdb

def connect():
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="api_mysql")
    cursor = db.cursor()

    return cursor, db