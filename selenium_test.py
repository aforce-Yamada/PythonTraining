from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://a-force.biz/")

driver.find_element_by_id("button-area").click() #チャットボットクリック
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_id("tweet").send_keys("福利厚生")
driver.find_element_by_id("send_btn").send_keys(Keys.ENTER)

time.sleep(3)

list = driver.find_elements_by_class_name("row")[2].text

time.sleep(3)

print(list)

driver.close()