from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

connections = {
    "shorter":
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
        self.cursor = self.session.query(self.model)
    