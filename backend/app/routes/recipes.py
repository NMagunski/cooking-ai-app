from fastapi import APIRouter

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.get("/test")
async def test_recipes():
    return {"message": "Recipes endpoint works"}