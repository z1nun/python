#01 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0])
print(letters[2])

#02 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
reversedStr= string[::-1] #[start:stop:step]
print(reversedStr)

#03 Input을 사용하여 특정 문자열 을 오른쪽에서 부터 검색하여 index를 출력하고 kr만 뽑아내서 domain에 저장해서 출력하세요.
url = input("url")
kr = url.rfind("kr")
domain = kr
print(domain)

#04 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = '보고서.xlsx'
print(file_name.endswith('xlsx'))

#05 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'으로 시작하는지 확인해보세요
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#06 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
score = int(input("점수를 입력해주세요."))
if (81 <= score <= 100 ) :
  print("A")
elif (61 <= score <= 80) :
  print("B")
elif (41 <= score <= 60) :
  print("C")
elif (21 <= score <= 40) :
  print("D")
else :
  print("E")

#07 다음 리스트에 저장된 데이터의 개수를 화면에 구해라.
cook = ["피자","김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

#08 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를 아니면 '투자 경고종목이 아닙니다.'를 출력하는 프로그램을 작성하라
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investment_list = input("투자 종목을 말씀해주세요.")

if investment_list in warn_investment_list :
  print("투자 경고 종목입니다.")
else :
  print("투자 경고 종목이 아닙니다.")

#09 다음과 같이 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 for 문을 사용해서 화면에 출력하라. 단 부가세는 10원으로 가정한다.
리스트 = [100, 200, 300]
for i in 리스트 :
  i += 10
  print(i)

#10 리스트에 주식 종목이름이 저장되어 있다. 저장된 문자열의 길이를 다음과 같이 출력하라.
list = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list :
  print(len(i))
