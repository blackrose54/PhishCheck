from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.linear_model import LogisticRegression

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from tokenizer import tokenizer

def evaluate(pipeline,url,label):
    cfm = pd.DataFrame(confusion_matrix(label,pipeline.predict(url)),columns = ['Predicted:Bad', 'Predicted:Good'],
                index = ['Actual:Bad', 'Actual:Good'])
    plt.figure(figsize= (6,4))
    sns.heatmap(cfm, annot = True,fmt='d',cmap="YlGnBu")
    print("Accuracy",pipeline.score(url,label)*100)
    plt.show()


df = pd.read_csv('final_dataframe.csv')

pipeline = make_pipeline(CountVectorizer(tokenizer=tokenizer,stop_words='english'),LogisticRegression(n_jobs=-1))

print("Trianing the Model..")

pipeline.fit(df.url,df.label)

print('Done Training !')

test = pd.read_csv('verified_online.csv')

test['label'] = 'bad'

print("Evaluating the model...")

evaluate(pipeline,test.url,test.label)

with open('model.sav','wb') as fp:
    joblib.dump(pipeline,fp)

