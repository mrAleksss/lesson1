import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/107.0.0.0 Safari/537.36"
}


def download(url):
    resp = requests.get(url, stream=True)
    r = open("C:\\Users\\User\\Desktop\\Velotrade_img\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1, 2):
        url = f"https://velotrade.com.ua/uk/shop/velosipedi/page/{count}/"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="product__item ecommerce-product__item mod_category_bike")

        for i in data:
            card_url = "https://velotrade.com.ua" + i.find("a").get("href")
            yield card_url


def parser():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        sleep(1)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="product-cart")

        name = data.find("h1").text
        articul = data.find("div", class_="product__code").text
        brand = data.find("a", class_="brand-link").text
        price_available = data.find("div", class_="b-product_price color-b").text
        description = data.find("div", class_="text clr").text
        url_img = "https://velotrade.com.ua" + data.find("a", class_="product__general-box-big-img fancybox-img").get(
            "href")
        download(url_img)
        yield name, articul, brand, price_available, description, url_img
