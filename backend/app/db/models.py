from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str
    stories: List["Story"] = Relationship(back_populates="user")


class Story(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    content: str
    choices: List["Choice"] = Relationship(back_populates="story")


class Choice(SQLModel, table=True):
    id: int = Field(primary_key=True)
    story_id: int = Field(foreign_key="story.id")
    text: str
    next_story_id: Optional[int]  # NULL means it's an ending
    story: Story = Relationship(back_populates="choices")
