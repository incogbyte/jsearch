from jsearch import BeautifulSoup, os, requests
from regex_modules import regex_modules
from urllib.parse import urlparse
from requests_module import requests_module
import re
from utils_module import colors

class CoreParser():
    
    def __init__(self, html_doc, url_domain,
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'):
        self.html_doc = html_doc
        self.url_domain = url_domain
        self.soup = BeautifulSoup(self.html_doc, 'html.parser')
        self.user_agent = user_agent
        self.urls = []
        self.host = urlparse(url_domain).hostname


    def parser_url(self,src_tags):
        parser_url_domain = urlparse(self.url_domain)
        parser_src_tags = urlparse(src_tags)
        
        if parser_src_tags.path[0:1] != '/':
            src_tags = parser_url_domain.scheme + "://" + parser_url_domain.hostname + "/" + parser_src_tags.path
            self.urls.append(src_tags)

        elif parser_src_tags.netloc == '':
            src_tags = parser_url_domain.scheme + "://" + parser_url_domain.hostname + parser_src_tags.path + "?" +\
                parser_src_tags.query
            self.urls.append(src_tags)
        else:
            self.urls.append(src_tags)

        
        
                    
    def get_content_js(self):
        
        test_conn = requests_module.CoreRequests(self.url_domain)
        if test_conn:
            current_dir = os.getcwd()
            path_save = ""
            #parsing_dir_name
            dir_name = urlparse(self.url_domain)
            dir_name = dir_name.hostname
            #dir_name = dir_name.hostname.replace(".", "_", -1)
        else:
            print(f"{self.url_domain} maybe down :/ ?")

        try:
            os.mkdir(str(dir_name))
            print(f">> Create directory {dir_name}")
            print(f">> File will be saved at {dir_name}")
        except FileExistsError as e:
            print(f">> {e}")
        
        
        for url_src_tag in self.urls:
            arrays_match = []
            try:
                if url_src_tag[0:2] == "//":
                    url_src_tag = "http:" + url_src_tag
                print(colors.colors.fg.yellow + f"[INFO] Getting info from: {url_src_tag}" + colors.colors.reset)
                r = requests.get(url_src_tag, verify=False, data={'User-Agent:': self.user_agent}, stream=True)
                content_save = r.content
                for _,v in regex_modules.REGEX_PATT.items():
                    values_found = re.findall(v, r.text)
                    if values_found:
                        for v in values_found:
                            if v in arrays_match:
                                continue
                            else:
                                arrays_match.append(v) 
                
                for url in arrays_match:
                    if "aws" in url:
                        print(colors.colors.fg.blue + f"[AWS INFO] {url}" + colors.colors.reset)
                    elif self.host in url:
                        print(colors.colors.fg.cyan + f"[DOMAIN INFO] {url}" + colors.colors.reset)
                    else:
                        print(colors.colors.fg.pink + f"[INFO URL] {url}" + colors.colors.reset)
                    
                         

            except ConnectionError as e:
                print(f">> Error while save content from \n{url_src_tag} \n {e}")

            try:
                name_save_url_tag = url_src_tag.replace(".", "_")
                name_save_url_tag = name_save_url_tag.replace("//", "_")
                name_save_url_tag = name_save_url_tag.replace("/", "_")[0:10]
                path_save = current_dir+"/"+dir_name+"/"+name_save_url_tag

                with open(path_save+".js",'wb') as f:
                    f.write(content_save)

            except FileNotFoundError as e:
                print(f">> Error while saving JS content to parse \n {e}")
        
    
    def find_all_script(self):
        for tag in self.soup.find_all("script"):
            if tag.get('src'):
                #print(tag.get('src'))
                self.parser_url(tag.get('src'))
            
    