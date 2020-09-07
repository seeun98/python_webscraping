import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()#문제있으면 바로 종료

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) #첫번째 a태그를 보여줘
print(soup.a.attrs) #첫번째 a 태그 속성
print(soup.a["href"])#a 태그 href 속성을 보여줘

#일반적으로 웹스크랩핑의 정보를 잘 모르기 때문에 find를 쓴다.

print(soup.find(attrs={"class":"Nbtn_upload"})) #(  )태그의 조건에 해당하는 정보를 가져온다, 특정정보를 담겨있는 부분
rank = soup.find("li", attrs={"class":"rank01"})
print(rank.a.get_text())
print(rank.next_sibling) #element 다음으로 넘어감. #결과값 아무것도 안나옴
print(rank.next_sibling.next_sibling) #두번 하면 넘어감

rank2 =rank.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank2.a.get_text(), rank3.a.get_text())


rank4 = rank.find_next_sibling("li")
print(rank4.a.get_text())



webtoon = soup.find("a", text = "여신강림-122화")
print(webtoon)
