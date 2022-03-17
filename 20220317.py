#001 화면에 Hello World 문자열을 출력하시오
print('Hello World')

#002 화면에 Mary's cosmetics을 출력하세요. (중간에'가 있음에 주의하세요)
print("mery's cosmeics")

#003 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요)
print('신씨가 소리질렀다. "도둑이야".')

#004 화면에 "C:\windows"를 출력하세요
print('"C:\windows"')

#005 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
print("안녕하세요. \n만나서 \t\t반갑습니다.") #\n은 줄바꿈, \t는 띄어쓰기

#051 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요 (순위정보는 저장하지 않습니다.)
movie_rank=['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

#052 051의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append('배트맨')
print(movie_rank)

#053 movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. '슈퍼맨'을 '닥터 스트레인지'와 ''스플릿'사이에 추가하라.
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

#058 다음 리스트의 합을 출력하라
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#059 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
cook = ['피자', '김밥', '만두', '양념치킨', '족발', '피자', '김치만두', '쫄면', '소시지', '라면', '팥빙수', '김치전']
print('cook리스트의 크키:', len(cook))

#060 다음 리스트의 평균을 출력하라
nums = [1, 2, 3, 4, 5]
print('다음 배열의 평균값:', sum(nums)/5)

#102 아래 코드의 출력 결과를 예상하라
print( 3 == 5) #false

#103 아래 코드의 출력 결과를 예상하라
print( 3<5 ) #True

#104 아래 코드의 결과를 예상하라
x = 4
print( 1< x < 5 ) #True

#105 아래 코드의 결과를 예상하라
print(( 3 == 3) and (4 != 3)) #True