import re
p = re.compile("ca.e")

def print_match(m):
    if m:
        print("m.group()",m.group()) #일치하는 문자열 반환
        print("m.string:", m.string) #입력받은 문자열
        print("m.start()", m.start()) #일치하는 문자열의 시작 index
        print("m.span():", m.span()) #일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

   # m = p.match("caselass") #주어진 문자열의 처음부터 일치하는지 확인하므로 ca.e와 맞음
   # print_match(m)

m = p.search("careless") #search : 주어진 문자열 중에 일치하는게 있는지 확인

lst = p.findall("careless") #findall: 일치하는 모든 것을 리스트 형태로 변환
print(lst)




#1. p = re.comile("원하는 형태")
#2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
