from typing import Optional
from pydantic import BaseModel
import os
import json
import re

# from typing import List, Dict

from scripts.generate_json import generate_json
from scripts.run_post_treatment import apply
from scripts.sbm_data import get_dir_name_sbm, get_file_sbm


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
            if self.filter_select:
                # S6_example_leiden.res0.001_i2_post_cm_filter.R.tsv
                cluster_path = input_dir + "/leiden_res" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "/S6_example_leiden.res" + str(self.params["res"]) + "_i" + str(self.params["i"])+"_post_cm_filter.R.tsv"
            else:
                # S4_example_leiden.connectivity_modifier_res0.001_i2.tsv
                cluster_path = input_dir + "/leiden_res" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "/S4_example_leiden.connectivity_modifier_res" + str(self.params["res"]) + "_i" + str(self.params["i"])+".tsv"

            output_dir_path = input_dir + "/post"

            os.makedirs(output_dir_path, exist_ok=True)

            if "wcc" in self.post_treatment: 
                
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_res_" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "_wcc.tsv"
            else:
                
                output_file_path = output_dir_path + "/output_" + self.algo_name + "_res_" + str(self.params["res"]) + "_i" + str(self.params["i"]) + "_cc.tsv"


        elif  self.algo_name == "leiden_mod":

            if self.filter_select:
                # S6_example_leiden_mod.i1_post_cm_filter.R.tsv
                cluster_path = input_dir + "/leiden_mod_i" + str(self.params["i"]) + "/S6_example_leiden_mod.i" + str(self.params["i"])+"_post_cm_filter.R.tsv"
            else:
                # S4_example_leiden_mod.connectivity_modifier_i1.tsv
                cluster_path = input_dir + "/leiden_mod_i" + str(self.params["i"]) + "/S4_example_leiden_mod.connectivity_modifier_i" + str(self.params["i"])+".tsv"

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

        
        elif self.algo_name == "sbm":

            sbm_dir = get_dir_name_sbm(input_dir)

            if self.filter_select:
                cluster_path = input_dir + "/" + sbm_dir + "/" + get_file_sbm(input_dir + "/" + sbm_dir )
            else:
                cluster_path = input_dir + "/" + sbm_dir + "/S2_example_sbm_clustering.tsv"

            output_dir_path = input_dir + "/post"

            os.makedirs(output_dir_path, exist_ok=True)

            if "wcc" in self.post_treatment: 
                
                output_file_path = output_dir_path + "/output_sbm_clustering_wcc.tsv"
            else:
                
                output_file_path = output_dir_path + "/output_sbm_clustering_cc.tsv"


        
        cm_prefix = "cm-"
        if cm_prefix in self.post_treatment:
            post_treatment = self.post_treatment[len(cm_prefix):]
        else:
            post_treatment = self.post_treatment

        return apply(treatment=post_treatment,
              edge_list_path= "../api/"+self.file_path,
              cluster_path=cluster_path,
              output_file_path=output_file_path)
    
    def get_type_post(self, input_dir):

        if self.post_treatment == "cm" or self.post_treatment == "":
            out = "make_cm_ready"
        elif not self.filter_select:
            out = "connectivity_modifier"
        else:
            out = "post_cm_filter"

        if "leiden" in self.algo_name:
            algo = "leiden"
        else:
            algo = self.algo_name

        dirs = os.listdir(input_dir)

        dir = [d for d in dirs if algo in d and not d.startswith("S1")][0]
        sorted_files = sorted(list(os.listdir(os.path.join(input_dir,dir))), key=self.extract_step_number,  reverse=True)

        for f in sorted_files:
            if out in f and f.endswith(".tsv") and "stats" not in f:
                break
        
        for f_stats in sorted_files:
            if "stats" in f_stats:
                break
        

        
        return os.path.join(os.path.join(input_dir, dir), f), os.path.join(os.path.join(input_dir, dir), f_stats)
        
    def extract_step_number(self, name):
        match = re.match(r"S(\d+)_", name)
        return int(match.group(1)) if match else float('inf')  # Put unmatched at the end
