from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
from matplotlib import pyplot as plt
from io import StringIO
# Create your views here.

def scrapper(url):
    page = requests.get(url)
    htmlContent = page.content

    soup = BeautifulSoup(htmlContent,'html.parser')

    # WEB SCRAPPING
    name = []
    for n in soup.find_all("div",class_="_4rR01T"):
        name.append(n.string.strip())

    price = []
    for p in soup.find_all('div',class_='_30jeq3 _1_WHN1'):
        pdash = p.string.strip()
        pdash = pdash.replace('₹','')
        pdash = pdash.replace(',','')
        price.append(int(pdash))


    rating = []
    for rate in soup.find_all('div',class_='_3LWZlK'):
        if len(rating)<24:
            r = rate.get_text()
            rating.append(float(r))

    return {'name':name,'price':price,'rating':rating}      


def home(request):
    return render(request,'home.html',{})


def iphone(request):
    url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on" 
    
    return render(request,'iphone.html',scrapper(url))

def ipad(request):
    url = "https://www.flipkart.com/search?q=IPAD&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    return render(request,'ipad.html',scrapper(url))

def macbook(request):
    url = "https://www.flipkart.com/search?q=macbook&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    return render(request,'ipad.html',scrapper(url))


def downloadIphone(request):
    url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on" 
    df = pd.DataFrame(scrapper(url))
    df.to_csv('ihone.csv',index=True)
    return render(request,'home.html',{})

def downloadIpad(request):
    url = "https://www.flipkart.com/search?q=IPAD&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    df = pd.DataFrame(scrapper(url))
    df.to_csv('ipad.csv',index=True)
    return render(request,'home.html',{})

def downloadMac(request):
    url = "https://www.flipkart.com/search?q=macbook&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    df = pd.DataFrame(scrapper(url))
    df.to_csv('macbook.csv',index=True)
    return render(request,'home.html',{})      

def graph():
    url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on" 
    di = scrapper(url)
    y = di['rating']
    x = di['price']
    fig = plt.figure()
    plt.plot(x,y)
    # plt.bar(x,y)
    # plt.xlabel("Rating's of iphone")
    # plt.ylabel("Price's of iphone")
    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data

def graphIphone(request):
    context = {}
    context['graph'] = graph()
    return render(request, 'graph.html', context)



