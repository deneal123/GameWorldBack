from src.database.my_connector import get_db_connection
from src.database.models import Tables


def get_all_tables():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
    connection.close()
    return [{'table_name': list(table.values())[0]} for table in tables]


def get_table_data(table_name: str):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        result = cursor.fetchall()
    connection.close()
    return result
