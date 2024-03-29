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
        self.driver.get('http://10.51.100.26/AIMSPlus80/')
        self.driver.maximize_window()

    def login(self):
        pass


    def test_login(self):

        driver=self.driver

        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').send_keys("Abubakar123")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').send_keys("Abubakar123")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lbLogin"]').click()
        time.sleep(10)
        #login steps till now 



        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl02_lblhdrJobNameTitleAndIssue"]').click()
        time.sleep(5)
        #selecting first job 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane4_header"]').click()
        time.sleep(5) #left menu Generate     

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane4_content_lbGenerateBarcode"]').click()
        time.sleep(2) #Barcode
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMcbTabPanel_ctl02_gdvwFilteredContainers_ctl01_chkSelectAllCheckboxes_Copy"]').click()
        time.sleep(2) #selectAll
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMcbTabPanel_ctl02_lblResequenceBarcode"]').click()
        time.sleep(2) #Generate Barcode
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMcbTabPanel_ctl02_lnkBtnReSequence"]').click()
        time.sleep(3) #First part done 

        driver.find_element_by_xpath('//*[@id="__tab_ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMtbTabPanel"]').click()
        time.sleep(3) #Second Tab
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMtbTabPanel_ctl02_gdvwFilteredContainers_ctl01_chkSelectAllCheckboxes_Copy"]').click()
        time.sleep(2) #Select All  
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMtbTabPanel_ctl02_lblResequenceBarcode"]').click()
        time.sleep(2) #Resequence Barcode 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMtbTabPanel_ctl02_lnkBtnReSequence"]').click()
        time.sleep(3) #button submission 


        #Third tab resequence IMB
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMbTabPanel_IMbPanel"]').click()
        time.sleep(5) #selecting thrid tab
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMbTabPanel_ctl02_lbSelectAllMailPieces"]').click()
        time.sleep(2) #select all
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMbTabPanel_ctl02_lbResequenceBarcode"]').click()
        time.sleep(2) #resequence options
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_BarcodeTabContainer_IMbTabPanel_ctl02_lnkBtnReSequence"]').click()
        time.sleep(5) #final btn 

        
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        # time.sleep(5) #close modify drop down menu
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        # time.sleep(5) #open export menu drop down 
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_trPostalOneExport"]/td').click()
        # time.sleep(10) #selecting Postal One! 


        
        a = ActionChains(driver)
        m= driver.find_element_by_xpath('//*[@id="ctl00_ctl00_Image3"]')
        a.move_to_element(m).perform() 
        time.sleep(1)       
        

        a = ActionChains(driver)
        m= driver.find_element_by_xpath('//*[@id="ctl00_ctl00_btnSignout"]')
        a.move_to_element(m).perform()
        
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_btnSignout"]').click() 
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