from selenium import webdriver

driver = webdriver.Firefox() #opens Firefox browser
driver.get("http://lakshmimaduri.herokuapp.com") #Navigates to webpage lakshmimaduri.herokuapp.com
assert driver.title == 'Lakshmi Maduri\'s Portfolio'
driver.close()
