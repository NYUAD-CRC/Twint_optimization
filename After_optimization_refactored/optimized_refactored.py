# Import Libraries
import twint
import nest_asyncio
nest_asyncio.apply()
import time
import pandas as pd
import os
import re
import multiprocessing 
import datetime
import sys

# Removing old result
def file_remover(name):
        if os.path.exists(name):
            os.remove(name)
            print(name," old is removed")
        else:
            print(name,"does not exist")

# Calculating the current time
t1=time.time()

# Function to run the search
def search_twint(c):
    twint.run.Search(c)
    return twint.storage.panda.Tweets_df

# configuration
def configure_twint(start_date, end_date, search_term,file_name):
    c = twint.Config()
    c.Until = end_date
    c.Since = start_date
    c.Lang = "en"        # Language
    c.Pandas = True
    c.Store_csv = True
    c.Output = file_name
    c.Search = search_term  # key words to look for.
    return c

if __name__ == '__main__':

    # consider the start date as 2022-december 23 st
    start_date = datetime.date(2022, 12, 23)
    
    # consider the end date as 2023-january 1 st
    end_date = datetime.date(2023, 1, 1)
    
    # delta times
    delta_s = datetime.timedelta(days=2)
    delta_n = datetime.timedelta(days=1)
    
    # iterate over range of dates
    while (start_date <= end_date):
        # Empty list for processes
        procs = []
        # End time per loop
        end_intermediate_date = start_date + delta_n
        file_name=start_date.strftime("%Y-%m-%d")+"_process.csv"
        # Removing old results
        file_remover (file_name)
        start=start_date.strftime("%Y-%m-%d")
        end=end_intermediate_date.strftime("%Y-%m-%d")
        config = configure_twint(start,end, "climate change",file_name)
        proc = multiprocessing.Process(target=search_twint, args=(config, ))
        # Filling the list with different processes
        procs.append(proc)
        proc.start()
        # Incrementing the start time
        start_date += delta_s
        
    # completing the processes
    for proc in procs:
        proc.join()

# Getting time
t2=time.time()
print(t2-t1)
with open('filename.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(t2-t1)
    sys.stdout = original_stdout # Reset the standard output to its original value
