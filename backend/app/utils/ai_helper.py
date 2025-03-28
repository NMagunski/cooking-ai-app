import os
from typing import List
from .recipe_generator import LocalRecipeGenerator


class RecipeGenerator:
    def __init__(self, use_openai: bool = False):
        self.use_openai = use_openai
        self.local_gen = LocalRecipeGenerator()

    def generate_recipe(self,
                        ingredients: List[str],
                        equipment: List[str],
                        diet: str = "none",
                        max_time: int = 30) -> str:
        """
        Генерира рецепта (локално или чрез OpenAI)

        Параметри:
            ingredients: Списък със съставки
            equipment: Списък с налични кухненски уреди
            diet: Диетични изисквания
            max_time: Максимално време за приготвяне (в минути)
        """
        if not ingredients:
            return "Моля, добавете поне една съставка"

        if self.use_openai:
            return self._generate_with_openai(ingredients, equipment, diet, max_time)
        return self.local_gen.generate(ingredients, equipment, diet, max_time)

    def _generate_with_openai(self,
                              ingredients: List[str],
                              equipment: List[str],
                              diet: str,
                              max_time: int) -> str:
        """Резервиран за бъдеща интеграция с OpenAI"""
        raise NotImplementedError(
            "OpenAI интеграцията не е активирана. "
            "За да я използвате, добавете API ключ в .env и променете use_openai=True"
        )


# Глобална инстанция за лесен достъп
recipe_generator = RecipeGenerator(use_openai=False)