# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요.

# 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.

def solution(arr, idx):
    
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    
    return -1

# 원래는 Idx보다 커야 하는데, '질문하기'보니까 문제가 잘못된듯. 크거나 같아야 함.

# 조금 더 간단하게 풀어보기
def solution(arr, idx):
    
    if 1 in arr[idx:]:
        return arr.index(1, idx)
    
    return -1