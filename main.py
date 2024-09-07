from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests
import re

SENDKEY = os.environ.get("SERVERCHANSENDKEY")


def get_info_from_iflow():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("https://www.iflow.work/")
        time.sleep(5)
        element = driver.find_element(By.CLASS_NAME, "grid")
        print("Element value:\n", element.text)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        result = element.text
        driver.quit()
        return result


def send_info_to_server_chan(title, description="", key=SENDKEY):
    postdata = {"title": title, "desp": description}
    url = f"https://sctapi.ftqq.com/{key}.send"
    requests.post(url=url, json=postdata)


def shorten_info(info):
    stripped = info.split("\n")
    guadaozhishu = -1
    year = -1
    season = -1
    month = -1

    match = re.search(r"\d+\.\d+", stripped[0])
    if match:
        guadaozhishu = match.group()

    match = re.search(r"\d+", stripped[1])
    if match:
        month = match.group()

    match = re.search(r"\d+", stripped[2])
    if match:
        season = match.group()

    match = re.search(r"\d+", stripped[3])
    if match:
        year = match.group()

    result = f"行情指数:{guadaozhishu}，超越本年{year}%，本季{season}%，本月{month}%"
    print(result)
    return result


if __name__ == "__main__":
    info = get_info_from_iflow()
    shorted = shorten_info(info)
    send_info_to_server_chan(info, description="今日行情")
