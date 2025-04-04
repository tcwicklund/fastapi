from fastapi import APIRouter, HTTPException
from app.schemas import StoryCreate, StoryRead, ChoiceCreate, ChoiceRead
from app.services.story_service import generate_story
from app.db.session import Session
from app.db.models import Story, Choice
from sqlalchemy.orm import Session as SQLSession

router = APIRouter()


# Generate a new story
@router.post("/generate", response_model=StoryRead)
async def create_story(story_create: StoryCreate, db: SQLSession = Depends(get_db)):
    """Generate a new story based on a prompt"""
    story_text = generate_story(story_create.prompt)

    # Save story to DB
    story = Story(title=story_create.title, content=story_text)
    db.add(story)
    db.commit()
    db.refresh(story)

    return story


# Get all story titles
@router.get("/", response_model=list[StoryRead])
async def get_stories(db: SQLSession = Depends(get_db)):
    """Get a list of all stories"""
    return db.query(Story).all()


# Get a specific story by ID
@router.get("/{story_id}", response_model=StoryRead)
async def get_story(story_id: int, db: SQLSession = Depends(get_db)):
    """Get a specific story by ID"""
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story


# Create a new choice for a story
@router.post("/{story_id}/choice", response_model=ChoiceRead)
async def create_choice(
    story_id: int, choice_create: ChoiceCreate, db: SQLSession = Depends(get_db)
):
    """Create a new choice for a story"""
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    choice = Choice(
        story_id=story_id,
        text=choice_create.text,
        next_story_id=choice_create.next_story_id,
    )
    db.add(choice)
    db.commit()
    db.refresh(choice)

    return choice


# Get all choices for a specific story
@router.get("/{story_id}/choices", response_model=list[ChoiceRead])
async def get_choices(story_id: int, db: SQLSession = Depends(get_db)):
    """Get all choices for a specific story"""
    story = db.query(Story).filter(Story.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")

    return db.query(Choice).filter(Choice.story_id == story_id).all()
