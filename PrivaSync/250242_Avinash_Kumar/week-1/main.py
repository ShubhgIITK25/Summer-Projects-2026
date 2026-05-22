from fastapi import Depends, FastAPI, HTTPException, Query
from typing import Generator, Optional, List
from contextlib import asynccontextmanager
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel

class User(SQLModel,table=True):
    id: Optional[int] = Field(primary_key=True,default=None)
    name:str
sqlurl = "sqlite:///data.db"
engine = create_engine(sqlurl,echo=True)


app = FastAPI()
@app.on_event("startup")
async def on_startup():
    SQLModel.metadata.create_all(engine)
@app.get("/")
async def home():
    return {"data": "Hello World"}

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

@app.get("/users", response_model=List[User])
def read_users(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100) # Limits max results to 100 per request
):
    statement = select(User).offset(offset).limit(limit)
    users = session.exec(statement)
    return users

@app.post("/add")
def create_hero(user: User):
    try:
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            return user
    except:
        raise HTTPException(
            status_code=404,
            detail={'error': 'User can\'t be inserted', 'user_id': user_id} #This is a dict for customizing the error message
        )
