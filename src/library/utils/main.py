import random
import string

def create_short_code():
    caracteres = string.ascii_letters + string.digits + "_"
    short_code = "".join(random.choice(caracteres) for _ in range(6))
    return short_code