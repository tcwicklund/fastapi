from app.db.models import Story, User
from sqlalchemy.orm import Session


def get_story_by_id(db: Session, story_id: int):
    return db.query(Story).filter(Story.id == story_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, email: str, hashed_password: str):
    db_user = User(email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_story(db: Session, title: str, content: str, user_id: int):
    db_story = Story(title=title, content=content, user_id=user_id)
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story
