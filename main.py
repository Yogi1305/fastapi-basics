from fastapi import FastAPI
from routes import user,post
app = FastAPI()

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}

app.include_router(user.router,prefix="/users")
app.include_router(post.router, prefix="/posts")

