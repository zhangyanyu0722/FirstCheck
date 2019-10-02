from sentimentanalyzer import classify
from first_check import search_tweets

disaster = input()
number = input(" ")
number = int(number)
location = input()

search_tweets(disaster, number)

textin = sys.argv[1]
openfile = open(textin,"r")
readfile = openfile.read()
tweetstrings = readfile.split('[BEGIN]')
tweets = [x.strip() for x in tweetstrings if len(x) != 0]
# tweets = [x.replace('\n+', ' ') for x in tweets]

for tweet in tweets:
  classifiedtweet = classify(tweet)
  if any(location in classified):
    print(classifiedtweet)