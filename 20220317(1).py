# print("하이")
# print('ab\'c')
# s1 = '화면에 직접 출력'
# s2 = 'ab\'c'
# s3 = 'does'
# print(s1)
# print(s2)
# print(s3)
# print(s3[2])
# print(s3[1:3])
# print(s3[-1]) #마지막 글자
# print(s3[-2]) #마직막에서 두번째 글자
# print('-'*80)
# a = 2
# b = 3.1452
# c = a + b
# print(a)
# print(b)
# print(c)
# print(round(c,3)) #소수점 3번쨰 자리에서 반올림
# print("%.3f" %(c)) #소수점 3자리 반올림
# print(a+b)
# print(a,b,a+b,c)
# d = 1e2
# e =13-2
# print(d)
# print(e)
# print('-'*80)
# item1 = '사과'
# price1 = 1000
# item2 = '바나나'
# price2 = 2000
# print(item1, price1)
# print(item2, price2)
# str1 = '{0}는 {1}원입니다.' #치환
# print(str1.format(item1, price1))
# print(str1.format(item2, price2))
# print(item1, price1, sep=',', end='/') #sep item1, price1 사이에 들어갈 문자, end 마지막에 들어갈 문자
# print(item2, price2)
# str2 = '%s는 %d원입니다.'
# #%s와 %d와 같은 방식으로도 치환이 가능한데
# #%s일 경우는 str(string)타입이 올수 있고
# #%d인 경우에는 int 또는 float 타입이 올 수 있습니다.
# #문자열%(값1, 값2)와 같은 방식으로 표현이 가능

#몫과 나머지를 한번에
print(divmod(5,2))
quotient, remainder = divmod(5,2)
print(quotient, remainder)