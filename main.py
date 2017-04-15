from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from bs4 import BeautifulSoup
import time

url = "https://web.spaggiari.eu/home/app/default/login.php"

if __name__ == "__main__":
	with open("profile.txt", "r") as input_file:
		username = input_file.readline().replace("\n", "")
		password = input_file.readline().replace("\n", "")

	# print(username, password)

	browser = webdriver.PhantomJS()
	
	browser.get(url)

	# print(browser.page_source)

	username_slot = browser.find_element_by_id("login")
	password_slot = browser.find_element_by_id("password")

	username_slot.send_keys(username)
	password_slot.send_keys(password)

	browser.find_element_by_class_name("check-auth").click()

	time.sleep(1)

	# print(browser.page_source)

	browser.get("https://web.spaggiari.eu/cvv/app/default/genitori_note.php?classe_id=406595&studente_id=2807426")

	time.sleep(1)

	# print(browser.page_source)

	soup = BeautifulSoup(browser.page_source, "html.parser")

	table = soup.find_all("table", {"class" : "griglia_tab", "id" : "data_table_2"})[0]

	print(table.text)


