import psycopg2
import sys

host = 'localhost'
user = 'iti'
password = '123'
dbname = 'iti'

def connect():
    try:
        connection = psycopg2.connect(
            database=dbname,
            user=user,
            password=password,
            host=host
        )
        return connection
    except Exception as error:
        print(f"Error connecting to PostgreSQL database: {error}")


def insert_track(id, name):
    connection = connect()
    cursor = connection.cursor()

    try:
        query = "INSERT INTO track (id, name) VALUES (%s, %s) RETURNING id;"
        cursor.execute(query, (id, name))
        trackid = cursor.fetchone()[0]
        connection.commit()
        print(f"Track with ID {trackid} inserted.")
    except Exception as e:
        print(f"An error occurred: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


# e.g:

insert_track(1, 'Python')


def insert(id, name, track_id):
    connection = connect()
    cursor = connection.cursor()
    try:
        query = "INSERT INTO trainee (id, name, track_id) VALUES (%s, %s, %s) RETURNING id;"
        cursor.execute(query, (id, name, track_id))
        traineeid = cursor.fetchone()[0]
        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def select():
    connection = connect()
    cursor = connection.cursor()

    try:
        query = "SELECT * FROM trainee;"
        cursor.execute(query)
        trainees = cursor.fetchall()
        for trainee in trainees:
            print(trainee)
    except Exception as error:
        print(f"Error reading employees: {error}")
    finally:
        cursor.close()
        connection.close()


def update(id, name, track_id):
    connection = connect()
    cursor = connection.cursor()
    try:
        query = """UPDATE trainee SET name = %s, track_id = %s WHERE id = %s;"""
        cursor.execute(query, (name, track_id, id))
        connection.commit()
        print(f"Trainee with ID {id} updated.")
    except Exception as error:
        print(f"Error updating Trainee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def delete(id):
    connection = connect()
    cursor = connection.cursor()

    try:
        query = "DELETE FROM trainee WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()
        print(f"Trainee with ID {id} deleted.")
    except Exception as error:
        print(f"Error deleting trainee: {error}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

