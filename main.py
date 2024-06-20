from fastapi import FastAPI, Query, HTTPException
from src.service import players_service, arms_service, tablesinfo_service, class_services, playerarms_services, query_services
from src.database.models import Player, Arm, Tables, Class, ClassId, ClassArm, PlayerArms, SearchQuery, SearchResult
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/players/", response_model=list[Player])
def get_players():
    return players_service.get_all_players()


@app.get("/players/{players_id}", response_model=Player)
def get_player(player_id: int):
    player = players_service.get_player_by_id(player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.get("/players/nickname/{player_name}", response_model=dict)
def get_player_id_by_name(player_name: str):
    player = players_service.get_player_id_by_name(player_name)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player


@app.post("/players/", response_model=Player)
def create_player(player: Player):
    return players_service.create_player(player)


@app.put("/players/{player_id}", response_model=Player)
def update_player(player_id: int, player: Player):
    return players_service.update_player(player_id, player)


@app.put("/players_arms/{player_id}", response_model=Player)
def update_player_arms(player_id: int, player_arms: PlayerArms):
    return playerarms_services.update_player_arms(player_id, player_arms)


@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    return players_service.delete_player(player_id)


@app.get("/arms/", response_model=list[Arm])
def get_arms():
    return arms_service.get_all_arms()


@app.get("/class_arms/", response_model=list[ClassArm])
def get_class_arms():
    return arms_service.get_class_arms()


@app.get("/arms/{arm_id}", response_model=Arm)
def get_arm(arm_id: int):
    arm = arms_service.get_arm_by_id(arm_id)
    if arm is None:
        raise HTTPException(status_code=404, detail="Arm not found")
    return arm


@app.get("/arms/name/{arm_name}", response_model=dict)
def get_arm_id_by_name(arm_name: str):
    arm = arms_service.get_arm_id_by_name(arm_name)
    if arm is None:
        raise HTTPException(status_code=404, detail="Arm not found")
    return arm


@app.post("/arms/{arm_id}", response_model=Arm)
def create_arm(arm: Arm):
    return arms_service.create_arm(arm)


@app.put("/arms/{arm_id}", response_model=Arm)
def update_arm(arm_id: int, arm: Arm):
    return arms_service.update_arm(arm_id, arm)


@app.delete("/arms/{arms_id}", response_model=Arm)
def delete_arm(arm_id: int):
    return arms_service.delete_arm(arm_id)


@app.get("/tables/", response_model=list[Tables])
def get_tables():
    return tablesinfo_service.get_all_tables()


@app.get("/tables/{table_name}", response_model=list[dict])
def get_table_data(table_name: str):
    data = tablesinfo_service.get_table_data(table_name)
    if not data:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found")
    return data


@app.get("/class/", response_model=list[Class])
def get_all_class():
    return class_services.get_all_class()


@app.get("/class/{name_class}", response_model=ClassId)
def get_id_by_class(name_class: str):
    id_class = class_services.get_id_by_class(name_class)
    if id_class is None:
        raise HTTPException(status_code=404, detail="Class not found")
    return id_class


@app.get("/search/", response_model=list[SearchResult])
async def search(query: str = Query(...)):
    results = await query_services.perform_search_in_database(query)
    return results
