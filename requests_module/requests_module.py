from jsearch import requests
from bs4_module import bs4_module

try:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
except ConnectionError as e:
    print("[+] SSL problem :/")
    print(f"{e}")
    pass

class CoreRequests():
    def __init__(self, url):
        self.url = url
        self.output_file = ""
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X inc0gbyt3; rv:42.0) Gecko/20100101 Firefox/42.0'

    def test_connection(self):
        
        try:
            head_connection = requests.head(self.url,verify=False,data={'User-Agent': self.user_agent})
            if head_connection.status_code == 200 or head_connection.status_code != 500 or head_connection.status_code != 404:
                return True
            else:
                return False
        except ConnectionError as e:
            print(f"[+] Connection problems.. {e}")

    

    def get_content_html(self):
        try:
            get_content = requests.get(self.url, data={'User-Agent': self.user_agent}, verify=False)
            if self.test_connection:
                soup_objt = bs4_module.CoreParser(get_content.text, self.url)
                soup_objt.find_all_script()
                soup_objt.get_content_js()

        except ConnectionError as e:
            print(f"Connection error while try to parse the URL content \n{e}")