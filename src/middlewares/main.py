from abc import ABC,abstractmethod
from werkzeug.wrappers import Request,Response
from src.library.utils.main import validate_string
from src.library.db_connector.main import RepositoryShortURL,DBConnector
from src.library.db_connector.models import ShortURL
from src.library.logger.main import Logger

USER = 'production'

class ValidateRoute(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def validate(self):
        pass
class ValidateNewShortCode(ValidateRoute):
    def __init__(self,data,repository):
        self.data = data
        self.repositoy = repository
    def validate(self):
        if 'url' not in self.data:
            return Response("Key 'url' not found", mimetype= 'text/plain', status=400)
        if 'shortcode' in self.data:
            response = self.repositoy.read_by_short_code(self.data['shortcode'])
            if response is not None:
                return Response("Shortcode already in use", mimetype= 'text/plain', status=409)
            if validate_string(self.data['shortcode']):
                return Response("The provided shortcode is invalid", mimetype= 'text/plain', status=412)
        return self.data
class ValidateExistShortCode(ValidateRoute):
    def __init__(self,data,respository):
        self.data = data
        self.repository = respository
    def validate(self):
        response =self.repository.read_by_short_code(self.data['shortcode'])
        if response is None:
            return Response("Shortcode not found", mimetype= 'text/plain', status=404)
        return self.data
def choose_middleware(route):
    if route.endswith("/shorten"):
        return ValidateNewShortCode
    return ValidateExistShortCode
class Middleware:
    def __init__(self, app):
        self.app = app
    def __call__(self,environ,start_response):
        # get call
        Logger.emit('Getting call')
        request = Request(environ)
        # get method
        method = request.method
        # get data
        Logger.emit('Get data from call')
        if method == 'POST':
            data = request.get_json()
        else:
            data = {"shortcode": request.path.split('/')[1]}
        # get path
        route = request.path
        # Choose the class accordingly with route
        class_validation = choose_middleware(route)
        # Instance the valid class
        Logger.emit('Making Validations')
        class_midleware = class_validation(data,RepositoryShortURL(DBConnector(USER,ShortURL)))
        res = class_midleware.validate()
        print(res)
        # If not pass for the validation
        if isinstance(res,Response):
            return res(environ, start_response)
        # if pass
        environ['data'] = res
        Logger.emit('Ending Validations')
        return self.app(environ, start_response)