#data collection
import os
import time# shows how much time takes to download html page
import requests#helps to download file from website
import sys


def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                   url ='https://en.tutiempo.net/climate/0{}-{}/ws-432950.html'.format(month,year)
                   
            else:
                   url ='https://en.tutiempo.net/climate/{}-{}/ws-432950.html'.format(month,year)

            texts=requests.get(url)# helps to retrieve all data in url
            text_utf=texts.text.encode('utf=8')# used to fix character present in information
      
            if not os.path.exists("/DATA/Html_data/{}".format(year)):
                 os.makedirs("/DATA/Html_data/{}".format(year))
            with open("/DATA/Html_data/{}/{}.html".format(year,month),"wb") as output: #opening in right mode
                 output.write(text_utf)
            
        
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time =time.time()
    retrieve_html()
    stop_time=time.time()
    print("time taken {}".format(stop_time-start_time))