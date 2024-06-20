from pydantic import BaseModel, StrictBool, StrictStr, StrictFloat, PositiveInt, NonNegativeInt
from typing import Optional, Dict
from datetime import datetime


class Player(BaseModel):
    id: Optional[int]
    nickname: StrictStr
    data_registration: datetime
    class_id: Optional[int]


class Arm(BaseModel):
    id: Optional[int]
    name: StrictStr
    damage: StrictFloat


class ClassArm(BaseModel):
    class_name: str
    arm_name: str


class Class(BaseModel):
    id: Optional[int]
    name: StrictStr
    status: NonNegativeInt


class ClassId(BaseModel):
    id: PositiveInt


class ClassArms(BaseModel):
    id: Optional[int]
    class_id: PositiveInt
    arms_id: PositiveInt


class PlayerArms(BaseModel):
    id: Optional[int]
    player_id: PositiveInt
    arms_id: PositiveInt


class Tables(BaseModel):
    table_name: StrictStr


class SearchQuery(BaseModel):
    query: str


class SearchResult(BaseModel):
    id: int
    name: str
    description: str


