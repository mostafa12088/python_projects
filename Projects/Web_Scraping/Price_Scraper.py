# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:14:40 2019

@author: BME7ABT
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.de/dp/B075T76CP4/ref=sr_1_10?keywords=Sony%2BDSLR%2BCamera&qid=1576925385&s=ce-de&sr=1-10&th=1"

browser_agent = {
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
}


def check_price():
    page = requests.get(URL, headers=browser_agent)

    soup = BeautifulSoup(page.content, "html.parser")

    # title = soup.find(id = 'productTitle').get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if converted_price < 1.600:
        send_mail()
    print(converted_price)

    if converted_price > 1.600:
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login("engr.mostafa12088@gmail.com", "xuttcxebtuyswfxw")
        subject = "Hey, the price fell down!"
        body = "Please check the Amazon link: https://www.amazon.de/dp/B075T76CP4/ref=sr_1_10?keywords=Sony%2BDSLR%2BCamera&qid=1576925385&s=ce-de&sr=1-10&th=1"
        msg = f"subject: {subject}\n\n{body}"

        server.send_mail(
            "engr.mostafa12088@gmail.com",
            "fixed-term.MohammadMostafaBepari@de.bosch.com",
            msg,
        )
        print("Hey, Email has been sent")
        server.quit()
    except:
        print("Some error occured!")


# check_price()
while True:
    check_price()
    time.sleep(60 * 60)

