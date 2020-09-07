import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()#문제있으면 바로 종료

soup = BeautifulSoup(res.text, "")