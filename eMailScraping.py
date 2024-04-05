import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.teknoparkistanbul.com.tr/firmalar")
browser.maximize_window()
time.sleep(1)
web_bağlantıları = []
def getMail(): 
    for i in range(1, 372):# XPath'in belirli bir aralıktaki elemanlarını döngüyle toplamak
        xpath = f"/html/body/div[4]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[{i}]/a"  # Her bir firma için XPath oluştur
        element = browser.find_element(By.XPATH,xpath) # XPath ile a tag'ını bul
        web_bağlantıları.append(element.get_attribute("href")) # a tag'ının href özelliğinden web bağlantısını al ve listeye ekle
    print(web_bağlantıları)# Bağlantıları yazdır
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
        try: # Belirtilen XPath ile div elementini bul
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
            b_tags = div_element.find_elements(By.TAG_NAME,"b")# Bu div elementinin altındaki b tag'larını bul
            for b_tag in b_tags:#   Her bir b tagı için işlem yap
                a_tag = b_tag.find_element(By.TAG_NAME,"a")# b tag'ının altındaki a tag'ını bul    
                mail_adresi = a_tag.get_attribute("href").split(":")[1]# a tag'ının içerdiği mail adresini al        
                if check_at_symbol(mail_adresi): # Mail adresini listeye ekle
                    mail_adresleri.append(mail_adresi)
                    print(mail_adresi)
                else:
                    print(f"{mail_adresi} ==> Mail Adresi Bulunamadi")                
        hatalimi = False
getMail()
print(mail_adresleri)# Mail adreslerini yazdır
import pandas as pd
def listToDataFrame(_mailList):
    df1 = pd.DataFrame(_mailList, columns=["Mail Listesi"])
    print(df1)
    with pd.ExcelWriter(r"mailListesi.xlsx") as writer:
        df1.to_excel(writer, sheet_name="mailList")
listToDataFrame(mail_adresleri)
browser.quit()
