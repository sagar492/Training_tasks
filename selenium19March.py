from selenium import webdriver
import time
DRIVER_PATH = r'C:/Users/7000026200/Downloads/chromedriver_win32/chromedriver.exe'
driver=webdriver.Chrome(DRIVER_PATH)
driver.implicitly_wait(20)

driver.get(url="https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.find_element_by_xpath("//button[@type='submit'][1]").click()
driver.find_element_by_xpath("//li[@class='menu-list header-icon-menu'][2]").click()
win_handles=driver.window_handles

driver.switch_to.window(win_handles[1])

driver.find_element_by_id("departFrom").send_keys('Bangalore')

driver.find_element_by_xpath("//ul[@id='ui-id-1']/li//div[text()='Bangalore']").click()

driver.find_element_by_id("goingTo").send_keys('Chennai')

driver.find_element_by_xpath("//ul[@id='ui-id-2']/li//div[text()='Chennai']").click()

driver.find_element_by_id("departDate").click()
driver.find_element_by_xpath("(//table[@class='ui-datepicker-calendar']/tbody//tr[4]/td/a)[1]").click()

driver.find_element_by_xpath("//button[text()='Search Bus ']").click()
driver.find_element_by_xpath("//button[text()='Select Seat'][1]").click()
time.sleep(2)
driver.find_element_by_xpath("(//div//span[@class='Sleeper_V' ])[9]").click()
time.sleep(2)
driver.find_element_by_xpath("(//div//input[@name='bordTime' and @type='radio'])[1]").click()
time.sleep(2)
driver.find_element_by_xpath("(//input[@name='debordTime'])[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-md btn-primary btn-radius yellow-gradient']").click()
time.sleep(2)
driver.back()  ##used to move to the previous page in the same tab

