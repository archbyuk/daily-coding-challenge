# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

def solution(b, n, m):
    return int (b%(n*m) == 0)

# 이랬는데 틀렸다.
# 이렇게 했어야 했다.
def solution(b, n, m):
    return int(b % n == 0 and b % m == 0)