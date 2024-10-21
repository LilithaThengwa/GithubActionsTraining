from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    published_date: Optional[str] = None

# BaseModel: Inherits from pydantic.BaseModel, which handles validation and serialization.
# Optional Fields: Using Optional[dataType] to declare a field as optional with a default value of None.
# List and Nested Models: Pydantic allows lists and nested data models to be validated.