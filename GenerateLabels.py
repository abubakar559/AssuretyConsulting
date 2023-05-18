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
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane4_header"]').click()
        time.sleep(5) #left menu Generate     

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane4_content_lbGenerateLabels"]').click()
        time.sleep(2) #Labels selection
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_chkGenerateLabelforIMtB"]').click()
        time.sleep(2) #check box first 
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_chkGenerateLabelforIMcB"]').click()
        time.sleep(2) #check box second 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnPrintLables"]').click()
        time.sleep(5) #Generate Button 


        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        # time.sleep(5) #close modify drop down menu
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        # time.sleep(5) #open export menu drop down 
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_trPostalOneExport"]/td').click()
        # time.sleep(10) #selecting Postal One! 


        
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