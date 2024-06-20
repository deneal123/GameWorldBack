from src.repository import query_repository
from src.database.models import SearchQuery, SearchResult


async def perform_search_in_database(query: str) -> list[SearchResult]:
    results = []
    players_results = await query_repository.search_players_by_name(query)
    results.extend(players_results)
    arms_results = await query_repository.search_arms_by_name(query)
    results.extend(arms_results)
    return results
