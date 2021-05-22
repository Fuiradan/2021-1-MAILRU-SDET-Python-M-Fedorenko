import pytest
from mysql.builder import MySQL_Builder


class MySQLBase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql_builder = MySQL_Builder(mysql_client)

class TestMySQL(MySQLBase):
    def test_RequestsByMethod(self):
        parced_data, records = self.mysql_builder.write_RequestsByMethod()
        assert len(records) == len(parced_data)

    def test_TopRequests(self):
        parced_data, records = self.mysql_builder.write_TopRequests()
        assert len(records) == len(parced_data)

    def test_TotalRequests(self):
        parced_data, records = self.mysql_builder.write_TotalRequests()
        assert len(records) == len(parced_data)
    
    def test_ClientErrorRequests(self):
        parced_data, records = self.mysql_builder.write_ClientErrorRequests()
        assert len(records) == len(parced_data)
    
    def test_ServerErrorUsers(self):
        parced_data, records = self.mysql_builder.write_ServerErrorUsers()
        assert len(records) == len(parced_data)
        

