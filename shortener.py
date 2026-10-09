import secrets

ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

data = {}

def code_generator(lenght=5):
    code = "".join(secrets.choice(ALPHA) for _ in range(lenght))
    return code

def shorten(link:str):
    data[link] = code_generator()
