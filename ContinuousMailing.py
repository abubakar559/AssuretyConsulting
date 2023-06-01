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
        self.driver.get('http://10.51.100.26/AIMSQA/Default.aspx')
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


    #     driver.find_element_by_xpath('//*[@id="lblImportJob"]').click()
    #     time.sleep(5)
    #     driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob_wrap"]').click()
        
    #     #driver.find_element_by_id('ctl00_masterContentPlaceHolder_flUpdJob').click()
    #    # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob"]').click()

    #     time.sleep(4) #waiting for window popup to open
    #     pyautogui.write(r"C:\Users\RockY\Downloads\STD-FLT- Bundle on Pallet.zip") #path of File
    #     pyautogui.press('enter')
    #     time.sleep(5)        
    #     driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnSave"]').click()
    #     time.sleep(5)
    #     driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnRefresh"]').click()
    #     time.sleep(10)

    #     while True:
    # # find the element that contains the status you're interested in (e.g. the second row, third column)
    #         status_element = driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobStatus_ctl02_lblStatus"]')
    
    # # get the text of the status element
    #         status = status_element.text
    
    # # check if the status is 'Passed'
    #         if status == 'Successful':
    #             print('Status has passed!')
    #             break
    #         elif status == 'Failed':
    #             print('Failed because failed to upload file') 
    #             driver.quit()  #if status failed then quit the automation      
    # # if the status isn't 'Passed', refresh the page and wait for a bit before checking again
    #         driver.refresh()
    #         time.sleep(5)
    #         driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnRefresh"]').click()
    #         time.sleep(5)


        #Create and apply Template to job
         
        driver.find_element_by_xpath('//*[@id="lblMaildatTemplate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMyTemplate")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for local Template")
        time.sleep(2) #Template Description 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[2]').click()
        time.sleep(4) #first hdr 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[3]').click()
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("5092424")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 

        

        #adding seg eDoc



        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[3]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[10]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("5092424")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
       
             
       
        #Second Task done proceding to the third task MPA Crid of owner  

        

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("5092424")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
        
        #third task done starting forth task MPA Cried of preparer


 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[2]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("5092424")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
        
             
        #forth task done, starting fifth task MPA Permit Number



        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[12]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("65")
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 


        #fifth task done, Sixth task starting MPA Permit ZIP +4



        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[13]').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("201911535")
        time.sleep(2)
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 


        #ZIP+4 done proceding to Mailer ID of Mail owner 

    
 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[7]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("106848")


        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
    
        #Mailer ID of mail owner done next Mailer ID of mail preparer

    

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)  
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[8]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("106848") 
        time.sleep(2)     

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
    
        #MPA Mailer ID of Mail Preparer done, next is CPT Mailer ID of Mail Owner Final step 

        
 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[6]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[23]').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("106848")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5) 



        driver.find_element_by_xpath('').click()







        driver.find_element_by_xpath('//*[@id="ctl00_hljobs"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl02_chkCheck"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkbtnApplyTemplate"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlEditingTemplate"]/option[9]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkBtnApply"]').click()
        time.sleep(2)        


        driver.find_element_by_xpath('').click()

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobs_ctl06_chkCheck"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkbtnApplyTemplate"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlEditingTemplate"]/option[9]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lnkBtnApply"]').click()
        time.sleep(2)        











        driver.find_element_by_xpath('//*[@id="lblPODashboard"]').click()
        time.sleep(2) #Dashboard
        driver.find_element_by_xpath('//*[@id="__tab_ctl00_masterContentPlaceHolder_POTransactionTabContainer_UploadedTabPanel"]').click()
        time.sleep(2) #upload tab
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlBranch"]/option[4]').click()
        time.sleep(2) #selection of branch 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlBranch"]/option[4]').click()
        time.sleep(3) #Selecting specific branch
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_POTransactionTabContainer_UploadedTabPanel_gdvwPODashboard_ctl02_lblJobID"]').click()
        time.sleep(3) #selecting job with pass status 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_header"]').click()
        time.sleep(2) #selecting export
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane5_content_LinkButton2"]').click()
        time.sleep(5) #selecting continuous mailing

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectionRanges"]').click()
        time.sleep(2) #selecting range
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDStartRangeSelection"]').send_keys("000040")
        time.sleep(2) #range 1
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDEndRangeSelection"]').send_keys("000041")
        time.sleep(2) #range 2
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddRangeSelection"]').click()
        time.sleep(2) #add range btn 

        
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDStartRangeSelection"]').send_keys("000010")
        # time.sleep(2) #range 1
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtcsmIDEndRangeSelection"]').send_keys("000014")
        # time.sleep(2) #range 2
        # driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddRangeSelection"]').click()
        # time.sleep(2) #add range btn 


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbRangeSelectionOk"]').click()
        time.sleep(2) #ok btn
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbEdit"]').click()
        time.sleep(2) #Edit

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
        time.sleep(2)# save btn






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