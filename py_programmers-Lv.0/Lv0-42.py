# 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다.

# 그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다.

# 계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다.

# 임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.

def solution(x):
    a = []
    a.append(x)
    
    while a[-1] != 1:
        if a[-1] % 2 == 0:
            a.append(a[-1] // 2)
        
        else:
            a.append(3 * a[-1] + 1)
    
    return a


# chat gpt가 알려준 개선 방안
# 중복된 인덱스 접근을 최소하해라
# a[-1]`을 반복적으로 사용 → 마지막 값을 변수에 저장해서 읽기 성능 & 가독성 개선

def solution(n):
    sequence = [n]
    
    while sequence[-1] != 1:
        current = sequence[-1]
        next_value = current // 2 if current % 2 == 0 else 3 * current + 1
        sequence.append(next_value)
    
    return sequence