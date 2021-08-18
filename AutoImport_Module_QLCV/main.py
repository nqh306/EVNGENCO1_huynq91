from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import xlrd
from xlrd import sheet
from selenium.common.exceptions import NoSuchElementException     
browser = webdriver.Chrome('/Users/quanghuy/Code/ChromeDriver_Selenium/chromedriver')

def check_exists_by_xpath(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        print('tim thay')
    except NoSuchElementException:
        print('khong tim thay')
        return False
    return True

browser.get('http://doffice.evngenco1.vn/login')

username = browser.find_element_by_id('mat-input-0')
username.send_keys('evngenco1\huynq91')

password = browser.find_element_by_id('mat-input-1')
password.send_keys('dOffice@123')
password.send_keys(Keys.RETURN)

wait = WebDriverWait(browser, 10)
wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='main']/toolbar/mat-toolbar/div/div[2]/input")))

browser.get('http://doffice.evngenco1.vn/congviec/cv-import-cv')

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mat-select-0']/div")))
browser.find_element_by_xpath("//*[@id='mat-select-0']/div").click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mat-option-1']")))
browser.find_element_by_xpath("//*[@id='mat-option-1']").click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mat-tab-content-3-0']/div/div/mat-card/mat-card-content/div[3]/div/button")))
browser.find_element_by_xpath("//*[@id='mat-tab-content-0-0']/div/div/mat-card/mat-card-content/div[3]/div/button").click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mat-input-8']")))
browser.find_element_by_xpath("//*[@id='mat-input-8']").send_keys("100/NQ-HĐTV")
browser.find_element_by_xpath("//*[@id='mat-tab-content-1-0']/div/div/div/div/button").click()



