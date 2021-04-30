# W207 Final Project

Group members: Alice Hua, Derrick Xiong, Haley Farber

Hello! This our final project for W207, our introduction to machine learning class. Our project is about predicting the popularity of online news articles. For our project, we scraped about 7,000 articles from Forbes from January 2020 to November 2020 and extracted article attributes such as an article's URL link, title, text, topic, time published,and number of views. We then created 65 features from these attributes. Most of these features were built and named after the features used by Kelwin Fernandes,Pedro Vinagre, and Paulo Cortez from their dataset that was used to measure the popularity of Mashable articles from 2013-2015. Instead of using shares to predict an article's popularity as was done by those who used the Mashable data set, we used views to predict an article's popularity and used linear regression to do so. The following documents are found in this repo:

1) Scrape_Forbes.py: the python script that was run to scrape the data from Forbes. At the bottom of the script, we scraped for a particular topic. This script ran for the "lifestyle" topic but it was also run on the topics innovation,leadership,money,and business. Each script produced a csv per topic. These csvs were then compiled to produce the final comprehensive csv with about 7,000 articles.
2) data_7k.csv: the csv produced by scraping Forbes.
3) Features.ipynb: jupyter notebook with the code to produce the 65 features from the attributes from the Forbes articles. It reads in the data_7k csv to produce the features.
4) data.csv: the csv with both the attributes from Forbes and the 65 features created from the atrributes.
5) Regressions.ipynb: jupyter notebook with exploratory data analysis on our data and regressions run to predict the number of views articles have. 
6) W207 Final Presentation Alice-Haley-Derrick.pdf: our final powerpoint presentation about our findings.
7) FinalReport.pdf: a pdf documenting all of our findings and results with citations. 


