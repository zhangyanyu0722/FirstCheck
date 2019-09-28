index = ['a earthquake in Washington', 'there is earthquake in china', 'there is a earthquake in Alaska']

emergency_tweets = []

normal_tweets = []

all_cities = ['Alaska', 'Washington']

for i in index:

	for j in all_cities:

		if str(i).find(j) < 0:

			normal_tweets.append(i)

			continue

		else:

		    emergency_tweets.append(i)

print("emergency_tweets : ")

print(emergency_tweets)

print("normal_tweets : ")

print(normal_tweets)