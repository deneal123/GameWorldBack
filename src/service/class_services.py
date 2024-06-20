from src.repository import class_repository
from src.database.models import Class, ClassId


def get_all_class():
    classes = class_repository.get_all_class()
    return [Class(**class_) for class_ in classes]


def get_id_by_class(name_class: str):
    id_class = class_repository.get_id_by_class(name_class)
    return id_class if id_class else None
