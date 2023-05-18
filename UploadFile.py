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

        driver.find_element_by_xpath('//*[@id="lblImportJob"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob_wrap"]').click()
        
        #driver.find_element_by_id('ctl00_masterContentPlaceHolder_flUpdJob').click()
       # driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_flUpdJob"]').click()

        time.sleep(4) #waiting for window popup to open
        pyautogui.write(r"C:\Users\RockY\Downloads\Bundel on Pallet-Presort-STD-FLT.zip") #path of File
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
                driver.quit()       
    # if the status isn't 'Passed', refresh the page and wait for a bit before checking again
            driver.refresh()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ImgBtnRefresh"]').click()
            time.sleep(5)

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_gdvwJobStatus_ctl02_hlnkSuccessMAID"]').click()
        time.sleep(5) #going to first job uploaded

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2) #modify
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnHdrEdit"]').click()
        time.sleep(5) #Header
        
        #driver.find_element_by_xpath('').click()
        #driver.find_element_by_xpath('').click()

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtJobNameTitleandIssue"]').send_keys("STDFLTS Bundle")
        time.sleep(2) 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5) # button to save Header name 

        #CMSEdit started 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
        time.sleep(5)   #ManageCSM selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectAllContainers"]').click()
        time.sleep(5) #SelectAllContainers

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbBatchEdit"]').click()
        time.sleep(5) #CSM Edit

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbcsmPresortLabelingListEffectiveDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cecsmPresortLabelingListEffectiveDate_today"]').click()
        time.sleep(2) #Presort Labeling List Effective Date: todays date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbcsmPresortCityStatePublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender3_today"]').click()
        time.sleep(2) #Presort City State Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbPresortZoneChartMatrixPublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender5_today"]').click()
        time.sleep(2) #Presort Zone Chart Matrix Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbLastUsedMailDirectionPublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender7_today"]').click()
        time.sleep(2) #Last Used Mail Direction Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbLastUsedLabelingListEffectiveDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cetbLastUsedLabelingListEffectiveDate_today"]').click()
        time.sleep(2) #Last Used Labeling List Effective Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbLastUsedCityStatePublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender4_today"]').click()
        time.sleep(2) #Last Used City State Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbcsmLastUsedZoneChartMatrixPublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender6_today"]').click()
        time.sleep(2) #Last Used Zone Chart Matrix Publication Date  


        html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(5) 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtActualContainerShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtActualContainerShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #Actual Container Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledPickUpDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledPickUpDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Pick Up Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledInHomeDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledInHomeDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled In-Home Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledInductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledInductionDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Induction Start Date:

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledInductionEndDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledInductionEndDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Induction End Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtActualinductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtActualinductionDate_CalendarExtender_today"]').click()
        time.sleep(2) #Actual Induction Date



        html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPostageStatementMailingDate"]').click()
        time.sleep(2) #Postage Statement Mailing Date to todays date
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPostageStatementMailingDate_CalendarExtender_today"]').click()
        time.sleep(2) #Postage Statement Mailing Date to todays date

        html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailStartDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailStartDateCalendarExtender_today"]').click()
        time.sleep(2) #Referenceable Mail Start Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailEndDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailEndDateCalendarExtender_today"]').click()
        time.sleep(2) #Referenceable Mail End Date       
        
       


        html = driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5) #click Save Button        





        #CMS Edit done Next Post and log info

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
        time.sleep(5)   #ManageCSM selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectAllContainers"]').click()
        time.sleep(5) #SelectAllContainers


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbPostageAndLogisticsInformation"]').click()
        time.sleep(5) #Post&LogInfo
        
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbScheduledInHomeDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender2_today"]').click()
        time.sleep(2) #Scheduled In-Home Date

        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbActualInductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender4_today"]').click()
        time.sleep(2) #Actual Induction Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledInductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbScheduledInductionDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Induction Start Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbScheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_tbScheduledShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ImgBtnDateUSPS"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender3_today"]').click()
        time.sleep(2) #Postage Statement Mailing Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbActualContainerShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender5_today"]').click()
        time.sleep(2) #Actual Container Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtbScheduledPickUpDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_CalendarExtender6_today"]').click()
        time.sleep(2) #Scheduled Pick up Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbUpdateTransportationInformation"]').click()
        time.sleep(5) #saving settings


        #PostandLogInfo done next transport


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
        time.sleep(5)   #ManageCSM selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectAllContainers"]').click()
        time.sleep(5) #SelectAllContainers

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbTransportManag"]').click()
        time.sleep(5) #transport Selected 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledInHomeDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledInHomeDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled In-Home Date
        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPostageStatementMailingDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPostageStatementMailingDate_CalendarExtender_today"]').click()
        time.sleep(2) #Postage Statement Mailing Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledShipDate_CalendarExtender_today"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(2)

        #Transport Done next Schedule 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lnkBtnManageCSM"]').click()
        time.sleep(5)   #ManageCSM selection 
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbSelectAllContainers"]').click()
        time.sleep(5) #SelectAllContainers


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbScheduleManag"]').click()
        time.sleep(5) #Select Schedule

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_cbPalletized"]').click()
        time.sleep(2) #selecting the check box (Apply changes to palletize tray)


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtInhomeDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtInhomeDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled In-Home Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPresortLabListEffectDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPresortLabListEffectDate_CalendarExtender_today"]').click()
        time.sleep(2) #PreSort Labeling List Effect Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPresortCityStatePublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPresortCityStatePublicationDate_CalendarExtender_today"]').click()
        time.sleep(2) #Presort City State Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtLastUsedLabelingListEffectiveDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastUsedLabelingListEffectiveDate_CalendarExtender_today"]').click()
        time.sleep(2) #Last Used Labeling List Effective Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtLastUserCityStatePublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastUserCityStatePublicationDate_CalendarExtender_today"]').click()
        time.sleep(2) #Last Used City State Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtSheduledInductionStartDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSheduledInductionStartDate_CalendarExtender_today"]').click()
        time.sleep(2) #scheduled Induction Start Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtSheduledInductionEndDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSheduledInductionEndDate_CalendarExtender_today"]').click()
        time.sleep(2) #scheduled Induction Start Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtSheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSheduledShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #scheduled Induction End Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtSheduledShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtSheduledShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #scheduled Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailStartDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtReferenceableMailStartDate_CalendarExtender_today"]').click()
        time.sleep(2) #Referenceable Mail Start Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtReferenceableMailEndDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtReferenceableMailEndDate_CalendarExtender_today"]').click()
        time.sleep(2) #Referenceable Mail End Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPresortZoneChartMatrixPublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPresortZoneChartMatrixPublicationDate_CalendarExtender_today"]').click()
        time.sleep(2) #Presort Zone Chart Matrix Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtLastUserMailDirectionPublicationDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtLastUserMailDirectionPublicationDate_CalendarExtender_today"]').click()
        time.sleep(2) #Last Used Mail Direction Publication Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtActualContainerShipDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtActualContainerShipDate_CalendarExtender_today"]').click()
        time.sleep(2) #Actual Container Ship Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtScheduledPickUpDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtScheduledPickUpDate_CalendarExtender_today"]').click()
        time.sleep(2) #Scheduled Pick Up Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtActualInductionDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtActualInductionDate_CalendarExtender_today"]').click()
        time.sleep(2) #Actual Induction Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPostageStatementMailingDate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPostageStatementMailingDate_CalendarExtender_today"]').click()
        time.sleep(2) #Postage Statement Mailing Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5) #saving

        #Schedule Done Next MPU & CPT Info

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lbMPUCPTInfo"]').click()
        time.sleep(5)   #MPU and CPT info selection 
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailPieceUnitName"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailPieceUnitName"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailPieceUnitName"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailPieceUnitName"]').send_keys("Automation")
        time.sleep(2) # backspacing and entering name (MPU Name)


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMPUDescription"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMPUDescription"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMPUDescription"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMPUDescription"]').send_keys("Automation")
        time.sleep(2) # backspacing and entering name (MPU description)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentWeight"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentWeight"]').send_keys("9")
        time.sleep(2) #Component weight


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentDescription"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentDescription"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentDescription"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtComponentDescription"]').send_keys("Automation")
        time.sleep(2) # backspacing and entering name (Component description)
        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtPeriodicalIssueDate"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPeriodicalIssueDate_CalendarExtender_today"]').click()
        time.sleep(2) #Periodical Issue Date

        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlCCR"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlCCR"]/option[14]').click()
        time.sleep(2) #Selecting Characteristic 
        

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlCharachteristicType"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlCharachteristicType"]/option[2]').click()
        time.sleep(2) #Selecting Characteristic Type       

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbCCRAdd"]').click()
        time.sleep(2) #Add Button 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(2)        
        alert = Alert(driver)
        alert.accept()
        time.sleep(2)

        #MPU and CPT info done next SEG & Permit Info


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lbMailAnyWhere"]').click()
        time.sleep(5)   #SEG and Permit info selection 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtAutomationCodingDate"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtAutomationCodingDate_CalendarExtender_today"]').click()
        time.sleep(2) #Automation Coding Date

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ibtxtMoveUpdateDate"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMoveUpdateDate_CalendarExtender_today"]').click()
        time.sleep(2) #Move Update Date


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailFacilityID"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailFacilityID"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailFacilityID"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtMailFacilityID"]').send_keys("5092424")
        time.sleep(2) # eDoc Sender CRID

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4"]').send_keys("543219876")
        time.sleep(2) #Permit Zip+4

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlMailOwnersLclPermitRefNumOrIntlBillNumType"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlMailOwnersLclPermitRefNumOrIntlBillNumType"]/option[4]').click()
        time.sleep(2) # Mail Owners Lcl. Permit Ref.No /Int'l Bill No. Type

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnSave"]').click()
        time.sleep(5) #saving    

        #task left for add additional MPA ID
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lbAddAdditionalMPAID"]').click()
        time.sleep(5)

        #driver.find_element_by_xpath('').click()
        #driver.find_element_by_xpath('').send_keys(Keys.CONTROL,'a')
        #driver.find_element_by_xpath('').send_keys(Keys.BACKSPACE)
        #driver.find_element_by_xpath('').send_keys("543219876")
        #time.sleep(2) #Permit Zip+4
        
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitNumber"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitNumber"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitNumber"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitNumber"]').send_keys("65")
        time.sleep(2) #Permit Number


        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4MPAID"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4MPAID"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4MPAID"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtPermitZipPlus4MPAID"]').send_keys("543219876")
        time.sleep(2) #Permit Zip+4

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCRIDofMailOwner"]').click()
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCRIDofMailOwner"]').send_keys(Keys.CONTROL,'a')
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCRIDofMailOwner"]').send_keys(Keys.BACKSPACE)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_txtCRIDofMailOwner"]').send_keys("5092424")
        time.sleep(2) #CRID of mail owner

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlPostagePaymentOptionMPAID"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlPostagePaymentOptionMPAID"]/option[5]').click()
        time.sleep(2) #Postage Payment Option

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlPostagePaymentMethod"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlPostagePaymentMethod"]/option[2]').click()
        time.sleep(2) #Postage Payment Method

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlMailOwnersLclPermitRefNumOrIntlBillNumTypeMPAID"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_ddlMailOwnersLclPermitRefNumOrIntlBillNumTypeMPAID"]/option[4]').click()
        time.sleep(2) 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_btnAdd"]').click()
        time.sleep(2) #Add button 

        #SEG and permit info done next Add Siblings 

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

        #Add siblings done, next Re-CalcuPieces

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_content_lbSyncJobReport"]').click()
        time.sleep(2) #Selection Re-CalcuPieces 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_imgBtnAutoCorrect"]').click()
        time.sleep(5) #re-calculate count btn 

        try:
            
            element = driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnKbtnUpdateWeights"]')

            # Fixing error 
            element.click()

        except NoSuchElementException:
            
            print("Element not found. Continuing with the ongoing script...")

             
        time.sleep(5)


        #Re-Calcu done next Generate Labels

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane3_header"]').click()
        time.sleep(2)
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

        #Generate Label done next generate postage 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane4_content_lnkBtnNewPostage"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl04_chkbxSelectContainer_freezeitem"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl07_chkbxSelectContainer_freezeitem"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl10_chkbxSelectContainer_freezeitem"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_grdvwSelectedContainers_ctl13_chkbxSelectContainer_freezeitem"]').click()
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkBtnPostageView"]').click()
        time.sleep(2)

        # Generate Postage done, next is copy job 

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane6_header"]').click()
        time.sleep(2) #left menu to More     

        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_LeftMenuJobDetail1_AccordionPane6_content_LbCopyJob"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="ctl00_ctl00_masterContentPlaceHolder_masterContentPlaceHolder_lnkbtnCreateACopy"]').click()
        time.sleep(5)



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