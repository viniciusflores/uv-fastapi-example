from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/hello")
async def root():
    return {"message": "Hello World!"}

@app.post("/hello-user")
async def root(name: str):
    return {"message": f"Hello {name}"}

@app.post("/hello-user/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}

@app.put("/hello-user/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}

@app.delete("/hello-user/{name}")
async def root(name: str):
    return {"message": f"Hello {name}"}
