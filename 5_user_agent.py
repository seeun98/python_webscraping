#사람이 접속하지 않고 웹크롤링이나 웹스크랩핑의 경우 페이지 입장에서 과부하가 올 수 있어
#user_agent를 이용
import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get(url, headers=headers) #정보 담아와서 출력할 수있음
#res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f .write(res.text)

#우리가 받아온 페이지에는 접속하는 것이 이상항 컴퓨터라 올바른 정보를 주지 않는 것임
#header 정보(유저 에이전트)를 이용해 가져와야 웹크롤링처럼 정보 그대로 가져올 수 있음