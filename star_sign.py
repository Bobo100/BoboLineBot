# 星座爬蟲測試
from bs4 import BeautifulSoup
# from abc import ABC, abstractmethod
import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# 確認使用者輸入的星座
def check_zodiac(zodiac):
    html_doc=""
    # print(zodiac)
    # print(type(zodiac))
    if zodiac=="魔羯" or zodiac == "摩羯座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Capricorn"        
    elif zodiac == "水瓶" or zodiac == "水瓶座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Aries"
    elif zodiac == "雙魚" or zodiac == "雙魚座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Pisces"
    elif zodiac == "牡羊" or zodiac == "牡羊座" or zodiac == "白羊" or zodiac == "白羊座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Aries"
    elif zodiac == "金牛" or zodiac == "金牛座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Taurus"
    elif zodiac == "雙子" or zodiac == "雙子座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Gemini"
    elif zodiac == "巨蟹" or zodiac == "巨蟹座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Cancer"
    elif zodiac == "獅子" or zodiac == "獅子座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Leo"
    elif zodiac == "處女" or zodiac == "處女座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Virgo"
    elif zodiac == "天秤" or zodiac == "天秤座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Libra"
    elif zodiac == "天蠍" or zodiac == "天蠍座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Scorpio"
    elif zodiac == "射手" or zodiac == "射手座":
        html_doc = "https://www.daily-zodiac.com/mobile/zodiac/Sagittarius"
    else:
        print("Nothing")
    # print(html_doc)
    search(html_doc)

# 爬蟲搜尋
def search(html_doc):
    res = requests.get(html_doc)
    soup = BeautifulSoup(res.text, "html.parser")   

    all_contents = ""
    # 抓星座名稱
    names = soup.find_all("p", class_="name")
    for name in names:   
        print(name.text.replace(" ",""))
        # all_contents += f"{name.text.replace(' ','')}"
        # message = TextSendMessage(text=name.text.replace(" ",""))
        # line_bot_api.reply_message(event.reply_token, message)

    # 抓星座圖片
    images = soup.find('img')
    image_url = (
        "https://www.daily-zodiac.com/" + 
        images['src'] # assets/mobile/1-da42fab9e8797e8990d53f476d5b6af6da79e3b312f19f5171da43c4eee5f07a.png
    )
    # print(image_url)

    # 抓星座雜項內容
    others = soup.find_all("ul", class_="today")
    for other in others:   
        # print(other.text.replace(" ","")) #今日運勢 2022/01/18(二) 晴時多雲
        # message = TextSendMessage(text=other.text.replace(" ",""))
        # line_bot_api.reply_message(event.reply_token, message)
        all_contents += f"{other.text.replace(' ','')}"


    # 抓星座運勢內容
    contnets = soup.select("article")[0:]
    for contnet in contnets:
        # print(contnet.text.replace(" ",""))
        all_contents += f"{contnet.text.replace(' ','')}"
        # message = TextSendMessage(text=contnet.text.replace(" ",""))
        # line_bot_api.reply_message(event.reply_token, message)

    print(all_contents)

check_zodiac("牡羊")