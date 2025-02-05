from typing import Optional
from pydantic import BaseModel
import os
import json

# from typing import List, Dict

from scripts.generate_json import generate_json
from scripts.run_post_treatment import apply


class AlgoIn(BaseModel):
    algo_name: str 
    params: dict
    file_path: str
    post_treatment: str 
    filter_select: bool

    def generate_cargs_json(self):
        block_state = self.params["block_state"]
        degree_corrected = self.params["degree_corrected"]
        dictionaire = {
            "block_state": block_state, 
            "degree_corrected": degree_corrected
        }
        
        with open("../api/cargs.json", "w") as f:
            json.dump(dictionaire, f)
        
        return 


    def callJSON(self):
        if len(self.file_path) == 0:
            self.file_path = "network.tsv"
        
        if "cm" in self.post_treatment:
            include_cm = True
        else:
            include_cm = False

        return generate_json(self.algo_name, self.params, self.file_path, include_cm, self.filter_select)

    def postTreatment(self, input_dir):

        if self.post_treatment == "" or self.post_treatment == "cm":
            return



        if self.algo_name == "leiden":

            cluster_path = input_dir + "/leiden_res" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "/S5_example_leiden.connectivity_modifier_res" + str(self.params["res"]) + "_i" + str(self.params["i"])+".tsv"

            output_dir_path = input_dir + "/post"

            os.makedirs(output_dir_path, exist_ok=True)

            if "wcc" in self.post_treatment: 
                
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_res_" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "_wcc.tsv"
            else:
                
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_res_" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "_cc.tsv"


        elif  self.algo_name == "leiden_mod":

            cluster_path = input_dir + "/leiden_mod_i" + str(self.params["i"]) + "/S5_example_leiden_mod.connectivity_modifier_i" + str(self.params["i"])+".tsv"

            output_dir_path = input_dir + "/post"

            os.makedirs(output_dir_path, exist_ok=True)
            if "wcc" in self.post_treatment: 
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_i" + str(self.params["i"]) + "_wcc.tsv"
            else:
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_i" + str(self.params["i"]) + "_cc.tsv"

        
        elif  self.algo_name == "infomap":
            
            cluster_path = input_dir + "/infomap/S2_example_infomap_clustering.tsv"

            output_dir_path = input_dir + "/post"

            os.makedirs(output_dir_path, exist_ok=True)
            if "wcc" in self.post_treatment: 
                output_file_path = output_dir_path + "/output_infomap_clustering_wcc.tsv"
            else:
                output_file_path = output_dir_path + "/output_infomap_clustering_cc.tsv"

        
        
        
        cm_prefix = "cm-"
        if cm_prefix in self.post_treatment:
            self.post_treatment = self.post_treatment[len(cm_prefix):]

        return apply(treatment=self.post_treatment,
              edge_list_path= "../api/"+self.file_path,
              cluster_path=cluster_path,
              output_file_path=output_file_path)
        
