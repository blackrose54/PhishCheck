from nltk.tokenize import RegexpTokenizer

def tokenizer(x):
    t = RegexpTokenizer(r'[A-Za-z]+')
    if 'https://' in x:
        x = x.replace('https://','');
    elif 'http://' in x:
        x = x.replace('http://','');
    if 'www.' in x:
        x = x.replace('www.','')
        return t.tokenize(x)
    else:
        return t.tokenize(x)
    