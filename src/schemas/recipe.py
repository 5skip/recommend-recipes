from pydantic import BaseModel, Field, field_validator
from abc import ABC, abstractmethod

class Recipe(BaseModel):
    id: int
    title: str
    url: str = Field(..., title='URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+") # URLの正規表現
    description: str
    image_url: str = Field(..., title='Image URL', pattern="https?://[\\w!?/+\\-_~;.,*&@#$%()'\\[\\]]+")
    category_id: str
    
    @field_validator('category_id')
    @classmethod
    def category_id_must_have_three_parts(cls, v):
        parts = v.split('-')
        if len(parts) != 3:
            raise ValueError('カテゴリーのIDは大-中-小の3つの部分で指定してください')
    
# レシピ取得用の抽象クラス
class IRecipeFetcher(ABC):
    @abstractmethod
    def fetch_recipe(self, category_id: str) -> list[Recipe]:
        """
        レシピを取得する
        
        category_idは大-中-小の順で指定する
        例: 10-200-2001
        """
        pass