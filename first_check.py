vimport tweepy 
import csv  
import string

def search_tweets(disastor, number):

	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_token_secret = ''
  
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
	auth.set_access_token(access_token, access_token_secret)   
	api = tweepy.API(auth)

	search_results = api.search(disastor, count = number)

	index = []

	for tweet in search_results:

		if 'text' in tweet._json:

			index.append(tweet._json['text'])

			# print(tweet._json['text'])

			with open("all_dis.txt", 'a') as f:

				f.write('[BEGIN]' + tweet._json['text'] + '\n\n')

# 	emergency_tweets = []

# 	csv_file = csv.reader(open("us_cities_states_counties.csv",'r'))

# 	city_list = []

# 	for stu in csv_file:

# 		city_list.append(stu)

# 	city_split = []

# 	state_split = []

# 	k = len(city_list)-1

# 	for cities in range(len(city_list)-1):

# 		a = city_list[cities+1][0].split("|")

# 		city_split.append(a[0])

# 		state_split.append(a[2])

# 	all_cities = city_split + state_split

# 	for i in index:

# 		for j in all_cities:

# 			if str(i).find(j) < 0:

# 				# normal_tweets.append(i)

# 				continue

# 			else:

# 		  	  	emergency_tweets.append(i)

# 		   	 	break
# 	# print("emergency_tweets : ")

# 	index_1 = []

# 	for key in emergency_tweets:

# 		index_1.append(key)

# 		# print(tweet._json['text'])

# 		with open("filter_dis.txt", 'a') as f:

# 			f.write('[BEGIN]' + key + '\n\n')









