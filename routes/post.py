from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Post(BaseModel):
    id: int
    title: str
    content: str
    author: str

posts = []  # renamed to avoid name conflict

# Create a new post
@router.post("/")
async def create_post(post: Post):
    posts.append(post)
    return {"posts": posts}

# Get all posts
@router.get("/")
async def get_posts():
    return {"posts by fetching": posts}

# Delete a post by index
@router.delete("/{post_id}")
async def delete_post(post_id: int):
    if 0 <= post_id < len(posts):
        posts.pop(post_id)
        return {"message": "Post deleted"}
    else:
        raise HTTPException(status_code=404, detail="Post not found")
