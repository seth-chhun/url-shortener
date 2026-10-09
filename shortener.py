import secrets
import storage

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def code_generator(lenght=5):
    code = "".join(secrets.choice(ALPHA) for _ in range(lenght))
    return code

def shorten(url:str):
    storage.insert(code_generator(), url)

