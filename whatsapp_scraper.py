from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import csv
import os


def scrape(driver):
    
    with open('whatsapp_chats.csv', 'w+', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['chats', 'from',  'text', 'time'])
        
        driver.get("https://web.whatsapp.com/")
        chat = ''

        for i in range(5):
            for j in driver.find_elements("xpath", '//*[@class="_21S-L"]'):
                try:
                    j.click()
                except:
                    pass
                chat = j.text

                chat_len1 = -1
                chat_len2 = len(driver.find_elements("xpath", '//*[@class="copyable-text"]'))
                time.sleep(5)
                
                s = 0
                while chat_len1!=chat_len2 and s!=3:
                    chat_len1 = chat_len2
                    try:
                        driver.find_element("xpath", '//*[@class="copyable-text"]').click()
                    except:
                        pass
                    chat_len2 = len(driver.find_elements("xpath", '//*[@class="copyable-text"]'))
                    if chat_len1 == chat_len2:
                        time.sleep(5)
                        s += 1
                    else:
                        s = 0

                for k in driver.find_elements("xpath", '//*[@class="copyable-text"]'):
                    writer.writerow([chat, k.get_attribute("data-pre-plain-text").split('] ')[1][:-2], k.text, k.get_attribute("data-pre-plain-text").split('] ')[0][1:]])
                    
            if chat: break
            time.sleep(10)
            
            
if __name__=='__main__':
    load_dotenv()
    CHROME_PROFILE = os.getenv('CHROME_PROFILE')
    EDGE_PROFILE = os.getenv('EDGE_PROFILE')
    browser = os.getenv('browser')
    
    
    if browser=='chrome':
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={CHROME_PROFILE}")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser=='edge':
        options = webdriver.EdgeOptions()
        options.add_argument(f"user-data-dir={EDGE_PROFILE}")
        driver = webdriver.Edge(options = options)
    
    scrape(driver)
    driver.quit()