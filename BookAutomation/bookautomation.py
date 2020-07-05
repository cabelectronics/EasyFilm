from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


print('Que libro quieres?')
book = input("> ")
time.sleep(1)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")

driver = webdriver.Chrome(chrome_options = options)
driver.get('https://zonadelibrosxyz.com')

text_area = driver.find_element_by_id('searchform-1')
text_area.send_keys(book)
text_area.send_keys(Keys.ENTER)

your_book = driver.find_element_by_xpath('/html/body/div/div/div/main/article[1]/header/h2/a')
your_book.click()

book_acces = driver.find_element_by_xpath('//*[@id="passster_password"]')
book_acces.send_keys('librosgratisxyz')

book_submit = driver.find_element_by_xpath('//*[@id="passster_submit"]')
book_submit.click()

two = NoSuchElementException

try:
    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[1]/a[1]/img")
except NoSuchElementException:
    pass
try:
    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[2]/a[1]/img")
except NoSuchElementException:
    try:
        element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[3]/a[1]/img")
    except NoSuchElementException:
        try:
            element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[4]/a[1]/img")
        except NoSuchElementException:
            try:
                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[5]/a[1]/img")
            except NoSuchElementException:
                try:
                    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[6]/a[1]/img")
                except NoSuchElementException:
                    try:
                        element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[7]/a[1]/img")
                    except NoSuchElementException:
                        try:
                            element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[8]/a[1]/img")
                        except NoSuchElementException:
                            try:
                                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[9]/a[1]/img")
                            except NoSuchElementException:
                                try:
                                    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[10]/a[1]/img")
                                except NoSuchElementException:
                                    try:
                                        element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[11]/a[1]/img")
                                    except NoSuchElementException:
                                        try:
                                            element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[12]/a[1]/img")
                                        except NoSuchElementException:
                                            try:
                                                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[13]/a[1]/img")
                                            except NoSuchElementException:
                                                try:
                                                    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[14]/a[1]/img")
                                                except NoSuchElementException:
                                                    try:
                                                        element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[15]/a[1]/img")
                                                    except NoSuchElementException:
                                                        try:
                                                            element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[16]/a[1]/img")
                                                        except NoSuchElementException:
                                                            try:
                                                                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[17]/a[1]/img")
                                                            except NoSuchElementException:
                                                                try:
                                                                    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[18]/a[1]/img")
                                                                except NoSuchElementException:
                                                                    try:
                                                                        element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[19]/a[1]/img")
                                                                    except NoSuchElementException:
                                                                        try:
                                                                            element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[20]/a[1]/img")
                                                                        except NoSuchElementException:
                                                                            try:
                                                                                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[21]/a[1]/img")
                                                                            except NoSuchElementException:
                                                                                pass
element.click()

book_download = driver.find_element_by_id('download-url')
book_download.click()
