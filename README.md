# Mini-project-1

Name_1: Jennifer Campbell (U48001098)
Name_2: Yanyu Zhang (U47793163)

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

2. Item2
    - something eles
        - something eles else

[My reference](http://www.google.com)
<img src= " ">
