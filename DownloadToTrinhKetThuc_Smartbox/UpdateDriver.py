import zipfile

from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.chrome.options import Options

downloads_url = "https://chromedriver.chromium.org/downloads"
basic_downloads_path = 'https://chromedriver.storage.googleapis.com/{0}chromedriver_{1}.zip'
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# os='win32'
os = 'mac64'
driver_executable = '/Users/quanghuy/chromedriver/chromedriver'


def check_browser():
    driver = None
    try:
        driver = webdriver.Chrome(executable_path=driver_executable, options=options)
        driver.get('https://www.google.com/')
        return True
    except SessionNotCreatedException:
        return False
    finally:
        if driver is not None:
            driver.close()


def download_zip(_url):
    r = requests.get(_url, allow_redirects=True)
    open('./driver/chrome.zip', 'wb').write(r.content)
    with zipfile.ZipFile('./driver/chrome.zip') as z:
        z.extractall('./driver/')


def get_versions():
    html = requests.get(downloads_url).text
    soup = BeautifulSoup(html, "html.parser")
    versions_a = soup.find_all('a', href=re.compile('https://chromedriver.storage.googleapis.com/index.html\\?path='))
    versions = []
    for a in versions_a:
        version = a['href'].split('=', 1)[1]
        versions.append(version)
    return versions

print('====> Checking current Chrome compatibility.')
compatible = check_browser()
print('====> It is ' + ('Compatible.' if compatible else 'Not Compatible.'))
if not compatible:
    print('====> Trying to find alternate versions.')
    versions = get_versions()
    print(f'==> ({len(versions)}) found.')
    for version in versions:
        url = basic_downloads_path.format(version, os)
        download_zip(url)
        compatible = check_browser()
        print(f'==> Trying version {version} - {"Compatible" if compatible else "Not Compatible"}')
        if compatible:
            break
    if not compatible:
        raise Exception('Unable to upgrade chrome version. Probably you are using very old chrome version.'
                        'Please update chrome and try again!!')



