from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--incognito')
chrome_opt.add_argument("--disable-notifications")
driver = webdriver.Chrome('D:\\Study\\Automation\\chromedriver_win32\\chromedriver.exe',chrome_options=chrome_opt)
driver.maximize_window
driver.get('http://prueba.undostres.com.mx')
def waitForElementReady(locator,location):
        try:
            delay = 10 #seconds
            myElem = WebDriverWait(driver, delay).until(ec.element_to_be_clickable((locator, location)))
            print("Element is ready!")
            return myElem
        except TimeoutException:
            print("Element not found!")

operator_name = waitForElementReady(By.NAME,'operator')
operator_name.click()
option_operator = waitForElementReady(By.XPATH,'//*[@data-name="telcel"]')
option_operator.click()
mobile_number = waitForElementReady(By.NAME, 'mobile')
mobile_number.send_keys('5523261151')
recharge_amount = waitForElementReady(By.NAME,'amount')
recharge_amount.click()
option_amount = waitForElementReady(By.XPATH,'//*[@data-name="10"]')
option_amount.click()
next_button = waitForElementReady(By.XPATH,'//*[contains(text(),"Siguiente")]')
next_button.click()
driver.implicitly_wait(10)
url = driver.current_url
print(url)
if url == 'https://prueba.undostres.com.mx/payment.php':
    print("Url is correct")
else:
    print("Url is not correct")
card_name = waitForElementReady(By.XPATH,'(//*[@name="cardname"])[2]')
card_name.send_keys('Test')
card_number = waitForElementReady(By.XPATH,'(//*[@name="cardno"])[2]')
card_number.send_keys('4111111111111111')
exp_month = waitForElementReady(By.XPATH,'(//*[@name="expmonth"])[2]')
exp_month.send_keys('11')
exp_year = waitForElementReady(By.XPATH,'(//*[@name="expyear"])[2]')
exp_year.send_keys('2025')
cvv_no = waitForElementReady(By.XPATH,'(//*[@name="cvvno"])[2]')
cvv_no.send_keys('111')
email = waitForElementReady(By.XPATH,'(//*[@name="txtEmail"])')
email.send_keys('test@test.com')
submit = waitForElementReady(By.XPATH,'(//*[@name="formsubmit"])')
submit.click()

user_email = waitForElementReady(By.XPATH,'(//*[@name="email"])')
user_email.send_keys('marze.zr@gmail.com')
password = waitForElementReady(By.XPATH,'(//*[@name="password"])')
password.send_keys('123456')
captcha_frame = waitForElementReady(By.XPATH,'//iframe[@role="presentation"]')
driver.switch_to.frame(captcha_frame)
captcha_click = waitForElementReady(By.XPATH,'//span[@id="recaptcha-anchor"]')
captcha_click.click()
driver.switch_to.default_content()
login_button = waitForElementReady(By.XPATH,'//button[@name="loginbtn"]')
login_button.click()

time.sleep(10)
url_success = driver.current_url
print(url_success)
if url_success == 'https://prueba.undostres.com.mx/confirmation/success':
    print("Recharge is successful")
else:
    print("Recharge is NOT successful")