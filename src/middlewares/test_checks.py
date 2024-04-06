from werkzeug.wrappers import Response
from src.middlewares.checks import validate_shortcode_validity,validate_shortcode_in_use,validate_url_presence,validate_shortcode_exist


def test_validate_url_presence():
    data = {}
    result = validate_url_presence(data)
    assert isinstance(result,Response)
    assert result.status_code == 400
def test_validate_shortcode_in_use():
    response = {}
    result = validate_shortcode_in_use(response)
    assert isinstance(result,Response)
    assert result.status_code == 409
def test_validate_validity():
    data = {'shortcode':'abc^12'}
    result = validate_shortcode_validity(data)
    assert isinstance(result,Response)
    assert result.status_code == 412
def test_validate_shortcode_exist():
    response = None
    result = validate_shortcode_exist(response)
    assert isinstance(result,Response)
    assert result.status_code == 404
