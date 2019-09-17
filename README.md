# Mini-project-1

## Group Numbers

- Name_1: Jennifer Campbell (U48001098)
- Name_2: Yanyu Zhang (U47793163)

## User Stories

- I, the first response team, want to know when people need emergency assistance when a natural disaster happens
- I, the family member, want to know when my family is safe/not safe, when a disaster is in their area
- I, the ordinary person, want to know when the disaster will occur in my city/district, and how to take refuge and change the schedule
- I, a manager of a travel agency, want to know how to design tour route to avoid the disaster
- I, the farmer, want to know when the disaster will happen in this area and take some measurements to protect crops

## Architecture

- When you open the app, you enter the identity of user and name (city, district, county, etc.) of the location you are trying to investigate.
- After selecting location, designate which type of disaster you are concerned with investigating.
- The app will then filter through tweets that contain terms relating to: 1st. Location; 2nd. Disaster.
- Using natural language API, the sentiment will determine whether the poster of the tweet is in need of assistance or is safe.
- The user will then choose to take action if the poster is deemed to be unsafe.
- If the tweet’s sentiment is considered safe, the app will continue through to the next tweet until one is determined to be unsafe.

## Analysis of Twitter API, Google Vision, and Google Natural Language API

- When inputting tweets about natural disasters into the natural language API, Google frequently focused on the name of the disaster instead of the type first. For example, in our selections below, the tweets about the recent Hurricane Dorian were recognized as a person instead of a hurricane. We would like to have our API focus on the fact that it is a hurricane first and foremost in order to get through to our filtering process.

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

## Types of Twitter feeds we’re interested in

- Posters after natural disasters
- First responders looking for backup






