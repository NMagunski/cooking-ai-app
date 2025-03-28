from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from app.utils.ai_helper import recipe_generator

app = FastAPI(
    title="Cooking AI API",
    version="1.0.0",
    description="API за генериране на рецепти"
)

# CORS настройки
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модел за заявката
class RecipeRequest(BaseModel):
    ingredients: List[str]
    equipment: List[str] = ["тиган"]
    diet: str = "none"
    max_time: int = 30

@app.post("/api/generate")
async def generate_recipe_endpoint(request: RecipeRequest):
    try:
        recipe = recipe_generator.generate_recipe(
            ingredients=request.ingredients,
            equipment=request.equipment,
            diet=request.diet,
            max_time=request.max_time
        )
        return {"success": True, "recipe": recipe}
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Грешка при генериране: {str(e)}"
        )

@app.get("/")
async def health_check():
    return {
        "status": "active",
        "mode": "local" if not recipe_generator.use_openai else "openai"
    }