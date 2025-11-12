# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

# 12 ⊕ 3 = 123
# 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

def solution(a, b):
    answer = 0
    
    answer = 2*a*b if 2*a*b > int(str(a) + str(b)) else int(str(a) + str(b))
    
    return answer

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(a, b):
    ab = int(str(a) + str(b))
    return max(ab, 2 * a * b)

# max 함수는 두 값 중 더 큰 값을 반환한다.