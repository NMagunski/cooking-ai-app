from typing import List
import random


class LocalRecipeGenerator:
    """Локално генериране на рецепти без OpenAI"""

    @staticmethod
    def _get_random_cooking_method():
        methods = [
            "запържете",
            "запечете",
            "варете",
            "пържете на тиган",
            "гответе на пара"
        ]
        return random.choice(methods)

    @staticmethod
    def generate(ingredients: List[str], equipment: List[str], diet: str = "none", max_time: int = 30) -> str:
        main_ingredient = ingredients[0] if ingredients else "продукти"
        method = LocalRecipeGenerator._get_random_cooking_method()

        recipe = f"""РЕЦЕПТА: {main_ingredient.capitalize()} по домашно

СЪСТАВКИ:
- {'\n- '.join(ingredients)}

ИНСТРУКЦИИ:"""

        steps = [
            f"Почистете и нарежете {main_ingredient}",
            f"Загрейте {equipment[0] if equipment else 'съда'} на средна температура",
            f"Добавете малко зехтин или олио",
            f"{method.capitalize()} {main_ingredient} за {random.randint(5, max_time)} минути",
            "Добавете подправки на вкус",
            "Сервирайте топло"
        ]

        if "фурна" in equipment:
            steps.insert(2, "Предварително загряйте фурната на 180°C")

        for i, step in enumerate(steps, 1):
            recipe += f"\n{i}. {step}"

        recipe += f"\n\nОЧАКВАНО ВРЕМЕ: {max_time} минути"

        if diet != "none":
            recipe += f"\n\nДИЕТИЧНО: Подходяща за {diet} диета"

        return recipe