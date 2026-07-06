from pydantic import BaseModel
from typing import Optional

class MovieSchema(BaseModel):
    title: Optional[str] = None
    review: Optional[str] = None