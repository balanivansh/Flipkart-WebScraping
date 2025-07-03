# Flipkart Product Review Scraper

This project is a simple web application built with Flask and Bootstrap that allows users to search for any product on Flipkart and view its reviews in a clean, blue-themed table.

## Features
- Enter any Flipkart product name in the search box
- Scrapes and displays reviews (Name, Rating, Review Heading, Review)
- Clean, responsive UI with Bootstrap

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/flipkart-review-scraper.git
   cd flipkart-review-scraper/flipkart
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   python app.py
   ```

4. **Open in your browser:**
   Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Requirements
- Python 3.7+
- Flask
- requests
- beautifulsoup4

## File Structure
```
flipkart/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
```

## Notes
- This app scrapes public reviews from Flipkart. The structure of Flipkart's website may change, which could break the scraper.
- For educational purposes only.

## License
MIT
