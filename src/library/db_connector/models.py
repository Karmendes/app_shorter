from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ShortURL(Base):
    __tablename__ = "tb_shorters_link"
    __table_args__ = {'schema': 'sc_shorter'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_code = Column(String(6), unique=True)
    url = Column(String(2048))
    created = Column(DateTime)
    lastredirect = Column(DateTime)
    redirectcount = Column(Integer)
    