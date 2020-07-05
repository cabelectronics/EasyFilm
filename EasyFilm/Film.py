from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import subprocess

print("¿Que pelicula o serie quieres descargar?")
film = input("> ")
time.sleep(1)

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.drriver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.divxtotal.la/")

search_bar = driver.find_element_by_id('s')
search_bar.click()
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(Keys.BACK_SPACE)
search_bar.send_keys(film)
search_bar.send_keys(Keys.ENTER)

select_film = driver.find_element_by_xpath('//*[@id="center"]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[1]/a')
select_film.click()
select_film.click()

download1_button = driver.find_element_by_xpath('//*[@id="opcion2_th"]/a')
download1_button.click()

download2_button = driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div[2]/div[4]/div/h3/a/img')
download2_button.click()

download3_button = driver.find_element_by_xpath('//*[@id="opcion2_th"]/a')
download3_button.click()

f = open(os.path.expanduser("~/Downloads"))

print("Your Download finished successfully")




