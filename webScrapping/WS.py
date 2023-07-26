import requests
from bs4 import BeautifulSoup

# url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on" 
url = "https://www.flipkart.com/search?q=IPAD&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page = requests.get(url)
htmlContent = page.content

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify())

# WEB SCRAPPING
name = []
for n in soup.find_all("div",class_="_4rR01T"):
    name.append(n.string.strip())
# print(name)    
# print(len(name))  

price = []
for p in soup.find_all('div',class_='_30jeq3 _1_WHN1'):
    pdash = p.string.strip()
    pdash = pdash.replace('₹','')
    pdash = pdash.replace(',','')
    price.append(int(pdash))

# print(len(price))
# print(price)

# specs = []
# for sp in soup.find_all('ul',class_='_1xgFaf'):
#     specs.append(sp.get_text())

# # print(specs)
# # print(len(specs))

rating = []
for rate in soup.find_all('div',class_='_3LWZlK'):
    if len(rating)<24:
        r = rate.get_text()
        rating.append(float(r))

print(rating)    
print(len(rating))

links = []
for link in soup.select('a',href=True,class_='_1fQZEK'):
    # links.append(link.extract())
    # links.append(link.find('a').attrs['href'])
    # link = link.find('a',href=True)
    # if link is None:
    #    continue
    print(links.append(link['href']))

print(links)    
print(len(links))    


