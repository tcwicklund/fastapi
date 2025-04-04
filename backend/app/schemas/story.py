from pydantic import BaseModel
from typing import List, Optional


class StoryCreate(BaseModel):
    title: str
    prompt: str


class StoryRead(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True


class ChoiceCreate(BaseModel):
    text: str
    next_story_id: Optional[int]


class ChoiceRead(BaseModel):
    id: int
    text: str
    next_story_id: Optional[int]

    class Config:
        orm_mode = True
