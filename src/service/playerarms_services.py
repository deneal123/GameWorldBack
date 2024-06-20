from src.repository import playerarms_repository
from src.service.players_service import get_player_by_id
from src.database.models import PlayerArms


def update_player_arms(player_id: int, player_arms: PlayerArms):
    player_arm = playerarms_repository.update_player_arms(player_id, player_arms)
    return get_player_by_id(player_id)
