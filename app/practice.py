import requests
from bs4 import BeautifulSoup

#  Page Urls
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
url2 = 'https://parade.com/1208432/marynliles/this-or-that-questions/'
url3 = 'https://snacknation.com/blog/would-you-rather-questions/'
url4 = 'https://conversationstartersworld.com/first-date-questions/' 
url5= 'https://positivepsychology.com/introspection-self-reflection/'
url6= 'https://parade.com/966617/parade/never-have-i-ever-questions/'
url7 = 'https://conversationstartersworld.com/yes-or-no-questions/'
url8 = 'https://conversationstartersworld.com/questions-for-couples/'
url9 = 'https://conversationstartersworld.com/most-likely-to-questions/'
url10 = 'https://conversationstartersworld.com/icebreaker-questions/'

# Requests to get website data
page2= requests.get(url2)
page3 = requests.get(url3)
page4= requests.get(url4)
page5 = requests.get(url5)
page6 = requests.get(url6)
page7 = requests.get(url7)
page8 = requests.get(url8)
page9 = requests.get(url9)
page10 = requests.get(url10)

# Check if page is able to be scraped
# print(page10)

soup2 = BeautifulSoup(page2.content, "html.parser")
soup3 = BeautifulSoup(page3.content, "html.parser")
soup4 = BeautifulSoup(page4.content, "html.parser")
soup5 = BeautifulSoup(page5.content, "html.parser")
soup6 = BeautifulSoup(page6.content, "html.parser")
soup7 = BeautifulSoup(page7.content, "html.parser")
soup8 = BeautifulSoup(page8.content, "html.parser")
soup9 = BeautifulSoup(page9.content, "html.parser")
soup10 = BeautifulSoup(page10.content, "html.parser")

# print(soup6)

# Scraping the specific content I need
looking_url3 = soup3.find_all('h4')
looking_url2 = soup2.find_all('p')
looking_url4 = soup4.find_all('li')
looking_url5= soup5.find_all('li')
looking_url6= soup6.find_all('p')
looking_url7= soup7.find_all('p')
looking_url8= soup8.find_all('li')
looking_url9= soup9.find_all('li')
looking_url10= soup10.find_all('li')
# print(looking_url10)

# >>>>>>>>>> Loops to grab each question <<<<<<<<

# would you rather questions deck
would_you_rather = []
for item in looking_url3:
    question = {"card": item.text}
    would_you_rather.append(question)
# print(would_you_rather)

# this or that questions deck
this_or_that = []
for item in looking_url2:
  question = {"card": item.text}
  this_or_that.append(question)
# print(this_or_that)

first_date = []
for item in looking_url4:
    question = {"card": item.text}
    first_date.append(question)
# print(first_date)

# Self reflection questions
self_reflection = []
for item in looking_url5:
    question = {"card": item.text}
    self_reflection.append(question)
# print(self_reflection)

# Never Have I ever questions
never_have_i_ever = []
for item in looking_url6:
    question = {"card": item.text}
    never_have_i_ever.append(question)
# print(never_have_i_ever) 

# Yes or No questions
yes_or_no = []
for item in looking_url7:
    question = {"card": item.text}
    yes_or_no.append(question)
# print(yes_or_no) 

# Questions for couples
couples_qs = []
for item in looking_url8:
    question = {"card": item.text}
    couples_qs.append(question)
# print(couples_qs) 

# Most Likely To
most_likely_to = []
for item in looking_url9:
    question = {"card": item.text}
    most_likely_to.append(question)
# print(most_likely_to) 

# Icebreaker questions
icebreakers = []
for item in looking_url10:
    question = {"card": item.text}
    icebreakers.append(question)
# print(icebreakers) 

# Firebase Credentials

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/Users/makeeshapruitt/Downloads/questions-unanswered-firebase-adminsdk-mc2dn-62ca1d4df6.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def save(collection_id, data):
    db.collection(collection_id).add(data)


# for card in icebreakers:
#     save(
#         collection_id = "Icebreakers",
#         data=card
#     )


# docs = db.collection(u'ListofCollections').stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
# docs = db.collection(u'Never have I ever').stream()
# array = []
# for doc in docs:
#     cards = doc.to_dict()
#     array.append(cards['card'])
# print(array)
    # print(cards['card'])
    
    