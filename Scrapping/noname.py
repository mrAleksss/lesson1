name = i.find("a", class_="product-link ecommerce-product-link").text.replace("\n", "")
articul = i.find("div", class_="product__art").text
price = i.find("div", class_="product__price").text
url_img = "https://velotrade.com.ua" + i.find("img").get("src")
print(name, articul, price, url_img)