import tweepy 

import csv  

import string
  
consumer_key = '' 

consumer_secret = '' 

access_token = '' 

access_token_secret = ''  
  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  

auth.set_access_token(access_token, access_token_secret)  
  
api = tweepy.API(auth)

# search_results = api.user_timeline('YANYUZHANG6')

q = 'earthquake'  # change the disastor here

search_results = api.search(q, count = 10)

index = []

for tweet in search_results:

	if 'text' in tweet._json:

		index.append(tweet._json['text'])

		# print(tweet._json['text'])

		with open("all_dis.txt", 'a') as f:

			f.write(tweet._json['text'] + '\n\n')

	# print("\n")

# print("\n")

# print(index)

emergency_tweets = []

csv_file = csv.reader(open("us_cities_states_counties.csv",'r'))

city_list = []

for stu in csv_file:

    city_list.append(stu)

city_split = []

state_split = []

k = len(city_list)-1

for cities in range(len(city_list)-1):

    a = city_list[cities+1][0].split("|")

    # print(a[2])

    city_split.append(a[0])

    state_split.append(a[2])

all_cities = city_split + state_split

# print(all_cities)

# print(index)


for i in index:

	for j in all_cities:

		if str(i).find(j) < 0:

			# normal_tweets.append(i)

			continue

		else:

		    emergency_tweets.append(i)

		    break


print("emergency_tweets : ")

# print(len(emergency_tweets))

for key in emergency_tweets:

	print(key)

	print("\n")








