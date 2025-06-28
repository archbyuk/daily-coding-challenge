# # 1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.

# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
# 세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.


def solution(a, b, c):
    s = 0
    
    if a == b and b == c and c == a:
        s = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
        
    elif a != b and b != c and c != a:
        s = a + b + c
        
    else:
        s = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    
    return s

# 이렇게 하면 더 좋지 않았을까?
def solution(a, b, c):
    nums = {a, b, c}  # 중복 제거된 집합 생성
    s1 = a + b + c
    s2 = a**2 + b**2 + c**2
    s3 = a**3 + b**3 + c**3

    if len(nums) == 1:       # 세 수가 모두 같음
        return s1 * s2 * s3
    elif len(nums) == 2:     # 두 수만 같음
        return s1 * s2
    else:                    # 모두 다름
        return s1
    
# Set 이렇게 쓰는 거구나