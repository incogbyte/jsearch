import json
import os
from bs4 import BeautifulSoup
#from jsearch import *
from regex_modules import regex_modules
import re
from utils_module import colors


class FileTracker():

    def __init__(self, directory,name_target_in):
        self.directory = directory
        self.found_hits = []
        self.final_info = {}
        self.arrays_match = []
        self.domain = name_target_in


    def file_searcher(self):
        #print(self.directory)
        for filename in os.listdir(self.directory):
            try:
            
               if filename:#filename.endswith(".js"):
                  #print(os.path.join(self.directory, filename))
                  try:
                      with open(os.path.join(self.directory, filename), 'r') as file_out:
                         js_data = file_out.read()#.replace('\n', '')
                         self.test_js_file(js_data,os.path.join(self.directory, filename))
           
                  except Exception as ex1:
                    print(ex1)
                    pass
            
            

            except Exception as ex2:
                    print(ex2)
                    pass

  

    def test_js_file(self,js_file_data,file_path_info):
        #here we are pulling the data in from file over a url
        arrays_match = []
        try:
            
            for _,v in regex_modules.REGEX_PATT.items():
                values_found = re.findall(v,js_file_data)
                if values_found:
                   for v in values_found:
                       if v in arrays_match:
                           continue
                       else:
                           arrays_match.append(v) 
                
                self.final_info['found_matches'] = arrays_match
                self.final_info['values_found'] = values_found

                
            for file_hit in arrays_match:
                if "aws" in file_hit:
                    print(colors.colors.fg.red + f"[AWS INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['aws_info'] = file_hit

                elif self.domain in file_hit:
                    print(colors.colors.fg.orange + f"[DOMAIN INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['domain_info'] = file_hit

                

                elif "admin" in file_hit:
                    print(colors.colors.fg.red + f"[admin INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['admin'] = file_hit
                
                elif "AMAZON_KEY" in file_hit:
                    print(colors.colors.fg.red + f"[AMAZON_KEY INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['AMAZON_KEY'] = file_hit

      

                elif "api-key" in file_hit:
                    print(colors.colors.fg.red + f"[api-key INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['uploads'] = file_hit

      
               
  
                elif "vtex" in file_hit:
                    print(colors.colors.fg.red + f"[VTEX INFO] {file_hit}" + colors.colors.reset)
                    self.final_info['vtex_info'] = file_hit

          


                self.final_info['file_name'] = file_path_info
                self.found_hits.append(json.dumps(self.final_info))

            
        except Exception as e:
            print(f"error while parsing file contents \n{e}")
            pass
