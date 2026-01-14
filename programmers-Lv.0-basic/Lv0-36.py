# 정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e, k] 꼴입니다.

# 각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 k보다 크면서 가장 작은 arr[i]를 찾습니다.

# 각 쿼리의 순서에 맞게 답을 저장한 배열을 반환하는 solution 함수를 완성해 주세요.
# 단, 특정 쿼리의 답이 존재하지 않으면 -1을 저장합니다.

def solution(arr, queries):
    a = []
    
    for s, e, k in queries:
        b = []
        for i in range (s, e+1):
            if arr[i] > k:
                b.append(arr[i])
        
        if not b:
            a.append(-1)
        else:
            a.append(min(b)) 
                
    return a

# 이렇게 풀었다면 더 좋았을 것.
def solution(arr, queries):
    result = []
    for s, e, k in queries:
        # arr[s]부터 arr[e]까지 중 k보다 큰 값만 골라서
        candidates = [v for v in arr[s:e+1] if v > k]
        # 후보가 있으면 최솟값, 없으면 -1
        result.append(min(candidates) if candidates else -1)
    return result