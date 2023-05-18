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