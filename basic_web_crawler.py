# import requests
# from flask import request, jsonify
# from bs4 import BeautifulSoup


# app.config["DEBUG"] = True
# app = Flask(__name__)

# @app.route('/companies', methods=['GET'])
# def companies():
#     r = requests.get("https://theinternship.io/") 
#     images_url = [] 
#     site_name = "https://theinternship.io/"
#     soup = BeautifulSoup(r.content, "html.parser")
#     images = soup.find_all("img", {"class": "center-logos"}
#     for i in images:
#         images_url.append( site_name + i['src'])
    
#     companies = [
#         {"companies" : images_url }
#     ]
#     return jsonify(companies)


# app.run()

import flask
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.config["DEBUG"] = True

images_url = [] 

@app.route('/companies', methods=['GET'])
def companies():
    r = requests.get("https://theinternship.io/") 
    soup = BeautifulSoup(r.content, "html.parser")
    images = soup.find_all("img", {"class": "center-logos"})
    for i in images:
        images_url.append( {"logo" : "https://theinternship.io/" + i['src']})
    
    companies = {"companies" : images_url }
    

    return flask.jsonify(companies)

app.run()