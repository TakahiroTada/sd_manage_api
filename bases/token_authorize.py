from fastapi import FastAPI, Depends, HTTPException, Header
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI()

# 固定のアクセストークン
ACCESS_TOKEN = "chinpocolin"

# 認証を行う関数
async def check_access_token(token: str = Header(None)):
    if token != ACCESS_TOKEN:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Invalid access token")
    return token

# @app.get("/private_endpoint", dependencies=[Depends(check_access_token)])
# async def private_endpoint():
#     return {"message": "You have access to this private endpoint"}
