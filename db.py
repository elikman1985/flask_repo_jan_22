import os
import sqlite3


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'example_2.sqlite3')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    records = cursor.fetchall()
    return records
