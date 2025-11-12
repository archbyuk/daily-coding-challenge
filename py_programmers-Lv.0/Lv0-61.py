# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.

def solution(a, d, included):
    
    # 등차수열 값
    result = 0
    
    for i, v in enumerate (included):
        if v == 1:
            result += a + (d * i)
    
    return result


# if v: 를 사용해서 조금 더 파이썬스럽게 작성할 수 있다.
def solution (a, d, included):
    result = 0

    for i, v in enumerate(included):
        if v:
            result += a + d * i

    return result

# 또ㄴ 한 번ㅔ 리스트 컴프리헨션을 사용하여 코드를 간결하게 작성할 수 있다.
def solution(a, d, included):
    return sum(a + d * i for i, v in enumerate(included) if v)

