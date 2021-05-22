import pytest

from mysql.client import MySQL_Client

@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MySQL_Client(user='root', psw='pass', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MySQL_Client(user='root', psw='pass', db_name='TEST_SQL')
        mysql_client.recreate_db()

        mysql_client.connect()
        mysql_client.create_TopRequests()
        mysql_client.create_TotalRequests()
        mysql_client.create_RequestsByMethod()
        mysql_client.create_ClientErrorRequests()
        mysql_client.create_ServerErrorUsers()

        mysql_client.connection.close()