from src.database.my_connector import get_db_connection
from src.database.models import Class, ClassId


def get_all_class():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM class")
        result = cursor.fetchall()
    connection.close()
    return result


def get_id_by_class(name_class: str):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM class WHERE name=%s", (name_class,))
        result = cursor.fetchone()
    connection.close()
    return result
