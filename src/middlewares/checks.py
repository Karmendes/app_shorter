from werkzeug.wrappers import Response
from src.library.utils.main import validate_string

def validate_url_presence(data):
    if 'url' not in data:
        return Response("Key 'url' not found", mimetype= 'text/plain', status=400)
    return None

def validate_shortcode_in_use(response):
    if response is not None:
        return Response("Shortcode already in use", mimetype= 'text/plain', status=409)
    return None

def validate_shortcode_validity(data):
    if validate_string(data['shortcode']):
        return Response("The provided shortcode is invalid", mimetype= 'text/plain', status=412)
    return None

def validate_shortcode_exist(response):
    if response is None:
        return Response("Shortcode not found", mimetype= 'text/plain', status=404)
    return None
