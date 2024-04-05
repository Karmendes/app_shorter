from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ShortURL(Base):
    __tablename__ = "sc_shorter.tb_shorters_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_code = Column(String(6), unique=True)
    url = Column(String(2048))
    dt_created = Column(DateTime)
    dt_updated = Column(DateTime)