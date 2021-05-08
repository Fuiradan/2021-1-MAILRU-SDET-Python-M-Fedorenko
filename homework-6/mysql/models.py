from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TotalRequests(Base):
    __tablename__ = 'TotalRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable = False)

    def __repr__(self):
        return f"<TotalRequests(" \
               f"id='{self.id}'," \
               f"quantity='{self.quantity}'" \
               f")>"

class TopRequests(Base):
    __tablename__ = 'TopRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000), nullable=False)
    quantity = Column(Integer, nullable = False)     

    def __repr__(self):
        return f"<TopRequests(" \
               f"id='{self.id}'," \
               f"url='{self.url}'," \
               f"quantity='{self.quantity}'" \
               f")>"

class RequestsByMethod(Base):
    __tablename__ = 'RequestsByMethod'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    method = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable = False)

    def __repr__(self):
        return f"<RequestsByMethod(" \
               f"id='{self.id}'," \
               f"method='{self.method}'," \
               f"quantity='{self.quantity}'" \
               f")>"

class ClientErrorRequests(Base):
    __tablename__ = 'ClientErrorRequests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000), nullable=False)
    statuscode = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(15), nullable=False)

    def __repr__(self):
        return f"<RequestsByMethod(" \
               f"url='{self.url}'," \
               f"statuscode='{self.statuscode}'," \
               f"size='{self.size}'," \
               f"ip='{self.ip}'" \
               f")>"

class ServerErrorUsers(Base):
    __tablename__ = 'ServerErrorUsers'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(15), nullable=False)
    quantity = Column(Integer, nullable = False)
  
    def __repr__(self):
        return f"<RequestsByMethod(" \
               f"ip='{self.ip}'," \
               f"quantity='{self.quantity}'" \
               f")>"
