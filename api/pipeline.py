from pydantic import BaseModel

from typing import List, Dict


class AlgoIn(BaseModel):
    algo_name: str 
    params: Dict[str,float] 
