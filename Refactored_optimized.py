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
names=["First","Second","Third","Fourth","Fifth"]
for x in names:
    name=x+"_process.csv"
    print(name)
    if os.path.exists(name):
        os.remove(name)
    else:
        print(name,"does not exist")
  

#Calculating the current time
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

    # Configuration of the different processes
    config_1 = configure_twint("2022-12-31","2023-01-01", "climate change","First_process.csv")
    config_2 = configure_twint("2022-12-29","2022-12-30", "climate change","Second_process.csv")
    config_3 = configure_twint("2022-12-27","2022-12-28", "climate change","Third_process.csv")
    config_4 = configure_twint("2022-12-25","2022-12-26", "climate change","Fourth_process.csv")
    config_5 = configure_twint("2022-12-23","2022-12-24", "climate change","Fifth_process.csv")

    # Splitting the serach date among different processes
    p1 = multiprocessing.Process(target=search_twint, args=(config_1, ))
    p2 = multiprocessing.Process(target=search_twint, args=(config_2, ))
    p3 = multiprocessing.Process(target=search_twint, args=(config_3, ))
    p4 = multiprocessing.Process(target=search_twint, args=(config_4, ))
    p5 = multiprocessing.Process(target=search_twint, args=(config_5, ))

    # Starting the different processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    # Ending the different processes
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

# Getting time
t2=time.time()
print(t2-t1)
