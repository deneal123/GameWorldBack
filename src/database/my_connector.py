import pymysql


def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='game_world',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
