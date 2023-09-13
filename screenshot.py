from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import base64

 
def get_screenshot(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path=r'C:/WebDriver/bin/chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    driver.execute_script('document.body.style.zoom = "60%";')
    driver.save_screenshot('screenshot.png')
    driver.quit()

    with open('screenshot.png','rb') as fp:
        return(base64.b64encode(fp.read()))
    