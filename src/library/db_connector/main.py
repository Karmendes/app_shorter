from datetime import datetime
from sqlalchemy import create_engine,update
from sqlalchemy.orm import sessionmaker
from src.library.db_connector.models import ShortURL


connections = {
    "production":
    {
        'user':'postgres',
        'pwd':'postgres',
        'host':'localhost',
        'db':'db_shorter',
        'port':5432,
        'schema':'sc_shorter',
        'server':'postgresql'
    },
    "test":
    {
        'user':'postgres',
        'pwd':'postgres',
        'host':'localhost',
        'db':'db_shorter',
        'port':5432,
        'schema':'sc_shorter',
        'server':'postgresql'
    }
}


class DBConnector:
    def __init__(self,name_connection,model):
        self.connection = connections[name_connection]
        self.model = model
        self.connect()
    def connect(self):
        self.engine = create_engine(f"{self.connection['server']}://{self.connection['user']}:{self.connection['pwd']}@{self.connection['host']}:{self.connection['port']}/{self.connection['db']}?options=-csearch_path%3D{self.connection['schema']}")
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()

class RepositoryShortURL:
    def __init__(self,connection):
        self.connection = connection
        self.model = ShortURL
    def insert_by_dict(self,data):
        model = self.model(**data)
        self.connection.session.add(model)
        self.connection.session.commit()
        return data
    def read_by_short_code(self,short_code):
        return self.connection.session.query(self.model).filter(self.model.short_code==short_code).first()
    def update_use_short_code(self,short_code):
        # Create an update statement targeting the ShortURL table
        update_stmt = update(self.model).where(self.model.short_code == short_code)
        # Increment the redirectcount by 1
        update_stmt = update_stmt.values(redirectcount=self.model.redirectcount + 1)
        update_stmt = update_stmt.values(lastredirect = datetime.now().isoformat())
        # Execute the update statement
        self.connection.session.execute(update_stmt)
        self.connection.session.commit()
        return short_code
    