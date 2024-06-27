import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = EMAIL
MY_PASSWORD = PASSWORD
product_url = AMAZON_PRODUCT_LINK
DESIRED_PRICE = 400
product_description = ""

headers = {
    "Accept-Language": " ",
    "User-Agent": " "
}

response = requests.get(url=product_url, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
str_price = soup.find(name=" ", class_=" ")
stripped_price = str_price.text.replace("$", "")
price = float(stripped_price)
print(price)

if price <= DESIRED_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECIPIENT_ADDRESS
                            msg=f"Subject: Amazon Price Alert!\n\n {product_description} price is now ${price}\n{product_url}")



