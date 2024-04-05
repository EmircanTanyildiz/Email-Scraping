import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.teknoparkistanbul.com.tr/firmalar")
browser.maximize_window()
time.sleep(1)
web_bağlantıları = []
def getMail():
    # XPath'in belirli bir aralıktaki elemanlarını döngüyle toplamak
    for i in range(1, 372):
        # time.sleep(1)
        # Her bir firma için XPath oluştur
        xpath = f"/html/body/div[4]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[{i}]/a"
        # XPath ile a tag'ını bul
        element = browser.find_element(By.XPATH,xpath)
        # a tag'ının href özelliğinden web bağlantısını al ve listeye ekle
        web_bağlantıları.append(element.get_attribute("href"))
        # Bağlantıları yazdır
    print(web_bağlantıları)
# WebDriver'ı kapat
getMail()
mail_adresleri = []

def check_at_symbol(text):
    if "@" in text:
        return True
    else:
        return False

def getMail():
    for x in web_bağlantıları:
        hatalimi = False
        browser.get(x)
        time.sleep(1)
        div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[6]/div"
        # Belirtilen XPath ile div elementini bul
        try:
            div_element = browser.find_element(By.XPATH,div_xpath)
        except:
            try:
                div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[5]/div"
                div_element = browser.find_element(By.XPATH,div_xpath)
            except:
                try:
                    div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[4]/div"
                    div_element = browser.find_element(By.XPATH,div_xpath)
                except:
                    try:
                        div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[3]/div"
                        div_element = browser.find_element(By.XPATH,div_xpath)
                    except:
                        try:
                            div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div"
                            div_element = browser.find_element(By.XPATH,div_xpath)
                        except:
                            print("Mail Adresi Belirtilmemis")
                            hatalimi = True
        finally: 
            div_xpath = "/html/body/div[4]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[6]/div"
        if hatalimi == False:
            # Bu div elementinin altındaki b tag'larını bul
            b_tags = div_element.find_elements(By.TAG_NAME,"b")
            #   Her bir b tagı için işlem yap
            for b_tag in b_tags:
                # b tag'ının altındaki a tag'ını bul
                a_tag = b_tag.find_element(By.TAG_NAME,"a")
                # a tag'ının içerdiği mail adresini al
                mail_adresi = a_tag.get_attribute("href").split(":")[1]
                # Mail adresini listeye ekle
                if check_at_symbol(mail_adresi):
                    mail_adresleri.append(mail_adresi)
                    print(mail_adresi)
                else:
                    print(f"{mail_adresi} ==> Mail Adresi Bulunamadi")                
                # time.sleep(0.5)
        hatalimi = False
# Mail adreslerini yazdır
getMail()
print(mail_adresleri)
browser.quit()
import pandas as pd
import listToExcel
c1 = listToExcel.convert
c1.listToDataFrame(mail_adresleri)