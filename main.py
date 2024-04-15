from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

EMAIL = 'mirna.oyola@hotmail.com'
PASSWORD = os.environ.get('PASSWORD_FB')

class WhatsappBot:
    def __init__(self): 
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--disable-notifications") #evitar notificaciones de bloqueo de ubicación
        self.chrome_options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=self.chrome_options)       
        

    def get_videos(self):
        global url_actual
        self.driver.get('https://www.youtube.com/results?search_query=evangelio+de+hoy')   
        self.driver.maximize_window()

        time.sleep(2)
        
        find_video = self.driver.find_element(By.XPATH, value='//*[@id="video-title"]/yt-formatted-string')
        find_video.click()
        time.sleep(2)

        url_actual = self.driver.current_url

    def send_video(self):
        self.driver.get('https://m.facebook.com/login/?locale=es_LA') 
        self.actions = ActionChains(self.driver)   
        self.driver.maximize_window()

        time.sleep(2)        

        email = self.driver.find_element(By.XPATH, value='//*[@id="m_login_email"]')
        email.click()
        email.send_keys(EMAIL)

        password = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[3]/form/div[4]/div[3]/div/div/div/div[1]/div/input')
        password.click()
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(4)
        print('yes')

        accept = self.driver.find_element(By.CLASS_NAME, value='_2pis')
        print('yes')
        accept.click()
        time.sleep(3)

        self.actions.move_by_offset(1200, 30).click().perform()
        time.sleep(2)
        print('time')
        # self.actions.move_by_offset(1020, 250).click().perform()

        jaimee = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[1]/div')
        jaimee.click()
        time.sleep(2)

        text = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[4]/div[2]/div/div[1]/div[1]/p')
        text.click()
        text.send_keys(url_actual)
        text.send_keys(Keys.ENTER)

        time.sleep(2)
        self.driver.quit()

while True:
    bot = WhatsappBot()
    bot.get_videos()
    bot.send_video()
    time.sleep(86400) #enviar cada dia