from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Define SQLAlchemy model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))  # Define the 'username' column
    email = Column(String(100))
    password = Column(String(100))

# Database connection
DATABASE_URL = "mysql+pymysql://root:Password272801%23%40!@localhost:3306/fastapidb"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

# Session creation
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations
@app.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Refresh the user to fetch the auto-generated ID
    return new_user

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str, email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.username = username
    user.email = email
    user.password = password
    db.commit()
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
