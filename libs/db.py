from mysql.connector import connect


def connect_to_db():  # cnx, cursor (daje nam dwie rzeczy)
    cnx = connect(
        user='root',
        password='coderslab',
        database='communicator_db'
    )
    cursor = cnx.cursor()

    return cnx, cursor  # zwroci nam to dwuelementowa krotke


def close_connection(cnx, cursor):
    cursor.close()
    cnx.close()
