# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

def solution(n):
    a = 0
    
    if n%2 == 1:
        for i in range (1, n + 1 , 2):
            a += i
    else:
        for i in range(2, n + 1, 2):
            a += i * i
    return a

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(n):
    if n % 2 == 1:
        return sum(i for i in range(1, n + 1, 2))  # 홀수의 합
    else:
        return sum(i * i for i in range(2, n + 1, 2))  # 짝수의 제곱 합