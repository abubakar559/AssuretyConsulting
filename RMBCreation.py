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
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtUserID"]').send_keys("Abubakar123")
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

        time.sleep(4) #waiting for window popup to open C:\Users\abubakar.ijaz\Downloads
        pyautogui.write(r"C:\Users\abubakar.ijaz\Downloads\STD-FLT- Bundle on Pallet.zip") #path of File
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
        time.sleep(5) # going to first job uploaded

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)#modify
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnHdrEdit"]').click()
        time.sleep(3) #header
        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys("RMB Creation")
        time.sleep(2) #Header Info
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(3) #Save
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)#modify 



        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccPaneManageCampaigns_header"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccPaneManageCampaigns_content_lnkbtnRMS"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtRMSID"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtRMSID"]').send_keys("88888888")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCampaignTitle"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCampaignTitle"]').send_keys("testingggggggggggggggggggggggggggggggggg")
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCampaignMailOwnerCRID"]').send_keys("5092424")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtDisplayName"]').send_keys("Testingggggggggggggggggggggggg")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCampaignCode"]').send_keys("9000000000000000000000000000000000000000")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccPaneManageCampaigns_content_lnkbtnRMR"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_rdCPT"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_gdvwFilteredComponent_ctl01_chkSelectAllCheckboxesComponent"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_lblAddRMRComponent"]').click()
        time.sleep(5) #Generate RMR
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_chkRMRContentTypeA"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_chkRMRContentTypeB"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_chkRMRContentTypeC"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_txtRMRContentTypeARMRValue"]').send_keys("tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_txtRMRContentTypeBRMRValue"]').send_keys("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_txtRMRContentTypeCRMRValue"]').send_keys("nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_RMRTabContainer_NotLinkedTabPanel_ctl02_lnkBtnAddRMR"]').click()
        time.sleep(3) #Saving RMR details 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_pane1_header"]').click()
        time.sleep(2) #Summary info
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_pane1_content_LinkButton3"]').click()
        time.sleep(2) #Job details
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_HyperLinkRMR"]').click()
        time.sleep(2) #RMR Record opening 
        









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


