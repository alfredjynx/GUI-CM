from typing import Optional
from pydantic import BaseModel

# from typing import List, Dict

from scripts.generate_json import generate_json


class AlgoIn(BaseModel):
    algo_name: str 
    params: dict
    file_path: str

    def callJSON(self):
        if len(self.file_path) == 0:
            self.file_path = "network.tsv"

        return generate_json(self.algo_name, self.params, self.file_path)
    