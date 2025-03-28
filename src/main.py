from web_scraper import WebScraper
from google_boot import GoogleBot

def main():
	#Scraping data
	scraper = WebScraper()
	web_page = scraper.scrape_web()
	data = scraper.handle_data(web_page)
	#Writing data to google form and further passing them to a Google sheet
	bot = GoogleBot()
	bot.write_data(data)

if __name__ == "__main__":
	main()