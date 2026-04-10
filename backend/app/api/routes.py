from fastapi import APIRouter

router = APIRouter()

@router.get("/upload")
def upload():
    return "upload file"

@router.get("/detect") 
def detect():
    return "detect threats"

@router.get("/history")
def history():
    return "show history"