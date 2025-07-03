from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse

app = Flask(__name__)

def get_flipkart_reviews(product_name):
    # Encoding the product name for URL (handles spaces and special characters)
    encoded_product = urllib.parse.quote_plus(product_name)
    flipkart_url = f"https://www.flipkart.com/search?q={encoded_product}"
    try:
        res = requests.get(flipkart_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = bs(res.text, "html.parser")
        main_divs = soup.findAll("div", {"class": "cPHDOP col-12-12"})
        if len(main_divs) < 4:
            return []
        product_link = "https://www.flipkart.com" + main_divs[3].div.div.div.a['href']
        product_req = requests.get(product_link, headers={'User-Agent': 'Mozilla/5.0'})
        product_html = bs(product_req.text, "html.parser")
        review_divs = product_html.findAll("div", {"class": "RcXBOT"})
        reviews = []
        for i in review_divs:
            try:
                name = i.div.div.findAll("p", {"class": "_2NsDsF AwS1CA"})[0].text
                rating = i.div.div.div.div.text
                review_heading = i.div.div.div.p.text
                review = i.div.div.find("div", {"class": ""}).text
                # Remove 'READ MORE' if present
                review = review.replace('READ MORE', '').strip()
                reviews.append({
                    'name': name,
                    'rating': rating,
                    'review_heading': review_heading,
                    'review': review
                })
            except Exception:
                continue
        return reviews
    except Exception:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    reviews = []
    product = ''
    if request.method == 'POST':
        product = request.form.get('product')
        if product:
            reviews = get_flipkart_reviews(product)
    return render_template('index.html', reviews=reviews, product=product)

if __name__ == '__main__':
    app.run(debug=True)
