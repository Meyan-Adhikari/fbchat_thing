import wikipedia,requests,bs4,datetime,nepali_datetime
import json
from gtts import gTTS
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--headless")

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

rou={0:"COMP MS\nPHY RP\nCHE GD\nPHY DN\nMATHS KP\nPHY RP\nNEP PC",6:"COMP MS\nMATHS DM\nTEST\nPHY DN\nMATHS KP\nENG GA\nNEP PC",1:"COMP MS\nPHY DR\nCHE JY\nMATHS DM\nMATHS KP\nENG GA\nNEP PC",2:"CHEM JY\nCOMP MS\nPRACTICAL\nPRACTICAL\nPHY DR\nENG GA\nMATHS ND",3:"COMP MS\nCHE KS\nMATHS ND\nCHE JY\nPHY RP\nPRACTICAL\nPRACTICAL",4:"COMP MS\nCHE GD\nCHE KS\nPHY RP\nTEST\nENG GA\nMATHS ND",5:"आज छुट्टि हे मादरचोद"}

def get_s(tx):
    try:
        return wikipedia.summary(tx, sentences=2,auto_suggest=False)
    except:
        return wikipedia.summary(tx, sentences=2,auto_suggest=True)

def get_im(query):
            image_urls = []

            url = "https://bing-image-search1.p.rapidapi.com/images/search"

            querystring = {"q": query, "count": 1}

            headers = {
                'x-rapidapi-host': "bing-image-search1.p.rapidapi.com",
                'x-rapidapi-key': "801ba934d6mshf6d2ea2be5a6a40p188cbejsn09635ee54c45"
            }
            print("sending requests...")
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            print("got response..")
            data = json.loads(response.text)
            img_contents = (data["value"])
            for img_url in img_contents:
                image_urls.append(img_url["contentUrl"])
                print("appended..")
                print(image_urls)
                return image_urls[0]

def rand_quote():

    url = "https://zenquotes.io/"

    b = requests.get(url)
    s = bs4.BeautifulSoup(b.text,'html.parser')
    return (s.find('h1').text)




def joke():
    g = requests.get("https://icanhazdadjoke.com",headers={"Accept":"text/plain"})
    return g.text

def conv_mp3(text,l='en'):
    myobj = gTTS(text=text, lang=l, slow=False)
    myobj.save("welcome.mp3")


def yo_mama():
    a = requests.get("https://yomamma-api.herokuapp.com/jokes?count=1")
    j = a.json()
    return j['joke']

def date():
    return str(datetime.datetime.now())

def nep_date():
    return str(nepali_datetime.datetime.now())

def today_routine():
    return rou[datetime.datetime.today().weekday()]

def tomm_routine():
    if datetime.datetime.today().weekday() ==6:
        return rou[0]
    return rou[datetime.datetime.today().weekday()+1]

def get_pos():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/KEBHS")
    sleep(5)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")


    s = bs(html,'html.parser')
    thing = (s.find(True, {"class":["x126k92a"]}).text)
    driver.quit()
    return thing

def get_pos_ronb():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.facebook.com/officialroutineofnepalbanda")
    sleep(5)
    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")


    s = bs(html,'html.parser')
    thing = (s.find(True, {"class":["x126k92a"]}).text)
    driver.quit()
    return thing

