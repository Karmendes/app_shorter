from abc import ABC,abstractmethod
from src.library.utils.main import create_short_code,create_record_short_code
from src.library.logger.main import Logger

class Servicer(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(self):
        pass

class ServicerCreateShortLink(Servicer):
    def __init__(self,url,connector,short_code = None):
        self.url = url
        self.short_code = short_code
        self.connector = connector
    def run(self):
        Logger.emit('Starting the service to create shortcode')
        # Case the short code is not provided,create it
        if self.short_code is None:
            self.short_code = create_short_code()
        # Create record to save on database
        data = create_record_short_code(self.url,self.short_code)
        # Insert on database new short_code
        Logger.emit('Saving the shortcode on database')
        self.connector.insert_by_dict(data)
        return self.short_code

class ServiceGetUrlFromShortCode(Servicer):
    def __init__(self,connector,short_code):
        self.connector = connector
        self.short_code = short_code
    def run(self):
        Logger.emit('Starting the service to search for url')
        short_code = self.connector.read_by_short_code(self.short_code)
        Logger.emit('Updating the count of short code')
        self.connector.update_use_short_code(self.short_code)
        if short_code:
            return short_code.url
        return None