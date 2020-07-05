import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import subprocess

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
        
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        film = self.textbox.text()
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

        try:
            element=driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div[2]/div[4]/div/h3/div/table/tbody/tr[3]/td[2]')
        except NoSuchElementException:
            pass
        try:
            element=driver.find_element_by_xpath('//*[@id="content"]/div[4]/div[1]/div[2]/div[4]/div/h3/div/table/tbody/tr[3]/td[3]')
        except NoSuchElementException:
            try:
                element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[3]/a[1]/img")
            except NoSuchElementException:
                try:
                    element=driver.find_element_by_xpath("/html/body/div/div/div/main/article/div/p[4]/a[1]/img")
                except NoSuchElementException:
                    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())