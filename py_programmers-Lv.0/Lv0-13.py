# 문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(m, k):
    a = ''
    
    for i in range (0, k):
        a += m
    
    return a

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(my_string, k):
    return my_string * k

# 문자열은 * 연산자를 통해서 자동으로 반복시킬 수 있고,
# 성능 면에서도 더 빠르고, 코드 가독성도 좋기 때문에

# 연산자로 해결할 수 있는 건 반복문으로 쓰지 말자.