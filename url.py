import re

def check_url(url:str):
    if re.match(r'^https?://', url, re.IGNORECASE):
        return
    else:
        new_url = "".join(['https://', url])
        return new_url