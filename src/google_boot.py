import os, dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleBot:
	"""Responsible for parsing scraped data and writing them to a Google form"""

	form_link = os.getenv("GOOGLE_FORM_LINK")
	driver_path = os.getenv("DRIVER_PATH")
	prefs = {"intl.accept_languages": "en,en_US"}

	def __init__(self):
		self.options = uc.ChromeOptions()
		self.options.add_argument("--no-sandbox")
		self.options.add_argument("--disable-dev-shm-usage")
		self.options.add_argument("--start-maximized")
		self.options.add_argument("--force-dark-mode")
		self.options.add_argument("--enable-features=WebContentsForceDark")
		self.options.add_argument("--lang=en-US,en")
		self.options.add_argument("--window-size=1920,1080")
		self.options.add_experimental_option("prefs", self.prefs)
		self.options.binary_location = "/usr/bin/google-chrome"
		self.driver = uc.Chrome(options=self.options, driver_executable_path=self.driver_path, use_subprocess=True)
		self.driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {
			"headers": {
				"Accept-Language": "en-US,en"
			}
		})

	def write_data(self, data: list[tuple]):
		"""Writes scraped data to google form"""
		wait = WebDriverWait(self.driver, poll_frequency=1, timeout=10)
		#refreshing
		self.driver.delete_all_cookies()
		self.driver.get(self.form_link)

		#IMPORTANT AFTER EVERY ITERATION, CODE MUST FIND THE ELEMENT, OTHERWISE IT BECOME STALE!!!
		#Filling the pre-prepared google form with scraped data
		for property in data:
			for index, value in enumerate(property):
				fields = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input.whsOnd')))
				field = fields[index]
				try:
					time.sleep(0.5)
					field.click()
					time.sleep(0.2)
					field.send_keys(property[index])
					submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.uArJ5e[role="button"]')))
					submit_btn.click()
					time.sleep(1)
				except Exception as e:
					print(f"Could not type into field: {e}")
			next_form = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.c2gzEf a')))
			next_form.click()
			time.sleep(1)
		time.sleep(999)




