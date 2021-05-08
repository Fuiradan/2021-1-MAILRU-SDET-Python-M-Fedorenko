import pytest
from mysql.builder import MySQL_Builder


class MySQLBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql_builder = MySQL_Builder(mysql_client)

class TestMySQL(MySQLBase):
    def test_RequestsByMethod(self):
        records = self.mysql_builder.write_RequestsByMethod()
        assert len(records) == 4

    def test_TopRequests(self):
        records = self.mysql_builder.write_TopRequests()
        assert len(records) == 10

    def test_TotalRequests(self):
        records = self.mysql_builder.write_TotalRequests()
        assert len(records) == 1
    
    def test_ClientErrorRequests(self):
        records = self.mysql_builder.write_ClientErrorRequests()
        assert len(records) == 5
    
    def test_ServerErrorUsers(self):
        records = self.mysql_builder.write_ServerErrorUsers()
        assert len(records) == 5
        

