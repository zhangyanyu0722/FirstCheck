# Mini-project-1: First Check
<p align="center">
  <a href="https://docs.google.com/presentation/d/11-jlRNnnwyELKESdG6k7fvwvgQGAvKY6rJiQV4QFgRs/edit?usp=sharing">Overview</a>
</p>

## Team Members

- Jennifer Campbell (U48001098)
- Yanyu Zhang (U47793163)
- David Henderson (U13104443)

## Project Mission
- In order to bridge emergency response communications across social media platforms, our team is working to build a filtering app that allows for users to view tweets related to disasters happening in a selected location.


## User Stories

- I, the first response team, want to know when people need emergency assistance when a natural disaster happens
- I, the family member, want to know when my family is safe/not safe, when a disaster is in their area
- I, the ordinary person, want to know when the disaster will occur in my city/district, and how to take refuge and change the schedule
- I, a manager of a travel agency, want to know how to design tour route to avoid the disaster
- I, the farmer, want to know when the disaster will happen in this area and take some measurements to protect crops

## How it works

1. When you open the app, you enter the identity of user and name (city, district, county, etc.) of the location you are trying to investigate.
2. After selecting location, designate which type of disaster you are concerned with investigating.
3. The app will then filter through tweets that contain terms relating to: 1st. Location; 2nd. Disaster.
4. Using natural language API, the sentiment will determine whether the poster of the tweet is in need of assistance or is safe.
5. The user will then choose to take action if the poster is deemed to be unsafe.
6. If the tweet’s sentiment is considered safe, the app will continue through to the next tweet until one is determined to be unsafe.
<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/jennifercampbell/flowchart.png">
</p>






## Types of Twitter feeds being focused on

- Posters after natural disasters
- First responders looking for backup

## Twitter feed examples with sentiment

- [连续3个月的暴乱重创香港旅游业，8月访港旅客较去年急跌近40%，有酒店“十室九空”。即将到来的十一黄金周，旅游业界人士预测访港团数将较去年同期减少超70%！业界怒斥搞事者存心制造经济大灾难！香港两大主题乐园，迪士尼和海洋公园，人烟稀少.]<br>[The riots for three consecutive months have hit Hong Kong's tourism industry. In August, visitors to Hong Kong plunged nearly 40% compared with last year. There are hotels with ten rooms and nine airspaces. In the upcoming National Day, the travel industry will be reduced by 70% compared with the same period last year! The industry is angry at the troublemakers to create an economic catastrophe! Hong Kong's two major theme parks, Disney and Ocean Park, are sparsely populated.]

<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/master/picture/sentimentcomment1.png">
</p>

- [还记得前不久四川地震预警倒计时吗，目前提前数秒已到极限。此前，科学家在模拟地震中发现了“前震”的存在，现实中却一直没有实锤。最近，在分析了几百万份高分辨率地震数据后，终于与实验相吻合了！这将是实现地震预警的一大飞跃]<br>[Do you remember the countdown to the Sichuan earthquake warning? And it has reached a few seconds ahead of time. Previously, scientists discovered the existence of “existing earthquakes” in simulated earthquakes. In reality, there has been no real hammer. Recently, after analyzing millions of high-resolution seismic data, it finally coincided with the experiment! This will be a big achievement in achieving earthquake warning]

<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/master/picture/sentimentcomment2.png">
</p>

- [Thank you; what is really needed is the evacuation of the people of Abaco and Freeport. Can you help with that? Abaco is not going to be habitable for months, if ever.The people have no shelter, no way of preparing food,no sewer, no future there. #EvacuationNeeded #BahamasRelief]

<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/master/picture/sentimentcomment3.png">
</p>

- [It’s Been Basically A Week Since Hurricane Dorian And Up To This Day I Still Don’t Know If My Brother Is Alive Or Not. And It’s Killing Me Slowly But Surely. If Anyone From Abaco That Knows My Brother Please I’m Begging You To Reach Out To Me And Help Me Out On This One.]

<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/master/picture/sentimentcomment4.png">
</p>

- [Let’s help find people. If you have a family member who is missing in the Bahamas, in an area that was affected by Hurricane Dorian, send me their name, picture and location. If you want to record a video giving all the info, that’s good, too. Tag me. I will share it.]

<p align="center">
  <img src= "https://github.com/zhangyanyu0722/Mini-project-1/blob/master/picture/sentimentcomment5.png">
</p>

## Analysis of Twitter API, Google Vision, and Google Natural Language API

- When inputting tweets about natural disasters into the natural language API, Google frequently focused on the name of the disaster instead of the type first. For example, in our selections below, the tweets about the recent Hurricane Dorian were recognized as a person instead of a hurricane. We would like to have our API focus on the fact that it is a hurricane first and foremost in order to get through to our filtering process.

- We ran into some initial difficulties utilizing the NL API. The index function in the sample provided only sorts individual files, so we had the choice to either give each tweet its own file (which takes up unnecessary space), or change the function to index by each chink of text in the file.

- There is also a secondary issue that the NL API does not classify by individual words as easily, moreso topics and themes.

## How to Use

- Download FirstCheck_UI.py, first_check.py, firstcheckmain.py, sentimentanalyzer.py, and us_cities_states_counties.csv
- Create an <a href="https://cloud.ibm.com/docs/services/watson?topic=watson-about#about">IBM Cloud account</a> to access use of the <a href="https://cloud.ibm.com/apidocs/natural-language-understanding/natural-language-understanding">Natural Language API</a>
- Run FirstCheck_UI with the command "python FirstCheck_UI.py"; a window should open with command options
- To test the system works, select "Earthquake" and then input city name as "Washington DC"
  - Output should be fed back to you through the terminal, listing words related to earthquakes in the area of Washington DC with positive/negative sentiments applied

## Updates

- 9/29/19: Decided to use IBM Natural Language API instead of Google. IBM has a larger keyword and entity dictionary by which it categorizes phrases, and therefore is easier to implement when searching for natural disasters and locations.

- 10/2/19: MVP released. Still unable to list all tweets due to IBM character limits.
