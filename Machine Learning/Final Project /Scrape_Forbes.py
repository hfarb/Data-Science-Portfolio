import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from bs4 import BeautifulSoup
import codecs
import regex as re
import requests
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait       
from selenium.webdriver.common.by import By       
from selenium.webdriver.support import expected_conditions as EC


# Write a function to get unique links 
# Return unique links and links that have many other links in it
def get_unique_hrefs():
    hrefs = []
    href = driver.find_elements_by_xpath("//a[@href]")
    if href:
        for i in href:
            hrefs.append(i.get_attribute("href"))
    unique_hrefs = [x for x in hrefs if x.startswith("https://www.forbes.com/") and len(x) >=80]
    nested_hrefs = [x for x in hrefs if x.startswith("https://www.forbes.com/") and len(x) >=30 and len(x) < 80]
    return np.unique(unique_hrefs), np.unique(nested_hrefs)

# Write a function to get content per article and return all features of interest
def get_content(href):
    views = []
    links = []
    para = []
    titles = []
    times = []
    topics = []

    # Get views, if there is view, get all the features
    vi = driver.find_elements_by_class_name("pageviews")
    for i in vi:
        links.append(href)
        views.append(i.text)
        titles.append(driver.title)
        topic = driver.find_element_by_xpath("//a[@class='remove-underline']")
        topics.append(topic.text)
        
        article_p = []
        paragraphs = driver.find_elements_by_tag_name('p')
        for paragraph in paragraphs:
            article_p.append(paragraph.text)
        full_paragraph = "".join(article_p)
        para.append(full_paragraph)
        
        day = []
        t = driver.find_elements_by_tag_name('time')
        for i in t:
            day.append(i.text)
        full_time = " ".join(day)
        times.append(full_time)

    return links, titles, para, views, topics, times

# Ready to scrape
# Setting up path and driver
# Don't run options headless because it will not click, timeout error 
# Make sure to set user data dir or you will not be logged in
# Make sure you've already logged in with username and password, click remembered box
PATH = "C:\chromedriver.exe"
options = Options()
options.add_argument('--no-sandbox')
options.add_argument("start-maximized")
options.add_argument("user-data-dir=C:\\Users\\alice\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path=PATH, options=options)

# One single topic instead of two or more, easier to manage
# Two dataframes, one for second nested links
topics = ['lifestyle']
hrefs = []
category = []
df3 = pd.DataFrame(columns=['link', 'title', 'text', 'view', 'topic', 'time'])
df4 = pd.DataFrame(columns=['link', 'title', 'text', 'view', 'topic', 'time'])


for topic in topics:
    url = "https://www.forbes.com/" + str(topic)
    driver.get(url)
        
    # Get specific range of clicks on button to load more articles, wait in-between each click
    for i in range(7):
        wait = WebDriverWait(driver, 10)
        element = wait.until(lambda driver: driver.find_element_by_xpath("//*[@class='load-more']"))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(10)
        
    # Get all hrefs in that fully loaded site after 6 clicks
    all_hrefs = get_unique_hrefs()
    unique_hrefs = all_hrefs[0]
    nested_hrefs = all_hrefs[1]
    
    # Go over the unique links and get content if there is view
    # Deposit in the first dataframe row
    for i, link in enumerate(unique_hrefs):
        driver.get(link)
        if driver.find_elements_by_class_name("pageviews"):
            content = get_content(link)
            df3.loc[i] = [content[0], content[1], content[2], content[3], content[4], content[0]]
        else:
            pass
        
    # Go over the nested links and get unique links
    for i in nested_hrefs:
        more_hrefs = get_unique_hrefs()[0]
        
    # Iterate over the unique links of the nested links earlier
    for i, link in enumerate(more_hrefs):
        driver.get(link)
        if driver.find_elements_by_class_name("pageviews"):
            content = get_content(link)
            df4.loc[i] = [content[0], content[1], content[2], content[3], content[4], content[5]]
        else:
            pass
        
dfs = pd.concat([df4, df3], ignore_index=True)
dfs.to_csv("df_lifestyle.csv")
