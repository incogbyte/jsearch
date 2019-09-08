import sys
import argparse
import os
from requests_module import requests_module


try:
    from bs4 import BeautifulSoup
    import requests
    
except ImportError as e:
    print("[+] install requirements. pip3 install -r requirements.txt")
    print(f"{e}")
    sys.exit(1)


def main():

    filename = sys.argv[0]
    parse = argparse.ArgumentParser(description="Usage: {} -u <URL> -o output".format(filename))
    parse.add_argument('-u', "--url", type=str, required=True, help="[+] URL to craw")
    menu = parse.parse_args()

    if len(sys.argv[1:]) == 0:
        print(parse.print_help())

    jsearch = requests_module.CoreRequests(menu.url)
    jsearch.get_content_html()


if __name__ == "__main__":
    main()    