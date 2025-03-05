from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# Set up headless Chromium browser
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

@app.route('/')
def home():
    driver.get('https://example.com')  # Change this URL to the site you want to browse
    return driver.page_source  # Returns the HTML content of the page

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
