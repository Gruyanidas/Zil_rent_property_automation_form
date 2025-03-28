import dotenv, os
import requests, json
from bs4 import BeautifulSoup
import re

class WebScraper:
	"""Scrapes static web and orgranises scraped data for further parsing"""
	zil_url = os.getenv("ZIL_CLONE_URL")

	@staticmethod
	def perform_http_request(url: str, method: str = "GET", params=None, data=None, headers=None):
		"""Generic method to handle GET, POST, PUT"""
		try:
			method = method.upper()
			if method == "GET":
				response = requests.get(url=url, params=params, headers=headers, timeout=10)
			elif method == "POST":
				response = requests.post(url=url, json=data, headers=headers, timeout=10)
			elif method == "PUT":
				response = requests.put(url=url, json=data, headers=headers, timeout=10)
			elif method == "DELETE":
				response = requests.delete(url=url, headers=headers, timeout=10)
			else:
				raise ValueError(f"Unsupported HTTP method: {method}")

			response.raise_for_status()
			return response

		except requests.exceptions.Timeout:
			raise RuntimeError("Request timed out. Try again later.")
		except requests.exceptions.ConnectionError:
			raise RuntimeError("Network connection error. Check your internet.")
		except requests.exceptions.HTTPError as http_err:
			raise RuntimeError(f"HTTP error occurred for {method} {url}: {http_err}")
		except requests.exceptions.RequestException as req_err:
			raise RuntimeError(f"Request failed: {req_err}")
		except json.JSONDecodeError:
			raise RuntimeError("Failed to parse JSON response.")

	def scrape_web(self) -> BeautifulSoup:
		response = WebScraper.perform_http_request(method="GET", url=self.zil_url)
		web_page = BeautifulSoup(response.content, "lxml")
		return web_page

	@staticmethod
	def handle_data(web_page :BeautifulSoup) -> list[tuple]:
		"""Extracts data from a soup in a tuple ready for filling the form"""
		property_cards = web_page.find_all("div", class_="StyledPropertyCardDataWrapper")
		data = []

		for item in property_cards:
			address = item.find("address").get_text().strip()
			price = item.find("span", class_="PropertyCardWrapper__StyledPriceLine").get_text().strip()
			match = re.search(r"\$\d{1,3}(?:,\d{3})*", price)
			if match:
				price = match.group()
			link = item.find("a")["href"]
			data.append((address,price,link))
		return data

