# 🏡 Zillow Google Form Bot

This project demonstrates how to **scrape real estate listings** from a static website using `requests` and `BeautifulSoup`, and automatically **fill out a Google Form** using `Selenium` with `undetected-chromedriver`.

It's a great example of combining **web scraping** and **browser automation** to simulate end-to-end data collection and submission.

---

## 🔧 Technologies Used

### 📄 Web Scraping
- Uses `requests` to send HTTP requests directly (faster than Selenium for static pages).
- Parses HTML using `BeautifulSoup` with the `lxml` parser.
- Extracts structured data (address, price, link) into a list of tuples.

> ✅ Static scraping is lightweight and robust when no JavaScript rendering is needed.

### 🤖 Browser Automation
- Uses `Selenium` to automate Chrome via `undetected-chromedriver` (bypasses bot detection).
- Interacts with dynamic form elements, handles locale issues, and ensures stable field interaction.
- Submits data and clicks **"Submit another response"** for multiple entries.

> ✅ Best practice: elements are re-fetched each iteration to avoid stale references.

---

## 🧠 Project Structure

your_project/ ├── src/ │ ├── web_scraper.py # Scrapes Zillow clone page │ ├── google_bot.py # Automates Google Form filling │ └── main.py # Glue script ├── requirements.txt # Python dependencies ├── .gitignore # Ignore build/junk files └── README.md # This file


---

## 🚀 How to Run

### 1. Clone the project and enter it

<pre>bash
git clone https://github.com/your-username/zillow-form-bot.git
cd zillow-form-bot 

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

pip install -r requirements.txt

python src/main.py</pre>

🛠️ What You Should Replace
<pre>
    Important! Before running the code, make sure you do the following:
</pre>
✅ Replace the form_link in google_bot.py with your own Google Form link:

<pre>form_link = "https://docs.google.com/forms/..."</pre>

✅ Ensure you have the correct path to chromedriver in google_bot.py:

<pre>driver_path = "/path/to/your/chromedriver"</pre>

✅ Your form should contain three input fields in order: Address, Price, Link. It is
easily changeable according to your needs, by creating more or less form fields and
adjust the code slightly. With 1 click on google form, you can conect it with google sheet
like in my code and get all the data written to google sheet.

💡 Note: Google Forms can randomly change language or field structure — this project forces English (en-US) and re-finds elements each loop to handle DOM changes.

💬 Final Notes

Designed for demonstration, learning, and prototyping — not production deployment.

Works on static websites that don't use heavy JavaScript rendering.

Google Form layout should not, but can, be customized unless you adjust the selectors accordingly.
    
What I learned here:

🧠 Dev Wisdom

    "In every loop iteration, code must find the element over and over again — otherwise, the element becomes stale!"

Keep that in your toolbox. This is how real automation gets done. 🧱

Made with 🧠 and ☕ by a dev who knows that scraping and automation go hand in hand.

> _“I will unsheathe my sword by creating the code in my name!”_ ⚔️ Milos Grujic (aka Gruyanidas)