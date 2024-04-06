from datetime import datetime
from sqlalchemy import create_engine,update
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
    def insert_by_dict(self,data):
        model = self.model(**data)
        self.session.add(model)
        self.session.commit()
    def read_by_short_code(self,short_code):
        return self.session.query(self.model).filter_by(short_code=short_code).first()
    def update_use_short_code(self,short_code):
        # Create an update statement targeting the ShortURL table
        update_stmt = update(self.model).where(self.model.short_code == short_code)
        # Increment the redirectcount by 1
        update_stmt = update_stmt.values(redirectcount=self.model.redirectcount + 1)
        update_stmt = update_stmt.values(lastredirect = datetime.now().isoformat())
        # Execute the update statement
        self.session.execute(update_stmt)
        self.session.commit()
    