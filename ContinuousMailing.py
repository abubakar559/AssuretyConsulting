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


        driver.find_element_by_xpath('//*[@id="lblImportJob"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob_wrap"]').click()
        
        #driver.find_element_by_id('ctl00_masterContentPlaceHolder_flUpdJob').click()
       # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob"]').click()

        time.sleep(4) #waiting for window popup to open
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


        #Applying Template 

        driver.find_element_by_xpath('//*[@id="ctl00_hljobs"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl02_chkCheck"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkbtnApplyTemplate"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkBtnApply"]').click()
        time.sleep(3)        

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl02_lblhdrJobNameTitleAndIssue"]').click()
        time.sleep(3)#job Selection
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)#modify
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnHdrEdit"]').click()
        time.sleep(3)
        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys("Cont.Mail Test")
        time.sleep(2) #Header Info
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(3) #Save
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        time.sleep(2)#export
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_LinkButton2"]').click()
        time.sleep(2)#cont mailing 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_chkprovidefilename"]').click()
        time.sleep(2)#checkBox
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtNewFileName"]').send_keys("TestCont1")
        time.sleep(2)#name
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnSendToPreliminary"]').click()
        time.sleep(2)

        

        #wait here 

        driver.find_element_by_xpath('//*[@id="lblPODashboard"]').click()
        time.sleep(2) #Dashboard
        driver.find_element_by_xpath('//*[@id="__tab_ctl00_masterContentPlaceHolder_POTransactionTabContainer_UploadedTabPanel"]').click()
        time.sleep(2) #upload tab
        # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlBranch"]/option[4]').click()
        # time.sleep(2) #selection of branch 
        # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlBranch"]/option[4]').click()
        # time.sleep(3) #Selecting specific branch
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_POTransactionTabContainer_UploadedTabPanel_gdvwPODashboard_ctl02_lblJobID"]').click()
        time.sleep(3) #selecting job with pass status 
        
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        time.sleep(2) #selecting export
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_LinkButton2"]').click()
        time.sleep(5) #selecting continuous mailing

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectionRanges"]').click()
        time.sleep(5) #selecting range //*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDStartRangeSelection"]
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDStartRangeSelection"]').send_keys("000001")
        time.sleep(2) #range 1 time
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDEndRangeSelection"]').send_keys("000004")
        time.sleep(2) #range 2
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddRangeSelection"]').click()
        time.sleep(5) #add range btn 

        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDStartRangeSelection"]').send_keys("000007")
        time.sleep(2) #range 1
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDEndRangeSelection"]').send_keys("000015")
        time.sleep(2) #range 2
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddRangeSelection"]').click()
        time.sleep(5) #add range btn 


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbRangeSelectionOk"]').click()
        time.sleep(5) #ok btn  time change
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbEdit"]').click()
        time.sleep(5) #Edit

        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgStartDate1"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender5_today"]').click()
        time.sleep(2) #dates
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgStartDate2"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender6_today"]').click()
        time.sleep(2) #dates

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgScheduledInHomeDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender7_today"]').click()
        time.sleep(2) #dates 3


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgActualInductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender8_today"]').click()
        time.sleep(2) #4 dates


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgScheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender9_today"]').click()
        time.sleep(2) # 5 dates


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgActualContainerShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender10_today"]').click()
        time.sleep(2) #6 dates




        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgScheduledPickUpDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender11_today"]').click()
        time.sleep(2) #7 dates
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5)# save btn


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl01_chkbxSelectAllContainers"]').click()
        time.sleep(2) #Check box selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl01_chkbxSelectAllContainers"]').click()
        time.sleep(2) #Check box selection
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl01_chkbxSelectAllContainers"]').click()
        time.sleep(2) #Check box selection
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl01_chkbxSelectAllContainers"]').click()
        time.sleep(2) #Check box selection        
        





        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl02_chkbxSelectContainer"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl03_chkbxSelectContainer"]').click()
        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)          
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnPostageView"]').click()
        time.sleep(3)#generate
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)         
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnCommit"]').click()
        time.sleep(3)#save

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl07_chkbxSelectContainer"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl11_chkbxSelectContainer"]').click()
        time.sleep(3)
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)  
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnPostageView"]').click()
        time.sleep(3)#generate
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)         
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnCommit"]').click()
        time.sleep(3)#save    //*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnCommit"]

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwCalculatePostageStatement_ctl02_chkbxPostageContainer"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwCalculatePostageStatement_ctl03_chkbxPostageContainer"]').click()
        time.sleep(5)

        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)  



        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlTransactionType"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlTransactionType"]/option[2]').click()
        time.sleep(1)  
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnSend"]').click()
        time.sleep(2) #export

        driver.find_element_by_xpath('//*[@id="lblPODashboard"]').click()
        time.sleep(5) #DashBoard 



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