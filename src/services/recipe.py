from src.schemas.recipe import Recipe, IRecipeFetcher
from typing import Final
import time
from src.schemas.category import CategoryId

class RecipeService():
    
    _recipe_fetcher: IRecipeFetcher
    SLEEP_TIME: Final = 1
    
    def __init__(self, recipe_fetcher: IRecipeFetcher):
        self._recipe_fetcher = recipe_fetcher
    
    def fetch_recipes_by_category_ids(self, category_ids: list[CategoryId]) -> dict[str, list[Recipe]] | dict[str, str]:
                
        recipes: dict[str, list[Recipe]] = {}
        for category_id in category_ids:
            # 一定時間スリープしてからリクエストを送る
            time.sleep(self.SLEEP_TIME)
            recipes[category_id] = self._recipe_fetcher.fetch_recipe(category_id)
            
        return recipes