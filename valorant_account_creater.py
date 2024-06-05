import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains

def generate_random_email():
    domains = ["gmail.com"]
    letters = string.ascii_lowercase
    random_email = ''.join(random.choice(letters) for i in range(10)) + '@' + random.choice(domains)
    return random_email

def generate_random_nickname():
    letters = string.ascii_lowercase
    random_nickname = ''.join(random.choice(letters) for i in range(12))
    return random_nickname

def generate_random_password():
    characters = string.ascii_letters + string.digits
    random_password = ''.join(random.choice(characters) for i in range(10))
    return random_password

def save_email_and_nickname_to_file(email, nickname, password, filename="accounts.txt"):
    with open(filename, 'a') as file:
        file.write(f"Email: {email},{nickname}:{password}\n")

def click_element():
    # WebDriver'ı başlat (Chrome tarayıcı)
    driver = webdriver.Chrome()

    try:
        # Hedef web sitesine git
        driver.get("https://playvalorant.com/tr-tr/")

        # İlk elementin yüklenmesini bekle ve tıkla (Giriş butonu)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="GM-top_"]/div[2]/div/a'))
        )
        element.click()
        
        # İkinci elementin yüklenmesini bekle ve tıkla (Takımına Katıl butonu)
        element1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div[2]/div[1]/a'))
        )
        element1.click()

        # Üçüncü elementin yüklenmesini bekle ve e-posta alanına rastgele bir e-posta gir
        element2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div[1]/div/input'))
        )
        email = generate_random_email()
        element2.send_keys(email)

        # E-posta adresini kaydet
        nickname = generate_random_nickname()
        password = generate_random_password()
        save_email_and_nickname_to_file(email, nickname, password)

        # Devam et butonuna tıkla
        devam_et_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[3]/button'))
        )
        devam_et_butonu.click()
        

        # Doğum günü alanına rastgele bir gün değeri gir
        birth_day = str(random.randint(1, 29))  
        element4 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[1]/input'))
        )
        element4.send_keys(birth_day)

        # Doğum ayı alanına rastgele bir ay değeri gir
        birth_month = str(random.randint(1, 12))  
        element5 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[2]/input'))
        )
        element5.send_keys(birth_month)

        # Doğum yılı alanına rastgele bir yıl değeri gir
        birth_year = str(random.randint(1970, 2005))  
        element6 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[3]/input'))
        )
        element6.send_keys(birth_year)

        # Kaydet butonuna tıkla
        kaydet_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[3]/button'))
        )
        kaydet_butonu.click()

        # Nickname alanına rastgele bir nickname değeri gir
        element7 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div/input'))
        )
        element7.send_keys(nickname)

        # Kaydet butonuna tıkla
        kaydet_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[3]/button'))
        )
        kaydet_butonu.click()

        # Şifre alanlarına rastgele bir şifre değeri gir

        element8_1 = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[1]/div/input'))
        )
        element8_2 = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[2]/div/div[3]/div/input'))
        ) 

        element8_1.send_keys(password)
        element8_2.send_keys(password)      
    
        # Devam et butonuna tıkla
        devam_et_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[3]/button'))
        )
        devam_et_butonu.click()

        wait = WebDriverWait(driver, 10)
        checkbox = wait.until(EC.presence_of_element_located((By.ID, "tos-checkbox")))

        # JavaScript kullanarak 'disabled' niteliğini kaldır
        driver.execute_script("arguments[0].removeAttribute('disabled')", checkbox)
        checkbox.click()

        devam_et_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/main/div[3]/div/div[2]/div/div[3]/button'))
        )
        devam_et_butonu.click()


        WebDriverWait(driver, 60).until(
        lambda wd: driver.execute_script("return document.readyState") == 'complete',
        "Page taking too long to load"
        )  

        time.sleep(10)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

    finally:
        # Tarayıcıyı kapat
        driver.quit()

if __name__ == "__main__":
    click_element()