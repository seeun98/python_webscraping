import requests
res = requests.get("http://navers.com") #정보 담아와서 출력할 수있음
print("응답코드 : ", res.status_code) #200이면 정상

if res.status_code == requests.codes.ok:
    print("정상입니다")
else:
    print("문제가 생겼습니다");