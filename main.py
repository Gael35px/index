from os import name
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


User = "standard_user"
Password = "secret_sauce"

def main():
    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    #option.add_argument("--headless")
    option.add_argument("--window-size=1920,1080")
    driver = Chrome(service=service, options=option)
    driver.get("https://www.mercadolibre.com.mx/ofertas/novedades-de-temporada")

#extraerdatos
    products = driver.find_elements(By.CLASS_NAME, "andes-carousel-snapped__wrapper")
    product_data = []
    for product in products:
        name = product.find_element(By.CLASS_NAME, "poly-component__title").text
        price = product.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
        print(f"Nombre: {name}, Precio: {price}")
        product_data.append([name, price])

#cuadro con datos
    import pandas as pd
    df = pd.DataFrame(product_data, columns=["Nombre", "Precio"])
    print(df)

#guardar en excel
df.to_excel("productos.xlsx", index=False)

if __name__ == '__main__':
    main()