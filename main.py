from fastapi import FastAPI
import joblib
from nltk.tokenize import RegexpTokenizer # regexp tokenizers use to split words from text  
from tokenizer import tokenizer
from screenshot import get_screenshot
import whois
import requests
import socket
import re

app = FastAPI()
response = dict()
with open('model.sav','rb') as fp:
    model = joblib.load(fp)
        
@app.get('/api/')
def query(url:str):
    response['whois'] = dict(whois.whois(url))
    m = re.search('https?://([A-Za-z_0-9.-]+).*', url)
    domain = m.group(1)
    ip = socket.gethostbyname(domain)
    response['ipinfo'] = requests.get('https://ipinfo.io/'+ip+'/json').json()
    res = model.predict([url])[0]
    response['result'] = res
    image = get_screenshot(url)
    response['image'] = image
    return response
