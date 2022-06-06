#%%
from lxml import html
import requests
import csv
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

#%%
def web_scrape(n):
    name = []
    purpose = []
    for i in range(n):

        record = requests.get("http://3.89.180.32:8000/random_company")
        cont = html.fromstring(record.content)
        buyers = cont.xpath('//li/text()')

        li = [elem.split(':') for elem in buyers] 

        for i in range(len(li)):
            if li[i][0] == 'Name':
                name.append(li[i][1])
            elif li[i][0] == 'Purpose':
                purpose.append(li[i][1])
                break

    return name + purpose
               
#%%
a = web_scrape(51)
print(a)

#%%
def sentiment_csv(x):
    a = web_scrape(51)
    half = len(a)//2
    name = a[0:half]
    purpose = a[half:]
    #combime both lists
    name_purpose = [list(t) for t in zip(name, purpose)]
    print(name_purpose)
    #%%
    fields = ['Company Name', 'Purpose']

    with open(x, 'w') as f:
        
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(fields)
        write.writerows(name_purpose)

    df = pd.read_csv(x)
    sentiment = SentimentIntensityAnalyzer()
    scores = []

    for name, values in df.iloc[:, 1].iteritems():
        scores.append(sentiment.polarity_scores(values))

    comp_scores = []

    for i in range(len(scores)):
        comp_scores.append(scores[i]['compound'])

    df['Compound Scores'] = comp_scores
    df = df.sort_values(by = 'Compound Scores', ascending = False)

    return df.to_csv(x)

#%%
#df = pd.read_csv('TEST.csv')

# Companies with Highest Sentiment Scores
#df.head(n = 10)

#Companies with Lowest Sentiment Scores
#df.tail(10)

# %%
if __name__ == "__main__":
    #web_scrape(5)
    sentiment_csv('TEST.csv')
# %%
#'Companies Web Scrape.csv'