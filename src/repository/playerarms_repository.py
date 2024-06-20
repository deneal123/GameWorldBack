from src.database.my_connector import get_db_connection
from src.database.models import PlayerArms


def update_player_arms(player_id: int, player_arms: PlayerArms):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE players_arms SET arms_id=%s WHERE id=%s"
        cursor.execute(sql, (player_arms.arms_id, player_id))
        connection.commit()
    connection.close()
