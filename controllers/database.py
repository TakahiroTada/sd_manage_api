from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from bases.token_authorize import check_access_token
from databases.api_token import migrate_database as migrate_api_token
from databases.generate_task import migrate_database as migrate_generate_task

def get_database_router(config):
    database_url = config.connection_string
    engine = create_engine(database_url)
    router = APIRouter()

    @router.post("/database/migrate", dependencies=[Depends(check_access_token)])
    async def migrate_database():
        migrate_api_token(engine)
        migrate_generate_task(engine)
        return True

    return router
