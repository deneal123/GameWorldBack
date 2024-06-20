from src.repository import arms_repository
from src.database.models import Arm, ClassArm


def get_all_arms():
    arms = arms_repository.get_all_arms()
    return [Arm(**arm) for arm in arms]


def get_class_arms():
    arms = arms_repository.get_class_arms()
    return [ClassArm(**arm) for arm in arms]


def get_arm_by_id(arm_id: int):
    arm = arms_repository.get_arm_by_id(arm_id)
    return Arm(**arm) if arm else None


def get_arm_id_by_name(arm_name: str):
    arm = arms_repository.get_arm_id_by_name(arm_name)
    return arm if arm else None


def create_arm(arm: Arm):
    arm_id = arms_repository.create_arm(arm)
    return get_arm_by_id(arm_id)


def update_arm(arm_id: int, arm: Arm):
    arms_repository.update_arm(arm_id, arm)
    return get_arm_by_id(arm_id)


def delete_arm(arm_id: int):
    arms_repository.delete_arm(arm_id)
    return {"message": "Arm deleted successfully"}