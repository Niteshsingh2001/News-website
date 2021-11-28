from os import get_terminal_size
from flask import Flask,render_template,request,redirect
import requests as rqs
from bs4 import BeautifulSoup
from gtts import gTTS


app = Flask(__name__)

website = rqs.get("https://www.ndtv.com/latest")
scrapping = BeautifulSoup(website.text,'html.parser')
data = scrapping.select(".news_Itm-cont")
# img_data = scrapping.select("news_Itm-img")
# print(img_data)

def get_img():
    pass

def get_news(data):
     store_news = []
     store_news.clear()
     for i in range(len(data)):
         heading = data[i].select(".newsHdng")
         link = data[i].select("a")
         content = data[i].select(".newsCont")
         store_news.append({"Headline" : heading[0].text,"Content" : content[0].text,"Visit Link" : link[0].get("href")})
         myobj = gTTS(text=store_news[0]["Headline"], lang="en", slow=False) 
         myobj.save("welcome.mp3")
     print("task done")
     return store_news  
 
datax=[]    

@app.route("/")
async def hello_world():
    global datax
    datax.clear
    datax.append(get_news(data))
    
    return render_template("index.html",news=datax[0], length=len(datax[0]))

app.run(debug=True)