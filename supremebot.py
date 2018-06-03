from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



item_name = "Bless Hooded Sweatshirt"
item_color = "Black"
item_category = "sweatshirts"
item_size = "Large"



item_name_colors = []
on_color = False
item_links = dict()
link = ""
sizes = []


driver = webdriver.Chrome(executable_path = "/usr/local/selenium/webdriver/chrome/chromedriver")
driver.get("http://www.supremenewyork.com/shop/all/" + item_category)

item_name_colors = driver.find_elements_by_class_name('name-link')


item = ""
color = ""

for element in item_name_colors:


	if not on_color:

		item = element.text
		
		if not item in item_links:

			item_links[item] = []

		on_color = True

	else:

		color = element.text
		link = element.get_attribute('href')
		tup = (color,link)

		item_links[item].append(tup)

		on_color = False


for elem in item_links[item_name]:

	if(elem[0] == item_color):
		link = elem[1]
		break

driver.get(link)

sizes = Select(driver.find_element_by_id('s'))


for o in sizes.options:
	if o.text == item_size:
		sizes.select_by_visible_text(item_size)
		break

driver.find_element_by_name('commit').click()
time.sleep(0.05)
driver.get("http://www.supremenewyork.com/checkout")


order_bill_name = driver.find_element_by_xpath("//input[@id='order_billing_name']")
order_bill_name.send_keys("Test Tester")
order_email = driver.find_element_by_xpath("//input[@id='order_email']")
order_email.send_keys("test@gmail.com")
order_tele = driver.find_element_by_xpath("//input[@id='order_tel']")
order_tele.send_keys("240-555-1234")
order_address = driver.find_element_by_xpath("//input[@id='bo']")
order_address.send_keys("1234 Testing Street")
#order_bill_city = driver.find_element_by_xpath("//input[@id='order_billing_city']")
#order_bill_city.send_keys("Testingburg")
order_bill_zip = driver.find_element_by_xpath("//input[@id='order_billing_zip']")
order_bill_zip.send_keys("20879")
order_cnb = driver.find_element_by_xpath("//input[@id='nnaerb']")
order_cnb.send_keys("1358135853971789")
Select(driver.find_element_by_xpath("//select[@id='credit_card_month']")).select_by_visible_text("09")
Select(driver.find_element_by_xpath("//select[@id='credit_card_year']")).select_by_visible_text("2019")




#driver.quit()