from first_check import search_tweets

print("Please input the disaster")
disaster = input()
print("Please input the number of tweets")
number = input(" ")
number = int(number)

search_tweets(disaster, number)