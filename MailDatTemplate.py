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

        # Selecting Mail Dat template 
        driver.find_element_by_xpath('//*[@id="lblMaildatTemplate"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationHDR")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for hdr")
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)
        

        #adding seg eDoc

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationSEGeDoc")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for SEGeDoc")
        time.sleep(2) #Template Description 
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)        
       
       
       
        #Second Task done proceding to the third task 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPACriedofMailOwner")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA CRID of mail owner")
        time.sleep(2) #Template Description 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("5092424")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)        

        #third task done starting forth task 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPACriedofPreparer")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA CRID of Preparer")
        time.sleep(2) #Template Description 
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)   
        
             
        #forth task done, starting fifth task 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPApermitnumber")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA Permit Number")
        time.sleep(2) #Template Description 
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)  


        #fifth task done, Sixth task starting Permit ZIP +4

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPApermitZip+4")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA Permit ZIP +4")
        time.sleep(2) #Template Description 
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)  


        #ZIP+4 done proceding to Mailer ID of Mail owner 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPAmailIDofMailOwner")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA Mailer ID of Mail Owner")
        time.sleep(2) #Template Description 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_cblstVersions_2"]').click()
        time.sleep(2) #Radio button 
        
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFile"]/option[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_ddlMailDatFields"]/option[7]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_tbMailDatFieldValue"]').send_keys("106848")


        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbtnAddMailDatField"]').click()
        time.sleep(3) #Add Field 
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)  

        #Mailer ID of mail owner done next Mailer ID of mail preparer

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationMPAmailIDofMailPreparer")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for MPA Mailer ID of Mail Preparer")
        time.sleep(2) #Template Description 
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
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_lbSaveTemplate"]').click()
        time.sleep(5)  

        #MPA Mailer ID of Mail Preparer done, next is CPT Mailer ID of Mail Owner 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_LKBNewTemplate"]').click()
        time.sleep(5) #Add button 

        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateName"]').send_keys("AutomationCPTmailerIDofMailOwner")
        time.sleep(2) #Template Name    
        driver.find_element_by_xpath('//*[@id="ctl00_masterContentPlaceHolder_txtTemplateDescription"]').send_keys("This task is being automated for CPT Mailer ID of Mail Owner")
        time.sleep(2) #Template Description 
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