import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    # Obtains a fact from 'http://unko.com' and stores in the variable 'response'
    response = requests.get("http://unkno.com")

    # Uses BeautifulSoup to parse the content into html
    soup = BeautifulSoup(response.content, "html.parser")
    # Stores the Fact from the HTML content into the variable 'facts'
    facts = soup.find_all("div", id="content")

    return facts[0].getText()

def pig_latinize(pig_latin_URL):
    response = requests.get(url=pig_latin_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    string_list = soup.find_all(string=True)
    return string_list[-2]

@app.route('/')
def home():
    # This website only needs to return the link of the randomly scraped fact
    # and display it to the screen

    # Store the request URL into a variable
    pig_latin_URL = "https://hidden-journey-62459.herokuapp.com/piglatinize/"

    # Run the get_fact() function and scrape for a fact.
    random_fact = get_fact()
    
    # Store the Random fact in a dictionary to perform a "POST" request
    form_data = {"input_text": str(random_fact)}

    # send a "POST" request to the URL and obtain a response
    response = requests.post(url=pig_latin_URL, data=form_data, allow_redirects=False)

    # Obtain the URL of the Website from the Response Headers
    response_url = response.headers['location']

    # Take that URL and get the Pig Latin String
    pig_latin = pig_latinize(response_url)

    
    text = """
    <html>
    <body>
    Here is the original fact: {}
    <br> Here it the Response URL: {}
    </body>
    </html>""".format(random_fact, pig_latin)

    # Pass the fact to the pig latinizer 

    # Scrape the code for the link

    # print out the link.
    return text


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

#url = "http://hidden-journey-62459.herokuapp.com/esultray/1b7286fbc29436f4de5c7c582a851755/"
#response = requests.get(url=url)
#soup = BeautifulSoup(response.content, "html.parser")
#string_list = soup.find_all(string=True)
#print(string_list[-2])
#content = soup.text



