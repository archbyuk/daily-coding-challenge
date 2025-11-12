# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.

def solution(n, i):
    a = 0
    
    for r in n:
        if a > i:
            return a
        else: 
            a += r
            
    return a

# 이번 문제로 깨달았다.
# 리스트 컴프리헨션은 조건 누적용에는 적합하지 않다.

# 그리고
def solution(numbers, n):
    a = 0
    for r in numbers:
        a += r
        if a > n:
            return a
        # 이런 식으로 a += r을 먼저 해주면 마지막 값이 n보다 커지는 순간에 a를 리턴할 수 있다.