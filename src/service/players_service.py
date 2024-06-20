from src.repository import players_repository
from src.database.models import Player


def get_all_players():
    players = players_repository.get_all_players()
    return [Player(**player) for player in players]


def get_player_by_id(player_id: int):
    player = players_repository.get_player_by_id(player_id)
    return Player(**player) if player else None


def get_player_id_by_name(player_name: str):
    player_id = players_repository.get_player_id_by_name(player_name)
    return player_id if player_id else None


def create_player(player: Player):
    player_id = players_repository.create_player(player)
    return get_player_by_id(player_id)


def update_player(player_id: int, player: Player):
    players_repository.update_player(player_id, player)
    return get_player_by_id(player_id)


def delete_player(player_id: int):
    players_repository.delete_player(player_id)
    return {"message": "Player deleted successfully"}