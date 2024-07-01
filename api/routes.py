from fastapi import APIRouter, HTTPException, status

from pipeline import AlgoIn


router = APIRouter()

@router.get("/test", response_model=str, tags=["items"])
def get_tracking(): 
    return "Ola meu bom"



@router.post("/pipeline", response_model=AlgoIn, status_code=status.HTTP_201_CREATED, tags=["items"])
def run_pipeline(algoIn: AlgoIn): 
    return algoIn
   