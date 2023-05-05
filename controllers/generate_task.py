from fastapi import APIRouter, Depends
from bases.token_authorize import check_access_token
from logics.generate_task import fetch_generate_tasks
from sqlalchemy import create_engine
from pydantic import BaseModel

class GenerateTaskModel(BaseModel):
    user_id: int
    title: str
    status: int
    prompt: str
    negative_prompt: str
    model_name: str
 
def get_generate_task_router(config):
    database_url = config.connection_string
    engine = create_engine(database_url)

    router = APIRouter()

    @router.get("/generate_tasks/", dependencies=[Depends(check_access_token)])
    async def get_genetate_tasks():
        # TODO 処理を実装する
        return fetch_generate_tasks(engine)

    @router.get("/generate_tasks/next", dependencies=[Depends(check_access_token)])
    async def get_next_genetate_tasks(id: int):
        # TODO 処理を実装する
        return False
    
    @router.get("/generate_tasks/{id}", dependencies=[Depends(check_access_token)])
    async def get_genetate_task_detail(id: int):
        # TODO 処理を実装する
        return False
    
    @router.post("/generate_tasks/{id}", dependencies=[Depends(check_access_token)])
    async def update_genetate_task(id: int):
        # TODO 処理を実装する
        return False
    
    @router.put("/generate_tasks/{id}", dependencies=[Depends(check_access_token)])
    async def add_genetate_task(id: int, generate_task: GenerateTaskModel):
        # TODO 処理を実装する
        return {"item_name": generate_task.title, "item_description": generate_task.prompt}
    
    @router.delete("/generate_tasks/{id}", dependencies=[Depends(check_access_token)])
    async def drop_genetate_task(id: int):
        # TODO 処理を実装する
        return False
    
    @router.post("/generate_tasks/{id}/start", dependencies=[Depends(check_access_token)])
    async def start_genetate_task(id: int):
        # TODO 処理を実装する
        return {"task_id": id}

    return router
