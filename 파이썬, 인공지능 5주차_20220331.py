#01 아래와 같이 리스트의 데이터를 출력하라. 단 for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)) :
  print(i,price_list[i])

#02 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(1,4) :
  print(90+10*i, price_list[i])


#03 월드컵은 4년에 한 번 개최된다. range()를 사용하여 2002~2050년까지 중 월드컵이 개최되는 연도를 출력하라.
for i in range(2002,2051,4) :
  print(i)

#04 for문을 사용해서 아래와 같이 출력하라.
numList = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for i in range(len(numList)) :
  print(numList[i])

#05 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
ticker = "btc_krw"
print(ticker.upper())

#06 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx")) #True

#07 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split())

#08 다음과 같이 날자를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
print(date.split('-'))

#09 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
상장주식수 = "5,969,782,550"
상장주식수1 = 상장주식수.replace(",","")
상장주식수2 = int(상장주식수1)
print(상장주식수2)
print(type(상장주식수2))

#10 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
print(a.split())

#11 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트: 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#12 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])
  
#13 for문을 사용해서 3의 배수만을 출력하라.
리스트 = [3, 100, 23, 44]
for i in 리스트 :
  if (i%3==0) :
    print(i)