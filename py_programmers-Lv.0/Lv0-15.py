# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution(m, n):
    return 1 if m%n == 0 else 0

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(num, n):
    return int(num % n == 0)

# int() 함수는 True를 1로, False를 0으로 변환해준다.
# 따라서 1과 0을 반환하는 것과 동일하다.
# 이 방법이 더 간결하고, 가독성이 좋다.
# 또한, int() 함수는 성능 면에서도 더 빠르다.