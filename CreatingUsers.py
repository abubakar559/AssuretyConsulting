from tkinter import *
from turtle import clear
import pyautogui
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import unittest
from pathlib import Path
import pickle
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert




class Instagram(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://10.51.100.26/AIMSPlusCorefact/')
        self.driver.maximize_window()

    def login(self):
        pass


    def test_login(self):

        driver=self.driver

        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').send_keys("administrator")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').send_keys("abcd1234")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lbLogin"]').click()
        time.sleep(10)
        #login steps till now



        driver.find_element_by_xpath('//*[@id="ctl00_imgConfig"]').click() 
        time.sleep(3) #settings 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageUser"]').click()
        time.sleep(2) #manage users
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(2) #add users 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserName"]').send_keys("Abubakar123")
        time.sleep(1) #UserID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPassword"]').send_keys("Abubakar123")
        time.sleep(1)#Password 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtConfirmPassword"]').send_keys("Abubakar123")
        time.sleep(1)#Confirm Password
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtFirstName"]').send_keys("Abubakar")
        time.sleep(1) #FirstName
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastName"]').send_keys("Ijaz")
        time.sleep(1) #LastName            
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbBranchesSelectAll"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]').click()
        time.sleep(2)#selecting branch 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]/option[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(3) #saveBtn
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageUser"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(2) #add users 
        

        #Adding Second users 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserName"]').send_keys("Ashhar123")
        time.sleep(1) #UserID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPassword"]').send_keys("Ashhar123")
        time.sleep(1)#Password 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtConfirmPassword"]').send_keys("Ashhar123")
        time.sleep(1)#Confirm Password
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtFirstName"]').send_keys("Ashhar")
        time.sleep(1) #FirstName
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastName"]').send_keys("Husain")
        time.sleep(1) #LastName            
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbBranchesSelectAll"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]').click()
        time.sleep(2)#selecting branch 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]/option[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(3) #saveBtn
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageUser"]').click()
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(2) #add users 


        #Adding thrid user

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserName"]').send_keys("kamal123")
        time.sleep(1) #UserID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPassword"]').send_keys("kamal123")
        time.sleep(1)#Password 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtConfirmPassword"]').send_keys("kamal123")
        time.sleep(1)#Confirm Password
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtFirstName"]').send_keys("kamal")
        time.sleep(1) #FirstName
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastName"]').send_keys("khan")
        time.sleep(1) #LastName            
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlUserRole"]/option[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbBranchesSelectAll"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]').click()
        time.sleep(2)#selecting branch 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlSelectedBranches"]/option[3]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(5) #saveBtn
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageUser"]').click()
        time.sleep(5)








    def tearDown(self):
        time.sleep(5)
        self.driver.close()

    # def find_element(self):
    #     try:
    #         self.driver.find_element_by_class_name('_6CZji')
    #         return True
    #     except NoSuchElementException:
    #         return False

if __name__ == '__main__':
    unittest.main()