from src.database.my_connector import get_db_connection
from src.database.models import Arm


def get_all_arms():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM arms")
        result = cursor.fetchall()
    connection.close()
    return result


def get_class_arms():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = """
        SELECT
            class.name AS class_name,
            arms.name AS arm_name
        FROM
            class_arms
        JOIN
            class ON class_arms.class_id = class.id
        JOIN
            arms ON class_arms.arms_id = arms.id;
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    connection.close()
    return result


def get_arm_by_id(arm_id: int):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM arms WHERE id=%s", (arm_id,))
        result = cursor.fetchone()
    connection.close()
    return result


def get_arm_id_by_name(arm_name: str):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM arms WHERE name=%s", (arm_name,))
        result = cursor.fetchone()
    connection.close()
    return result


def create_arm(arm: Arm):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO arms (name, damage) VALUES (%s, %s)"
        cursor.execute(sql, (arm.name, arm.damage))
        db_connector.commit()
        result = cursor.lastrowid
    connection.close()
    return result


def update_arm(arm_id: int, arm: Arm):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "UPDATE arms SET name=%s, damage=%s WHERE id=%s"
        cursor.execute(sql, (arm.name, arm.damage, arm_id))
        connection.commit()
    connection.close()


def delete_arm(arm_id: int):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM arms WHERE id=%s", (arm_id,))
        connection.commit()
    connection.close()

