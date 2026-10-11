import re
import requests

def check_url(url:str):
    if re.match(r'^https?://', url, re.IGNORECASE):
        return
    else:
        new_url = "".join(['https://', url])
        return new_url

def check_web_server(url:str):
    try:
        reponse = requests.head(url, timeout=5)

        if reponse.status_code < 400:
            return True
    except requests.exceptions.RequestException:
        return False