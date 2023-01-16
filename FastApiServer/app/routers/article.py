from fastapi import APIRouter, Depends
import app.cruds.article as dao
from sqlalchemy.orm import Session
from app.schemas.article import ArticleDTO
from app.database import get_db

router = APIRouter()