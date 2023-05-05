from fastapi import FastAPI
from configurations.config import load_config
from controllers.generate_task import get_generate_task_router
from controllers.user import get_user_router
from controllers.database import get_database_router

app = FastAPI()

config = load_config()

routers = [
    get_user_router(config),
    get_database_router(config),
    get_generate_task_router(config)
]

for router in routers:
    app.include_router(router)
