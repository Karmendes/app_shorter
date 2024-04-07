from time import sleep
import requests
from src.library.logger.main import Logger


# Função para imprimir os resultados dos testes
def test_case(description, request_info):
    Logger.emit('####################################')
    Logger.emit(description)
    sleep(2)

    response = requests.request(**request_info)
    Logger.emit(f"Request URL: {response.request.url}")
    Logger.emit(f"Response: {response.text}")

# Testing shorten route
URL_SHORTEN = "http://localhost:5000/shorten"

# Testing cases
test_case('Testing case with all param on json', {
    'method': 'POST',
    'url': URL_SHORTEN,
    'json': {'url': 'https://ge.globo.com/', 'shortcode': 'abcder'}
})
test_case('Testing case with just url', {
    'method': 'POST',
    'url': URL_SHORTEN,
    'json': {'url': 'https://google.com/'}
})
test_case('Testing case without url', {
    'method': 'POST',
    'url': URL_SHORTEN,
    'json': {}
})
test_case('Testing case shortcode repeated', {
    'method': 'POST',
    'url': URL_SHORTEN,
    'json': {"url": 'asgciagsciuah', "shortcode": 'abcdef'}
})
test_case('Testing case shortcode invalid', {
    'method': 'POST',
    'url': URL_SHORTEN,
    'json': {"url": 'asgciagsciuah', "shortcode": '$g5C7d'}
})

# Test stats route
Logger.emit('####################################')
Logger.emit('##### Test stats route')
Logger.emit('####################################')
sleep(2)

test_case('Testing case stats valid', {
    'method': 'GET',
    'url': "http://localhost:5000/abcdef/stats"
})
test_case('Testing case shortcode not found', {
    'method': 'GET',
    'url': "http://localhost:5000/abcdeg/stats"
})

# Test route redirect <shortcode>
Logger.emit('####################################')
Logger.emit('##### Test route redirect <shortcode>')
Logger.emit('####################################')
sleep(2)

test_case('Testing case redirect valid', {
    'method': 'GET',
    'url': "http://localhost:5000/abcder"
})
test_case('Testing case redirect not found', {
    'method': 'GET',
    'url': "http://localhost:5000/ascarg"
})
