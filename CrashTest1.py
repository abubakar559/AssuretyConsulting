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
        self.driver.get('http://10.51.100.26/AIMSPlus79/')
        self.driver.maximize_window()

    def login(self):
        pass


    def test_login(self):

        driver=self.driver

        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').send_keys("Abubakar")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtPassword"]').send_keys("Abubakar123")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_lbLogin"]').click()
        time.sleep(10)
        #login steps till now 

        driver.find_element_by_xpath('//*[@id="lblImportJob"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob_wrap"]').click()
        
        #driver.find_element_by_id('ctl00_masterContentPlaceHolder_flUpdJob').click()
       # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob"]').click()

        time.sleep(4) #waiting for window popup to open
        pyautogui.write(r"C:\Users\RockY\Downloads\STD-FLT- Bundle on Pallet.zip") #path of File
        pyautogui.press('enter')
        time.sleep(5)        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnSave"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnRefresh"]').click()
        time.sleep(10)

        while True:
    # find the element that contains the status you're interested in (e.g. the second row, third column)
            status_element = driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobStatus_ctl02_lblStatus"]')
    
    # get the text of the status element
            status = status_element.text
    
    # check if the status is 'Passed'
            if status == 'Successful':
                print('Status has passed!')
                break
            elif status == 'Failed':
                print('Failed because failed to upload file') 
                driver.quit()  #if status failed then quit the automation      
    # if the status isn't 'Passed', refresh the page and wait for a bit before checking again
            driver.refresh()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnRefresh"]').click()
            time.sleep(5)
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobStatus_ctl02_hlnkSuccessMAID"]').click()
        time.sleep(5) #going to first job uploaded
        #Testing crash 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2) #Modify
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
        time.sleep(5) #Manage CSM
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_gdvwCSM_ctl03_chkCheck_freezeitem"]').click()
        time.sleep(2)# check box
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_gdvwCSM_ctl04_chkCheck_freezeitem"]').click()
        time.sleep(2) # check box
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddSiblings"]').click()
        time.sleep(3) #add sibling 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_chkGenerateBarcode"]').click()
        time.sleep(2) #check box on new pop up 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbCreateSiblings"]').click()
        time.sleep(3) #addbtn
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbviewOk"]').click()
        time.sleep(3) #close btn

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbPallets"]').click()
        time.sleep(2) #uncheck Pallets
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbIncludeLooseTrays"]').click()
        time.sleep(2) #uncheck Loose trays
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbSiblings"]').click()
        time.sleep(2) #Check sibilings
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_gdvwCSM_ctl02_chkCheck_freezeitem"]').click()
        time.sleep(2) #selecting first job 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbLabelManag"]').click()
        time.sleep(3) #Label select
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5)

        try:

            status_element = driver.find_element_by_xpath('//*[@id="lblAppError"]')
    
            # get the text of the status element
            status = status_element.text
    
            # check if the status is 'Passed'
            if status == 'Application Error':
                
                
                print('*******Crash on siblings Label************')
                print('*******Crash on siblings Label************')
                print('*******Crash on siblings Label************')
                print('*******Crash on siblings Label************')
                print('*******Crash on siblings Label************')
                print('*******Crash on siblings Label************')
                
                driver.find_element_by_xpath('//*[@id="hypGoBack"]').click()
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
                time.sleep(2)

                


            
        except NoSuchElementException:
            
            print("No Crash on siblings Label")
            print("No Crash on siblings Label")
            print("No Crash on siblings Label")


        #Unpalletization Sibling Crash Test
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbPallets"]').click()
        time.sleep(2) #uncheck Pallets
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbIncludeLooseTrays"]').click()
        time.sleep(2) #uncheck Loose trays
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbSiblings"]').click()
        time.sleep(2) #Check sibilings
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_gdvwCSM_ctl02_chkCheck_freezeitem"]').click()
        time.sleep(2) #selecting first job 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbUnpalletizeTrays"]').click()
        time.sleep(3)

        try:

            status_element = driver.find_element_by_xpath('//*[@id="lblAppError"]')
    
            # get the text of the status element
            status = status_element.text
    
            # check if the status is 'Passed'
            if status == 'Application Error':
                
                
                print('*******Crash on siblings Unpalletization************')
                print('*******Crash on siblings Unpalletization************')
                print('*******Crash on siblings Unpalletization************')
                print('*******Crash on siblings Unpalletization************')
                print('*******Crash on siblings Unpalletization************')
                print('*******Crash on siblings Unpalletization************')




                driver.find_element_by_xpath('//*[@id="hypGoBack"]').click()
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
                time.sleep(2)

                


            
        except NoSuchElementException:
            
            print("No Crash on siblings Unpalletization")
            print("No Crash on siblings Unpalletization")
            print("No Crash on siblings Unpalletization")



        #Seamless Acceptance Validation Crash Testing
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)#not for the smoke test only for this script 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccPaneSeamlessAcceptance_header"]').click()
        time.sleep(2) #Seamless Acceptance 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccPaneSeamlessAcceptance_content_lnkBtnSeamlessAcceptanceValidation"]').click()
        time.sleep(2) #Validation
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkbtnReValidate"]').click
        time.sleep(2) #Re-validate btn
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane2_header"]').click()
        time.sleep(2) #change of menu (Validations) 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane2_content_lbValidationSummary"]').click()
        time.sleep(2) #Job Validation 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_chkSeamlessValidation"]').click()
        time.sleep(2) #check box selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbValidate"]').click()
        time.sleep(2)  




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