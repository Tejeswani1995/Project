import pytest
import os
import json
import logging
import configparser
from selenium import webdriver
from datetime import datetime
from inclusive_function.configure import Config



def pytest_addoption(parser):

    parser.addoption("--browser", action="store", default=Config.BROWSER)
    parser.addoption("--f", action="store", default="../configration/config.json")





config = configparser.RawConfigParser()
config.read("..\\pytest.ini")



@pytest.fixture(scope="class")
def log(request):

    logging.basicConfig(filename=config.get('pytest', 'log_file'), format=config.get('pytest', 'log_file_format'),
                            datefmt=config.get('pytest', 'log_file_date_format'))
    logger = logging.getLogger()
    logger.setLevel(config.get('pytest', 'log_file_level'))

    request.cls.logger = logger
    return request.cls.logger




# fixture to launch browser via command prompt

@pytest.fixture(scope="class")
def get_browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture(scope="class")
@pytest.mark.usefixtures("log")
def launch_browser(request, get_browser, log):

    if get_browser == "chrome" :
        log.info("launching chrome browser")
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)


    elif get_browser == "edge":
        log.info("launching  edge browser")
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge()


    else:
        Exception


    driver.maximize_window()
    driver.get(Config.URL)
    driver.implicitly_wait(30)

    request.cls.driver = driver

    yield request.cls.driver

    driver.quit()




















# # launch browser via json file
# @pytest.fixture()
# def get_json_file(request):
#     file_name = request.config.getoption("--f")
#     return file_name
#
#
# @pytest.fixture()
# def launch_browser_json(get_json_file):
#
#     file = open(get_json_file)
#     data = json.load(file)
#
#     browser = data["browser"]
#
#     if browser == "chrome":
#         credentials = webdriver.ChromeOptions()
#         credentials.browser_version = data["version"]
#         credentials.platform_name = data["platform"]
#         driver = webdriver.Chrome(options=credentials)
#
#     elif browser == "edge":
#         credentials = webdriver.EdgeOptions()
#         credentials.browser_version = data["version"]
#         credentials.platform_name = data["platform"]
#         driver = webdriver.Chrome(options=credentials)
#
#     driver.get("https://www.sony.co.in")
#     driver.maximize_window(Config.URL)
#     driver.implicitly_wait(20)
#
#     yield driver
#
#     driver.quit()
#



# # hook to generate the report in test_report file
#
# @pytest.fixture()
# def func_name(request):
#     os.chdir("../log_files/")
#     with open("test_report.txt", "a") as file:
#         file.write(request.node.name)
#
#
# def generate_test_report(session):
#
#     # You can access session information and statistics here
#     passed = session.testscollected - session.testsfailed
#     total = session.testscollected
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     os.chdir("../log_files/")
#
#     report = f"Test report generated at {timestamp}\n"
#     report += f"Total tests: {total}\n"
#     report += f"Tests passed: {passed}\n"
#     report += f"Tests failed: {session.testsfailed}\n"
#
#     with open("test_report.txt", "a") as file:
#         file.write(report)
#         file.write("\n")
#     # print(report)
#
#
# @pytest.hookimpl(tryfirst=False)
# def pytest_sessionfinish(session):
#     generate_test_report(session)
#
