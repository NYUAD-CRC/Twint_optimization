# Import Libraries
import twint
import nest_asyncio
nest_asyncio.apply()
import time
import pandas as pd
import os
import re
import multiprocessing

# Removing old result
if os.path.exists("tweets_test.csv"):
  os.remove("tweets_test.csv")
else:
  print("The results file does not exist")

#Calculating the current time
t1=time.time()

# Function to run the search
def search_twint(c):
    twint.run.Search(c)
    return twint.storage.panda.Tweets_df

# configuration
def configure_twint(start_date, end_date, search_term):
    c = twint.Config() 
    c.Until = end_date
    c.Since = start_date
    c.Lang = "en"        # Language
    c.Pandas = True
    c.Store_csv = True
    c.Output = "tweets_test_4days.csv"
    c.Search = search_term  # key words to look for.
    return c

if __name__ == '__main__':
    start_date = "2022-12-23"
    end_date = "2023-01-01"
    search_term = "climate change"
    config = configure_twint(start_date, end_date, search_term)
    p1 = multiprocessing.Process(target=search_twint, args=(config, ))
    p1.start()
    p1.join()

# Getting time
t2=time.time()
print(t2-t1)
