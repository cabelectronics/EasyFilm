import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#import pyautogui
 
import time
import os
import subprocess
import sys

Window.size = (500, 200)

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter Film name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.add_widget(self.inside)

        self.submit = Button(text="Search", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

        

    def pressed(self, instance):
        film = self.name.text

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
        
        time.sleep(1)

        #pyautogui.scroll(-10)
        #pyautogui.moveTo(565, 581)
        #pyautogui.click()


        

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()