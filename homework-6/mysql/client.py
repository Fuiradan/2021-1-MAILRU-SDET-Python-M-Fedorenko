import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

from mysql.models import Base

class MySQL_Client:
    def __init__(self, user, psw, db_name):
        self.user = user
        self.psw = psw
        self.db_name = db_name

        self.host = '127.0.0.1'
        self.port = 3306

        self.engine = None
        self.connection = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db_name if db_created else ''

        self.engine = sqlalchemy.create_engine(
            f'mysql+pymysql://{self.user}:{self.psw}@{self.host}:{self.port}/{db}',
            encoding='utf8'
        )
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.connection.engine,
                                    autocommit=True,  # use autocommit on session.add
                                    expire_on_commit=False  # expire model after commit (requests data from database)
                                    )()


    def execute_query(self, query, fetch=True):
        res = self.connection.execute(query)
        if fetch:
            return res.fetchall()

    def recreate_db(self):
        self.connect(db_created=False)
        self.execute_query(f'DROP database if exists {self.db_name}', fetch=False)
        self.execute_query(f'CREATE database {self.db_name}', fetch=False)
        self.connection.close()

    def create_TotalRequests(self):
        if not inspect(self.engine).has_table('TotalRequests'):
            Base.metadata.tables['TotalRequests'].create(self.engine)

    def create_TopRequests(self):
        if not inspect(self.engine).has_table('TopRequests'):
            Base.metadata.tables['TopRequests'].create(self.engine)
        
    def create_RequestsByMethod(self):
        if not inspect(self.engine).has_table('RequestsByMethod'):
            Base.metadata.tables['RequestsByMethod'].create(self.engine)
    
    def create_ClientErrorRequests(self):
        if not inspect(self.engine).has_table('ClientErrorRequests'):
            Base.metadata.tables['ClientErrorRequests'].create(self.engine)
    
    def create_ServerErrorUsers(self):
        if not inspect(self.engine).has_table('ServerErrorUsers'):
            Base.metadata.tables['ServerErrorUsers'].create(self.engine)