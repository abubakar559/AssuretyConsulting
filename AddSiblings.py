from tkinter import *
from turtle import clear
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
        self.driver.get('http://aims.assuretyconsulting.com/AIMSPlus/Default.aspx')

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



        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl02_lblhdrJobNameTitleAndIssue"]').click()
        time.sleep(5)
        #selecting first job 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(5) #left menu Modify     
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lbSibling"]').click()
        time.sleep(5) # Add siblings selection 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_Image1"]').click()
        time.sleep(2) #search Filter

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_ddlContainerType"]').click()
        time.sleep(1) 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_ddlContainerType"]/option[2]').click()
        time.sleep(1) #container Type   

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_imgSearch"]').click()
        time.sleep(2) #Search button 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_gdvwFilteredContainers_ctl04_chkCheck"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_gdvwFilteredContainers_ctl02_chkCheck"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_gdvwFilteredContainers_ctl07_chkCheck"]').click()
        time.sleep(1) #selecting multiple Selection Checkbox 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_btnAddSiblings"]').click()
        time.sleep(5) # Adding sibbling button 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_chkGenerateBarcode"]').click()
        time.sleep(2) #check box selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_lbCreateSiblings"]').click()
        time.sleep(5) #Saving btn

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_AddSiblingContainer_AddSiblingPanel_ctl01_lbviewOk"]').click()
        time.sleep(2) # Close Btn 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(5) #close modify drop down menu
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        time.sleep(5) #open export menu drop down 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_trPostalOneExport"]/td').click()
        time.sleep(10) #selecting Postal One! 


        
        a = ActionChains(driver)
        m= driver.find_element_by_xpath('//*[@id="ctl00_Image3"]')
        a.move_to_element(m).perform() 
        time.sleep(1)       
        

        a = ActionChains(driver)
        m= driver.find_element_by_xpath('//*[@id="ctl00_btnSignout"]')
        a.move_to_element(m).perform()
        
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_btnSignout"]').click() 
        time.sleep(5) #log out step   




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