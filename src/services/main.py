from abc import ABC,abstractmethod
from src.library.utils.main import create_short_code,create_record_short_code

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
        # Case the short code is not provided,create it
        if self.short_code is None:
            self.short_code = create_short_code()
        # Create record to save on database
        data = create_record_short_code(self.url,self.short_code)
        # Insert on database new short_code
        self.connector.insert_by_dict(data)
        return self.short_code
