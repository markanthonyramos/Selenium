from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

starting_link = "https://drive.google.com/drive/folders/0B4RrFJ0LG5iyfjFpaHlFZkJmUFZ3dTRGZnFaYy1sOGVrWnM2UzYwbGJ2STlELTRfdUVjMDQ?resourcekey=0-HEAO9CwtQSKtM6UK0jO5dg"

username = "ramos.482897160011@depedqc.ph"
password = "Fish_cakes_apple_pies_474"

subject = 8
month = 1
week = 1
name_of_files = []

driver = webdriver.Firefox(executable_path="./geckodriver.exe")
action = ActionChains(driver)

driver.get(starting_link)

input_username = driver.find_element_by_xpath('//*[@id="identifierId"]')
input_username.send_keys(username)

next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]')
next_button.click()

time.sleep(3)

password_username = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password_username.send_keys(password)

sign_in = driver.find_element_by_xpath('//*[@id="passwordNext"]')
sign_in.click()

time.sleep(5)

subject_folders = driver.find_elements_by_class_name("jGNTYb")

for sindex, svalue in enumerate(subject_folders, start=1):
	if sindex == subject:
		action.double_click(svalue).perform()
		break

time.sleep(3)

month_folders = driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[2]/div/div/div[1]/div/div/div[3]/div/div/div/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[1]/div/div/div")

# for index, value in enumerate(month_folders, start=1):
# 	if index == month:
action.double_click(month_folders).perform()

# time.sleep(3)

# week_folders = driver.find_elements_by_class_name("jGNTYb")

# for index, value in enumerate(week_folders, start=1):
# 	if index == week:
# 		action.double_click(value).perform()

# time.sleep(3)

# performance_folder = driver.find_elements_by_class_name("jGNTYb")

# for index, value in enumerate(performance_folder, start=1):
# 	if index == 1:
# 		action.double_click(value).perform()

# written_folder = driver.find_elements_by_class_name("jGNTYb")

# for index, value in enumerate(written_folder, start=1):
# 	if index == 2:
# 		print(value)
# 		action.double_click(value).perform()