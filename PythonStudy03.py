#문자열 처리 함수
#count() | '문자열'.count('a') | 문자열 내에 'a'의 개수를 반환
str1 = "'abcdefga'.count('a') = " + str('abcdefga'.count('a'))
print(str1)

#index() | '문자열'.index('a') | 문자열 내에서 처음으로 나타나는 a의 위치를 반환, a가 없으면 -1 반환
str1 = "'bcda'.index('a') = " + str('bcda'.index('a'))
print(str1)

#join() | 'a'.join('베이스') | '베이스' 문자열 사이사이에 'a'를 넣는다'
str1 = "'a'.join('123') = " + str('a'.join('123'))
print(str1)

#upper() | "문자열".upper() | 문자열의 모든 알파벳을 대문자로 바꾼다.
str1 = "'abc'.upper() = " + str('abc'.upper())
print(str1)

#lower() | '문자열'.lower() | 문자열의 모든 알파벳을 소문자로 바꾼다
str1 = "'ABC'.lower() = " + str('abc'.lower())
print(str1)

#strip() | '문자열'.strip('지울문자') | 문자열 맨앞맨뒤에서 지울문자와 동일한 문제 제거, 지울문자에 스페이스를 넣으면 trim()과 같은 기능
str1 = "'abcdea'.strip('a') = " + str('abcdea'.strip('a'))
print(str1)

#replace() | '문자열'.replace('a','b') | 문자열 내부의 a를 b로 바꾼다
str1 = "'abcde'.replace('a','b') = " + str('abcde'.replace('a','b'))
print(str1)

#split() | '문자열'.split('a') | 문자열을 a를 기준으로 나눈다음 리스트로 반환한다.
str1 = "'abacadaeaf'.split('a') = " + str('abacadaeaf'.split('a'))
print(str1)