from selenium.webdriver.common.by import By
import basePages
from locators.locators import Table
from selenium import webdriver

class TablePages(basePages.BasePage):
    def getColumnNum(self):
        table = self.driver.find_element(*Table.elemTable)
        tr = table.find_elements_by_tag_name("tr")
        colNum=(len(tr[0].find_elements_by_tag_name("td")))
        print("Column number is: ")
        print(colNum)

    def getRowNum(self):
        table = self.driver.find_element(*Table.elemTable)
        rowNum=(len(table.find_elements_by_tag_name("tr")))
        print("Row number is:")
        print(rowNum)



    def selectRadioAccFirstname(self,firstname):
        table = self.driver.find_element(*Table.elemTable)
        print "\nEntire Table :\n***\n" + table.text + "\n***\n"

        for i,tr in enumerate(table.find_elements_by_tag_name("tr")):
            #print "TR is :" + tr.text

            for td in tr.find_elements_by_tag_name("td"): ### Search for TD tag
                #print(td.text) ### Print cell value

                if(td.text==firstname):
                    xPath_elemRadio="//table[@id='VIPs']/tbody/tr[{0}]/td[1]/input[@type='radio']".format(i+1)
                    elemRadio=self.driver.find_element(By.XPATH,xPath_elemRadio)

                    print tr.text
                    elemRadio.click()
                    print firstname+" has been selected."
                    #break
                    return # In for cycle, use "return" is better than "break"

            #else:
                #print ("No TD. May be TH row OR Empty Row")