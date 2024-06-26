import random
import string
import re
from datetime import datetime

def create_short_code():
    caracteres = string.ascii_letters + string.digits + "_"
    short_code = "".join(random.choice(caracteres) for _ in range(6))
    return short_code

def create_record_short_code(url,short_code):
    now = datetime.now()
    return {
        "short_code": short_code,
        "url":url,
        "created": now.isoformat(),
        "lastredirect":now.isoformat(),
        "redirectcount": 1
    }

def response_shortcode(shortcode):
    return {"shortcode":shortcode}

def validate_string(shortcode):
    pattern = r'^[a-zA-Z0-9_]{6}$'
    if not re.match(pattern, shortcode):
        return True
    return False