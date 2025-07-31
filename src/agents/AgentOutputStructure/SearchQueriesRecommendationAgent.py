from typing import List
from pydantic import BaseModel, Field

class SuggestedSearchQueries(BaseModel):
    queries: List[str] = Field(
        ...,
        title="Suggested search queries to be passed to the search engine",
    )
