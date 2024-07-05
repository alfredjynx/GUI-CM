from pydantic import BaseModel

# from typing import List, Dict

from scripts.generate_json import generate_json


class AlgoIn(BaseModel):
    algo_name: str 
    params: dict

    def callJSON(self):

        return generate_json(self.algo_name, self.params)