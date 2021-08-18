from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import xlrd
from xlrd import sheet
from selenium.common.exceptions import NoSuchElementException     
browser = webdriver.Chrome('/Users/quanghuy/chromedriver/chromedriver')

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

browser.get('http://doffice.evngenco1.vn/smartbox/sm-kt-chuyenvanthu')

wb = xlrd.open_workbook("/Users/quanghuy/Google Drive/BanTH_BaoCaoTuan/Extract Data DOffice/Data_Smartbox_For_Module_DownloadFile.xls")
sheet = wb.sheet_by_index(0)
sheet.cell_value(0,0)

totrinh = sheet.cell_value(2,0)

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='ds-to-trinh']/div/mat-toolbar/div[1]/div[3]/button")))
browser.find_element_by_xpath("//*[@id='ds-to-trinh']/div/mat-toolbar/div[1]/div[3]/button").click()

wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='mat-input-0']")))
browser.find_element_by_xpath("//*[@id='mat-input-0']").send_keys(totrinh)
browser.find_element_by_xpath("//*[@id='mat-input-1']").send_keys("01/01/2021")
browser.find_element_by_xpath("//*[@id='mat-input-2']").send_keys("31/12/2021")
browser.find_element_by_xpath("//*[@id='cdk-overlay-1']/div/div/div/div[2]/div/button[2]").click()

element_str = "//*[@id='ds-to-trinh']/div/div/mat-sidenav-container/mat-sidenav/div/section/sm-ds-ttrinh-left/div/table/tbody/tr/td/div[1]/span[1]"
if check_exists_by_xpath("//*[@id='ds-to-trinh']/div/div/mat-sidenav-container/mat-sidenav/div/section/sm-ds-ttrinh-left/div/table/tbody/tr/td") == True:
    totrinh_needtocheck = browser.find_element_by_xpath(element_str).text
    print(totrinh_needtocheck)
    if totrinh == totrinh_needtocheck:
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='file-manager']/div[2]/div/img")))
        browser.find_element_by_xpath("//*[@id='file-manager']/div[2]/div/img").click()
        wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='cdk-overlay-2']/div/div/button[3]")))
        browser.find_element_by_xpath("//*[@id='cdk-overlay-2']/div/div/button[3]").click()













   
