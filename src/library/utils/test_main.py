import string
from src.library.utils.main import create_short_code, create_record_short_code

# Test for create_short_code()
def test_create_short_code_length():
    short_code = create_short_code()
    assert len(short_code) == 6

def test_create_short_code_valid_characters():
    short_code = create_short_code()
    assert all(char in string.ascii_letters + string.digits + "_" for char in short_code)

# Test for create_record_short_code()
def test_create_record_short_code_fields():
    url = "https://www.example.com"
    short_code = "abcd12"
    record = create_record_short_code(url, short_code)
    assert record["short_code"] == short_code
    assert record["url"] == url
    assert "created" in record
    assert "lastredirect" in record
    assert "redirectcount" in record
    assert record['redirectcount'] == 1

def test_create_record_short_code_datetime_format():
    url = "https://www.example.com"
    short_code = "abcd12"
    record = create_record_short_code(url, short_code)
    assert isinstance(record["created"], str)  # Check for ISO format
    assert isinstance(record["lastredirect"], str)  # Check for ISO format