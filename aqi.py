import requests

from bs4 import BeautifulSoup

def get_aqi(url="https://airnow.tehran.ir"):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    vals = soup.find_all("span", {"class": "info-box-number aqival", "id": "ContentPlaceHolder1_lblAqi3h"})
    return int(vals[0].text)
