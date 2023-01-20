# Import Libraries
import twint
import nest_asyncio
nest_asyncio.apply()
import time
import pandas as pd
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    c.Search = search_term  # key words to look for.
    return c
    
if __name__ == '__main__':
    start_date = "2022-12-31"
    end_date = "2023-01-01"
    search_term = "climate change"
    config = configure_twint(start_date, end_date, search_term)
    # Use ThreadPoolExecutor to run the searches in parallel
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.submit(search_twint, config)
        
        # Wait for the task to complete and retrieve the result
        tweets_df = results.result()
        # Export the tweets to a CSV file
        tweets_df.to_csv('./orig_tweets_test.csv', index=False)
 
t2=time.time()
print(t2-t1)
