'''
Created on 6 Oct 2020

@author: FMORASSU
'''

from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import datetime

#op = webdriver.ChromeOptions()
#op.add_argument("user-data-dir=C:\\Users\\FMORASSU\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Profile 1")
#op.add_argument("--disable-bookmarks")
#op.add_argument("--disable-notifications")
#op.add_argument("--start-maximized")
#op.add_argument("--ignore-certificate-errors")

#driver = webdriver.Chrome(options=op)

def selectDate(d):
    currentDate = datetime.now()
    print(currentDate.strftime('%d/%m/%Y'))
    dt = datetime.strptime(d, '%d/%m/%Y')
    Year=dt.year
    day=dt.day
    month=dt.strftime("%B")
    print(Year)
    print(day)
    print(month)
    
    desirMY=str(month)+" " +str(Year)
    print(desirMY)
    
    while True:
        #dispMY = driver.find_element_by_xpath("//html/body/div[3]/div[1]/table/thead/tr[2]/th[2]").text
        dispMY = driver.find_element_by_css_selector("th.datepicker-switch").text
        print(dispMY)
        if(desirMY==dispMY):
            driver.find_element_by_xpath("//td[text()= '"+str(day)+"']").click()
            break
        else:
            if(dt>currentDate):
                driver.find_element_by_xpath("//html/body/div[3]/div[1]/table/thead/tr[2]/th[3").click()
            elif(dt<currentDate):
                driver.find_element_by_xpath("//html/body/div[3]/div[1]/table/thead/tr[2]/th[1]").click()
                 
browseroption = "Chrome"
webdriver.driver = None


if browseroption=='Chrome':
    driver = webdriver.Chrome()
elif browseroption=='Firefox':
    driver = webdriver.Firefox()
elif browseroption=='Edge':
    driver = webdriver.Edge()
elif browseroption=='IE':
    driver = webdriver.Ie()
else:
    print("No browser specified")


driver.maximize_window()    
driver.get("https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html")
driver.implicitly_wait(5)


driver.find_element_by_xpath("//html/body/div[2]/div/div[2]/div[1]/div/div[2]/div/div/span/i").click()
selectDate("21/09/2020")
