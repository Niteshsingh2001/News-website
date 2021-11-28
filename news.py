import json
import requests
from bs4 import BeautifulSoup
import pprint

website = requests.get("https://www.ndtv.com/latest")
scrapping = BeautifulSoup(website.text,'html.parser')
data = scrapping.select(".news_Itm-cont")

def get_news(data):
     store_news = []

     for i in range(len(data)):

         heading = data[i].select(".newsHdng")
         link = data[i].select("a")
         content = data[i].select(".newsCont")
         store_news.append({"Headline" : heading[0].text,"Content" : content[0].text,"Visit Link" : link[0].get("href")})
         
        #  print(f"Content : {content[0].text}")
        #  print(f"Headline : {heading[0].text}")
        #  print("Visit Link :" , link[0].get("href"))  #getting link addresss of anchor tag
        #  print("\n")
        #  pprint.pprint(store_news)
     with open("news.json","w") as myfile:
        # for value in store_news:
            my_news_data = json.dumps(store_news)
            myfile.writelines(my_news_data)
    
     print("task done")
     
         
    
get_news(data)