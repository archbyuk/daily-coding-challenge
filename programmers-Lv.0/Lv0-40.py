# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.



def solution(l, r):
    a = []
    
    for i in range (l, r + 1):
        if all(c in '05' for c in str(i)):
            a.append(i)
        
    return a if a else [-1]

# all() 함수는 주어진 iterable의 모든 요소가 참인지 확인한다.
# str(i)로 i를 문자열로 변환한 후, 각 문자 c가 '0' 또는 '5'인지 확인한다.
# 만약 i가 '0'과 '5'로만 이루어져 있다면, a 리스트에 추가한다.
# 만약 a가 비어 있다면, [-1]을 반환한다.
# 만약 a가 비어 있지 않다면, a를 반환한다.
# 이 코드는 l부터 r까지의 모든 정수를 검사하여, '0'과 '5'로만 이루어진 정수들을 찾아 리스트에 저장하고, 결과를 반환한다.