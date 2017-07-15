from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve
import sys
page = sys.argv[1]
# Создаём соединение
s = requests.Session() 
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
    })

def load_page_data(page, session):
    url = 'https://geometria.ru/{}'.format(page)
    request = session.get(url)
    return request.text

# Проверяем наличие ссылки на следующую картинку
def contain_next_url(text):
    soup = BeautifulSoup(text, "lxml")
    getUrl = soup.find('a', id="album_next_button").get('href')
    return getUrl is not None

# Загружаем файлы
count = 1
while True:
    data = load_page_data(page, s)
    soup = BeautifulSoup(data, "lxml")
    getUrl = soup.find('a', id="album_next_button").get('href')
    getImg = soup.find('img', id="album_original_photo").get('src')
    if contain_next_url(data):
        imgName = "./{}/img{}.jpg".format(sys.argv[2],count)
        print(getImg)
        print(imgName)
        urlretrieve(getImg,imgName)
        page = getUrl
        count +=1
    else:
            break