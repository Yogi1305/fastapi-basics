from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_name}")
async def get_user(user_name: str):
    return {"user": user_name}