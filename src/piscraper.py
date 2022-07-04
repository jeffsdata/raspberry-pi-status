import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException

class SiteScraper:
    def __init__(self) -> None:
        pass

    def __buildDriver(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-crash-reporter")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-in-process-stack-traces")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--output=/dev/null")
        return webdriver.Chrome(options=options)

    def __tryToFindElement(self, driver, by, name):
        wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        return wait.until(EC.element_to_be_clickable((by, name)))

    def __simpleFinder(self, driver, name, url, byname, byvalue):
        driver.get(url)
        cartbutton = driver.find_elements(by=byname, value=byvalue)[0]
        domain = url.split("/")[2].replace("www.", "")
        statustext = cartbutton.get_attribute('innerText') if cartbutton.get_attribute('value') == '' or cartbutton.get_attribute('value') is None else cartbutton.get_attribute('value')
        print(f"{domain} - {name} - {statustext}")


    # PiShop.us

    def PiShopCheck(self):
        driver = self.__buildDriver()
        checklist = [
            {"name": "RPI Pico", "url": "https://www.pishop.us/product/raspberry-pi-pico/"},
            {"name": "RPI Pico PS", "url": "https://www.pishop.us/product/raspberry-pi-pico-with-pre-soldered-headers/"},
            {"name": "RPI Pico H", "url": "https://www.pishop.us/product/raspberry-pi-pico-h/"},
            {"name": "RPI Pico W", "url": "https://www.pishop.us/product/raspberry-pi-pico-w/"},
            {"name": "RPI Zero W", "url": "https://www.pishop.us/product/raspberry-pi-zero-w/"},
            {"name": "RPI Zero 2 W", "url": "https://www.pishop.us/product/raspberry-pi-zero-2-w/"},
            {"name": "RPI 4 B 1GB", "url": "https://www.pishop.us/product/raspberry-pi-4-model-b-1gb/"},
            {"name": "RPI 4 B 2GB", "url": "https://www.pishop.us/product/raspberry-pi-4-model-b-2gb/"},
            {"name": "RPI 4 B 4GB", "url": "https://www.pishop.us/product/raspberry-pi-4-model-b-4gb/"},
            {"name": "RPI 4 B 8GB", "url": "https://www.pishop.us/product/raspberry-pi-4-model-b-8gb/"}
        ]

        for item in checklist:
            self.__simpleFinder(driver, item.get("name"), item.get("url"), By.ID, "form-action-addToCart")


    def SparkFunCheck(self):
        driver = self.__buildDriver()
        checklist = [
            {"name": "RPI Pico", "url": "https://www.sparkfun.com/products/17829"},
            {"name": "RPI Pico H", "url": "https://www.sparkfun.com/products/20172"},
            {"name": "RPI Pico W", "url": "https://www.sparkfun.com/products/20173"},
            {"name": "RPI Zero W", "url": "https://www.sparkfun.com/products/14277"},
            {"name": "RPI Zero 2 W", "url": "https://www.sparkfun.com/products/18713"},
            {"name": "RPI 4 B 2GB", "url": "https://www.sparkfun.com/products/15446"},
            {"name": "RPI 4 B 4GB", "url": "https://www.sparkfun.com/products/15447"},
            {"name": "RPI 4 B 8GB", "url": "https://www.sparkfun.com/products/16811"}
        ]

        for item in checklist:
            self.__simpleFinder(driver, item.get("name"), item.get("url"), By.CSS_SELECTOR, "p.add-buttons > input.btn, p.add-buttons > button.btn")

    def AdafruitCheck(self):
        driver = self.__buildDriver()
        checklist = [
            {"name": "RPI Pico",        "url": "https://www.adafruit.com/product/4864"},
            {"name": "RPI Pico PS",     "url": "https://www.adafruit.com/product/5525"},
            {"name": "RPI Pico W",      "url": "https://www.adafruit.com/product/5526"},
            {"name": "RPI Pico W PS",   "url": "https://www.adafruit.com/product/5544"},
            {"name": "RPI Zero W",      "url": "https://www.adafruit.com/product/3400"},
            {"name": "RPI Zero 2 W",    "url": "https://www.adafruit.com/product/5291"},
            {"name": "RPI 4 B 1GB",     "url": "https://www.adafruit.com/product/4295"},
            {"name": "RPI 4 B 2GB",     "url": "https://www.adafruit.com/product/4292"},
            {"name": "RPI 4 B 4GB",     "url": "https://www.adafruit.com/product/4296"},
            {"name": "RPI 4 B 8GB",     "url": "https://www.adafruit.com/product/4564"}
        ]  

        for item in checklist:
            self.__simpleFinder(driver, item.get("name"), item.get("url"), By.CSS_SELECTOR, "div.prod-oos-box > .oos-header")

    def CanaKitCheck(self):
        driver = self.__buildDriver()
        checklist = [
            {"name": "RPI Pico",        "url": "https://www.canakit.com/raspberry-pi-pico.html"},
            {"name": "RPI Pico W",      "url": "https://www.canakit.com/raspberry-pi-pico-w.html"},
            {"name": "RPI Zero W",      "url": "https://www.canakit.com/raspberry-pi-zero-wireless.html"},
            {"name": "RPI Zero 2 W",    "url": "https://www.canakit.com/raspberry-pi-zero-2-w.html"},
            {"name": "RPI 4 B 1GB",     "url": "https://www.canakit.com/raspberry-pi-4.html"},
            {"name": "RPI 4 B 2GB",     "url": "https://www.canakit.com/raspberry-pi-4-2gb.html"},
            {"name": "RPI 4 B 4GB",     "url": "https://www.canakit.com/raspberry-pi-4-4gb.html"},
            {"name": "RPI 4 B 8GB",     "url": "https://www.canakit.com/raspberry-pi-4-8gb.html"}
        ]  

        for item in checklist:
            self.__simpleFinder(driver, item.get("name"), item.get("url"), By.CSS_SELECTOR, "table.pdtHeadTable > tbody > tr:first-of-type #ProductAddToCartDiv")

    def VilrosCheck(self):
        driver = self.__buildDriver()
        checklist = [
            {"name": "Control - IN Stock",     "url": "https://vilros.com/products/raspberry-pi-400-kit"},
            {"name": "RPI Pico",        "url": "https://vilros.com/products/raspberry-pi-pico"},
            {"name": "RPI Pico H",      "url": "https://vilros.com/products/raspberry-pi-pico-with-soldered-40-pin-header-3-pin-jtag-connector"},
            {"name": "RPI Pico W",      "url": "https://vilros.com/products/raspberry-pi-pico-wireless"},
            {"name": "RPI Zero",        "url": "https://vilros.com/products/raspberry-pi-zero"},
            {"name": "RPI Zero W",      "url": "https://vilros.com/products/raspberry-pi-zero-w"},
            {"name": "RPI Zero W H",    "url": "https://vilros.com/products/raspberry-pi-zero-wh"},
            {"name": "RPI Zero 2 W",    "url": "https://vilros.com/products/raspberry-pi-zero-2-w"},
            {"name": "RPI 4 B 1GB",     "url": "https://vilros.com/products/raspberry-pi-4-model-b"},
            {"name": "RPI 4 B 2GB",     "url": "https://vilros.com/products/raspberry-pi-4-2gb-ram"},
            {"name": "RPI 4 B 4GB",     "url": "https://vilros.com/products/raspberry-pi-4-4gb-ram"},
            {"name": "RPI 4 B 8GB",     "url": "https://vilros.com/products/raspberry-pi-4-model-b-8gb-ram"}
        ]     

        for item in checklist:
            self.__simpleFinder(driver, item.get("name"), item.get("url"), By.CSS_SELECTOR, "div.payment-buttons > button")

def main():
    logger = logging.getLogger(__name__)
    logger.info('Running Raspberry Pi Stock Checker')

    sc = SiteScraper()
    sc.PiShopCheck()
    sc.SparkFunCheck()
    sc.AdafruitCheck()
    sc.CanaKitCheck()
    sc.VilrosCheck()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()