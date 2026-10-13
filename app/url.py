import re
import requests

def check_url(url:str, root_url=None):
    if re.match(r'^https?://', url, re.IGNORECASE):
        new_url = url
    else:
        new_url = "".join(['https://', url])

    if re.match(fr'{root_url}', url, re.IGNORECASE):
        raise RecursionError

    if check_web_server(new_url):
        return new_url
    else:
        raise TimeoutError

def check_web_server(url:str, timeout:int = 3):
    try:
        reponse = requests.head(url, timeout=timeout)

        if reponse.status_code < 400:
            return True
    except requests.exceptions.RequestException:
        return False