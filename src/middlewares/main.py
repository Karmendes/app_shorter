from abc import ABC,abstractmethod
from werkzeug.wrappers import Request,Response
from src.library.db_connector.main import RepositoryShortURL,DBConnector
from src.library.db_connector.models import ShortURL
from src.library.logger.main import Logger
from src.middlewares.checks import validate_shortcode_in_use,validate_shortcode_validity,validate_url_presence,validate_shortcode_exist

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
        result = validate_url_presence(self.data)
        if result is not None:
            return result
        if 'shortcode' in self.data:
            result = validate_shortcode_validity(self.data)
            if result is not None:
                return result
            response = self.repositoy.read_by_short_code(self.data['shortcode'])
            result = validate_shortcode_in_use(response)
            if result is not None:
                return result
        return self.data
class ValidateExistShortCode(ValidateRoute):
    def __init__(self,data,respository):
        self.data = data
        self.repository = respository
    def validate(self):
        response =self.repository.read_by_short_code(self.data['shortcode'])
        result = validate_shortcode_exist(response)
        if result is not None:
            return result
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