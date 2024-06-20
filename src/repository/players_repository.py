from src.database.my_connector import get_db_connection
from src.database.models import Player


def get_all_players():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players")
        result = cursor.fetchall()
    connection.close()
    return result


def get_player_by_id(player_id: int):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM players WHERE id=%s", (player_id,))
        result = cursor.fetchone()
    connection.close()
    return result


def get_player_id_by_name(player_name: str):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM players WHERE nickname=%s", (player_name,))
        result = cursor.fetchone()
    connection.close()
    return result


def create_player(player: Player):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO players (nickname, data_registration, class_id) VALUES (%s, %s, %s)"
        cursor.execute(sql, (player.nickname, player.data_registration, player.class_id))
        connection.commit()
        result = cursor.lastrowid
    connection.close()
    return result


def update_player(player_id: int, player: Player):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE players SET nickname=%s, data_registration=%s, class_id=%s WHERE id=%s"
        cursor.execute(sql, (player.nickname, player.data_registration, player.class_id, player_id))
        connection.commit()
    connection.close()


def delete_player(player_id: int):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM players WHERE id=%s", (player_id,))
        connection.commit()
    connection.close()

