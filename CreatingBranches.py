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
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageBranch"]').click()
        time.sleep(2)   #Manage Branches 

        #this step required 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(5) #plus add home 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtBranchName"]').send_keys("Abubakar")
        time.sleep(1) #branch Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserLicenseCode"]').send_keys("AB12")
        time.sleep(1)#user licence code
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerCorpID"]').send_keys("123456789962")
        time.sleep(1)#Scheduler Corp ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerID"]').send_keys("12345")
        time.sleep(1)#Scheduler ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCrid"]').send_keys("5092424")
        time.sleep(1)#CRID

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOUserName"]').send_keys("Abubakar123")
        time.sleep(1)#PostalOne!® User Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOPassword"]').send_keys("Abubakar123")
        time.sleep(1)#PostalOne!® Password:
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAddMID"]').click()
        time.sleep(5)#Add Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtmidMID"]').send_keys("106848")
        time.sleep(2) #Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbtnAddMidDetails"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(5) #save btn 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageBranch"]').click()
        time.sleep(3)


        #this step required 1 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(5) #plus add home 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtBranchName"]').send_keys("Ashhar")
        time.sleep(1) #branch Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserLicenseCode"]').send_keys("AW10")
        time.sleep(1)#user licence code
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerCorpID"]').send_keys("12589")
        time.sleep(1)#Scheduler Corp ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerID"]').send_keys("1995")
        time.sleep(1)#Scheduler ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCrid"]').send_keys("96325874")
        time.sleep(1)#CRID

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOUserName"]').send_keys("Ashhar123")
        time.sleep(1)#PostalOne!® User Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOPassword"]').send_keys("Ashhar123")
        time.sleep(1)#PostalOne!® Password:
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAddMID"]').click()
        time.sleep(5)#Add Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtmidMID"]').send_keys("199507")
        time.sleep(2) #Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbtnAddMidDetails"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(5) #save btn 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageBranch"]').click()
        time.sleep(3)




        #this step required 2 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAdd"]').click()
        time.sleep(5) #plus add home 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtBranchName"]').send_keys("KAM")
        time.sleep(1) #branch Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtUserLicenseCode"]').send_keys("KAM1")
        time.sleep(1)#user licence code
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerCorpID"]').send_keys("125899")
        time.sleep(1)#Scheduler Corp ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSchedulerID"]').send_keys("12549")
        time.sleep(1)#Scheduler ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCrid"]').send_keys("258741")
        time.sleep(1)#CRID

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOUserName"]').send_keys("kamal123")
        time.sleep(1)#PostalOne!® User Name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbPOPassword"]').send_keys("kamal123")
        time.sleep(1)#PostalOne!® Password:
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnAddMID"]').click()
        time.sleep(5)#Add Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtmidMID"]').send_keys("564759")
        time.sleep(2) #Mid
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbtnAddMidDetails"]').click()
        time.sleep(3) #Mid Save BTN
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(5) #save btn 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuSettings_AccordionPane1_content_lbManageBranch"]').click()
        time.sleep(3)





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