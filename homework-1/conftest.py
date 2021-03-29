import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--url', default='http://www.target.my.com')

@pytest.fixture(scope="session")
def config(request):
    url = request.config.getoption('--url')
    return {'url':url}

@pytest.fixture()
def user_creds():
    creds = dict(
    login = "maxfedorenko86@mail.ru",
    psw = "BGlogg3cXB"
    )
    return creds

@pytest.fixture(scope="function")
def driver(config):
    url = config['url']
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)
    browser.maximize_window()
    yield browser
    browser.close()