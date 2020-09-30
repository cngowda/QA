# CSP_HOST = "env-3.test.infoblox.com"
# CSP_USER = "achandran@infoblox.com"
CSP_PASSWORD = "Cto-bonfire1*"
# no_of_iteration = 2
# no_of_refresh = 5


import requests
import logging
logger = logging.getLogger(__name__)
import pytest
import time
from tabulate import tabulate
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def test_standalone(params):
    csp_load_time = {}
    composite_ui_time = {}
    root_ui_time = {}
    csp_url = "https://" + params['CSP_HOST'] + "/"
    print(f"CSP version: {((requests.get(csp_url + 'atlas/version')).content)}")
    for i in range(1, int(params['iteration']) +1):
        csp_load_time[i] = []
        composite_ui_time[i] = []
        root_ui_time[i] = []

        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome()
        #loading time
        time_before_csp_load = time.time()
        driver.get(csp_url)
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "idp-discovery-username")))
        except Exception as e:
            logger.exception(e)
        time_after_csp_load = time.time()
        csp_load = time_after_csp_load - time_before_csp_load
        print(f"Time took to load CSP : {csp_load}")
        csp_load_time[i].append(csp_load)

        #login csp
        element = driver.find_element_by_id("idp-discovery-username")
        element.send_keys(params['CSP_USER'])
        element = driver.find_element_by_id("idp-discovery-submit")
        element.click()
        try:
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.ID, "okta-signin-password")))
        except Exception as e:
            logger.exception(e)
        element = driver.find_element_by_id("okta-signin-password")
        element.send_keys(CSP_PASSWORD)
        element = driver.find_element_by_id("okta-signin-submit")
        element.click()

        #time to load landing page
        for j in range(1, int(params['refresh']) +1):
            # composite_ui_time[i][j] = []
            diff_time = load_time(driver, csp_url)
            print(f"Composite UI : {diff_time}")
            composite_ui_time[i].append(diff_time)
            driver.refresh()

        cookie= driver.get_cookie('csp_userrootui')
        print(cookie)
        if cookie:
            print(f"In Root UI, cookies : {driver.get_cookies()}")
        else:
            print(f"In Composite UI, cookies : {driver.get_cookies()}")

        print("setting Cookies")
        driver.add_cookie({'name': 'csp_userootui', 'value': 'true', 'domain': 'env-3.test.infoblox.com'})
        print(driver.get_cookies())

        for k in range(1, int(params['refresh'])+1):
            # root_ui_time[i][k] = []
            diff_time = load_time(driver, csp_url)
            print(f"root UI {diff_time}")
            root_ui_time[i].append(diff_time)
            driver.refresh()
        driver.quit()
    print(composite_ui_time)
    print(root_ui_time)

    print("Composite UI")
    for k, v in composite_ui_time.items():
        print(f"\n{k} : {v}")
    print("Root UI")
    for k, v in root_ui_time.items():
        print(f"\n{k} : {v}")



def load_time(driver, csp_url):
    before_landing_page = time.time()
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ib-navigation-content-container']")))
    except Exception as e:
        logger.exception(e)
    response = requests.get(csp_url)
    print(response.headers)
    after_landing_page = time.time()
    logedpgetime = after_landing_page - before_landing_page
    return logedpgetime
