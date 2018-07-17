import tweepy
import textblob
import matplotlib.pyplot as plt

consumerKey='your consumer key'
consumerSecret='your consumer secret'
accessToken='your access token'
accessSecret='your access secret'

authentication = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)
authentication.set_access_token(accessToken, accessSecret)
api = tweepy.API(authentication)

keyword=input('Enter what do you wanna search about?')
numberOfTweets=int(input('Enter the number of tweets'))

tweets = tweepy.Cursor(api.search, q=keyword, lang='en').items(numberOfTweets)


positive = 0
negative = 0
neutral = 0
polarity = 0

def calculatePercentage(a,b):
    return 100*float(a)/float(b)

for tweet in tweets:
    print(tweet.text)
    myAnalysis=textblob.TextBlob(tweet.text)
    polarity += myAnalysis.sentiment.polarity
    if myAnalysis.sentiment.polarity ==0:
        neutral+=1
    elif myAnalysis.sentiment.polarity > 0.00:
        positive+=1
    elif myAnalysis.sentiment.polarity < 0.00:
        negative+=1

positive=calculatePercentage(positive,numberOfTweets)
negative=calculatePercentage(negative,numberOfTweets)
neutral=calculatePercentage(neutral,numberOfTweets)

positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')

print('----------------------------------------------------------------------------')
if polarity>0:
    print('Positive')
elif polarity<0:
    print('Negative')
elif polarity==0:
    print('Neutral')

labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]','Negative [' + str(negative) + '%]']
sizes=[positive,neutral,negative]
colors=['green','yellow','red']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc="best")
plt.title('How people are reacting on ' + keyword + ' by analyzing ' + str(numberOfTweets) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()
