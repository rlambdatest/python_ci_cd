import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def run_automation_script(row):
    username = row[0]
    access_key = row[1]
    # Replace this function with your actual automation script logic
    print(f"Running automation script with Username: {username} and Access Key: {access_key}")
    print("hello")
    grid_Url = "hub.lambdatest.com/wd/hub"
    options = webdriver.ChromeOptions()
    options.browser_version = ""
    options.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = username
    lt_options["accessKey"] = access_key
    lt_options["project"] = "Parallel1"
    lt_options["selenium_version"] = "4.0.0"
    lt_options["w3c"] = True
    options.set_capability('LT:Options', lt_options)
    
    # lt_options = {}
    # lt_options["username"] = "utkarshs"
    # lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
    lt_options["project"] = "Parallel1"
    lt_options["selenium_version"] = "4.0.0"
    lt_options["w3c"] = True
    url = "https://"+username+":"+access_key+"@"+grid_Url
    driver = webdriver.Remote(
        command_executor=url,
        options=options
        )
    driver.get("https://accounts.lambdatest.com/")
    # driver.get("https://accounts.lambdatest.com/")
    u_name = driver.find_element("id", "email")
    u_name.send_keys("rakeshs@lambdatest.com")
    # uname.send_keys("gauravp@lambdatest.com")
    # for  password
    p_word = driver.find_element("id", "password")
    p_word.send_keys("Rakesh@9015")
    # for login
    login = driver.find_element("id", "login-button")
    login.send_keys(Keys.ENTER)
    time.sleep(10)
    # for dropdown
    print("Test completed")
    time.sleep(10)
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
