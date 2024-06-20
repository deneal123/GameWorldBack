from src.repository import tableinfo_repository
from src.database.models import Tables


def get_all_tables():
    tables = tableinfo_repository.get_all_tables()
    return [Tables(**table) for table in tables]


def get_table_data(table_name: str):
    data = tableinfo_repository.get_table_data(table_name)
    return data if data else None
