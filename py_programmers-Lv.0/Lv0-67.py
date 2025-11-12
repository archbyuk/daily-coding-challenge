# #문제 설명
# 알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요

def solution(myString):
    return ''.join('l' if ord(i) < ord('l') else i for i in myString)

# 이런 문제는 아스키 코드로 비교하는 게 좋음.
# ord() 함수는 문자의 아스키 코드를 반환

# 아스키코드: https://ko.wikipedia.org/wiki/%EC%95%84%EC%8A%A4%ED%82%A4_%EC%BD%94%EB%93%9C