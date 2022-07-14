import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InstagramFollowers:
    def __init__(self, profile, username, password):
        self.chrome_driver_past = "/Users/killsamurai/Development/chromedriver"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_past)
        self.list = 2
        self.user = profile
        self.username = username
        self.password = password
        self.login()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/?")
        time.sleep(3)
        self.user_name_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.password_input = self.driver.find_elements(By.CSS_SELECTOR, '[aria-label="Password"]')
        time.sleep(1)
        self.user_name_input.click()
        self.user_name_input.send_keys(self.username)
        self.password_input[0].click()
        self.password_input[0].send_keys(self.password)
        self.password_input[0].send_keys(Keys.ENTER)
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{self.user}/")
        self.find_followers()

    def find_followers(self):
        time.sleep(5)

        self.amount_of_followers = int(self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div/span').text)

        self.followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, "followers")
        self.followers.click()

        time.sleep(5)

        dialog = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')

        print(self.amount_of_followers)
        print()

        for item in range(int(self.amount_of_followers/12 + 1)):
            self.follow()
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", dialog)
            time.sleep(4)

    def follow(self):
        time.sleep(5)
        for i in range(12):
            try:
                self.follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{self.list}]/div/div[3]/button')
                self.follow_button.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                self.cancel_button = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
                self.cancel_button.click()
            except selenium.common.exceptions.NoSuchElementException:
                self.follow_button = self.driver.find_element(By.XPATH, f'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[{self.list}]/div/div[2]/button')
                self.follow_button.click()
            finally:
                self.list += 1
                time.sleep(3)
