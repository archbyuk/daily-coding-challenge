# # 정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.

# "w" : 수에 1을 더한다.
# "s" : 수에 1을 뺀다.
# "d" : 수에 10을 더한다.
# "a" : 수에 10을 뺀다.
# 그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.

# 주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.

def solution(numLog):
    answer = ''
    
    key = { 1:'w', -1:'s', 10:'d', -10:'a' }
    
    for i in range (1, len(numLog)):
        d = numLog[i] - numLog[i - 1]
        answer += key.get(d, '')

    return answer

# key.get(d, '')는 d가 key에 없을 때 빈 문자열을 반환합니다.
# 따라서 d가 1, -1, 10, -10이 아닌 경우에는 빈 문자열이 추가됩니다.