import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
# nOt0r5Le5LhYZjrmZ6DpW4QvvXBXTCyG670NB1H02zr1ik9Zwh
import csv

def run_automation_script(row):
    username = row[0]
    accesskey = row[1]
    print(f"Running automation script with Username: {username} and Access Key: {accesskey}")
    print("hello")
    build = os.getenv('LT_BUILD_NAME')
    gridUrl = "hub.lambdatest.com/wd/hub"
    options = ChromeOptions()
    options.browser_version = "112.0"
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = ""
    lt_options["accessKey"] = ""
    lt_options["project"] = "selenium test"
    lt_options["name"] = "selenium"
    lt_options["build"] = build
    lt_options["network"] = True
    lt_options["networkThrottling"] = "Regular 3G"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options.set_capability('LT:Options', lt_options)
    # "http://hub.lambdatest.com/wd/hub"
    url = "https://"+username+":"+accesskey+"@"+gridUrl
    driver = webdriver.Remote(
            command_executor=url,
            options=options
        )
    Username = ""
    pd = ""
    Url = "https://accounts.lambdatest.com/login"
    # driver = webdriver.Chrome()
    driver.get(Url)
    uname = driver.find_element("id", "email")
    uname.send_keys(Username)
    password = driver.find_element("id", "password")
    password.send_keys(pd)
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    driver.quit()

filename = "crediantial.csv"

with open(filename, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  
    for row in csvreader:
        if len(row) >= 2:
            run_automation_script(row)
            print("wait")
            

print("finished")


