import os


def capability_select():
    capability = {
        "platformName": "Android",
        "platformVersion": "8.1",
        "automationName": "Appium",
        "appPackage": "ru.mail.search.electroscope",
        "appActivity": "ru.mail.search.electroscope.ui.activity.AssistantActivity",
        "autoGrantPermissions": "true",
        "app": os.path.abspath(os.path.join(os.path.dirname(__file__),'../etc/Marussia_v1.39.1.apk')),
        "orientation": "PORTRAIT"
    }
    return capability