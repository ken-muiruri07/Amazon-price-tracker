import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "kenmuiruri187@gmail.com"
MY_PASSWORD = "uhpf pmaw frlq ojua"
product_url = "https://www.amazon.com/dp/B0CBD2G4KZ/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&aref=L8frR99e2z&th=1"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}

response = requests.get(url=product_url, headers=headers)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
str_price = soup.find(name="span", class_="aok-offscreen")
stripped_price = str_price.text.replace("$", "")
price = float(stripped_price)
print(price)

if price > 20:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="kenmuiruri07@gmail.com",
                            msg=f"Subject: Amazon Price Alert!\n\n Tasty Mini Rice Cooker with Removable Nonstick Bowl "
                                f"and Auto Keep Warm Function, Great For Soups, Stews, Grains and Oats, 6 Cups Cooked "
                                f"(3 Cups Uncooked), 1.5-Quart, White price is now ${price}\n{product_url}")



