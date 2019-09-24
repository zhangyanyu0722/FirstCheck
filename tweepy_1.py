import tweepy  
  
consumer_key = '***********************'  
consumer_secret = '*************************'  
access_token = '****************************'  
access_token_secret = '*******************************'  
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
  
api = tweepy.API(auth)



# public_tweets = api.user_timeline('BostonDynamics')  
# for tweet in public_tweets:  
#     print(tweet.text)



# public_tweets = api.home_timeline()  
# for tweet in public_tweets:  
#     print(tweet.text)



# api.update_status('hello python')



# for tweet in tweepy.Cursor(api.search,q='League of Legends').items(10):  
#     print('Tweet by: @' + tweet.user.screen_name)  



# search_results = api.search(q = 'python', count = 100)
# for tweet in search_results:
# 	if 'text' in tweet._json:
# 		print(tweet._json['text'])


















  
