from src.database.my_connector import get_db_connection
from src.database.models import SearchQuery, SearchResult


async def search_players_by_name(query: str) -> list[SearchResult]:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, nickname, data_registration, class_id FROM players WHERE nickname LIKE %s"
            cursor.execute(sql, (f"%{query}%",))
            result = cursor.fetchall()
            return [SearchResult(id=row['id'], name=row['nickname'], description=f"Class ID: {row['class_id']}") for row in result]
    finally:
        connection.close()


async def search_arms_by_name(query: str) -> list[SearchResult]:
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, name, damage FROM arms WHERE name LIKE %s"
            cursor.execute(sql, (f"%{query}%",))
            result = cursor.fetchall()
            return [SearchResult(id=row['id'], name=row['name'], description=f"Damage: {row['damage']}") for row in result]
    finally:
        connection.close()
