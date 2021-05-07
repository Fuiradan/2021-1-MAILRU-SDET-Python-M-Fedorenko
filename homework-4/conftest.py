import pytest
import os

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--appium', default='http://127.0.0.1:4723/wd/hub')

@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.pardir))

@pytest.fixture(scope='session')
def config(request):
    appium = request.config.getoption('--appium')
    return {'appium': appium}