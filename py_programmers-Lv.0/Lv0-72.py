# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
# 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]

def solution(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    
    return 1

# 내가 풀었을 때는 이렇게 풀었지만 시간 복잡도 최적화 측면에서 조금 더 개선할 수 있다고 한다.

def solution(arr):
    for i in range(arr):
        for j in range(i + 1, arr):  # i 이하 영역은 제외 (중복 방지)
            if arr[i][j] != arr[j][i]:
                return 0
            
    return 1
# 그리고 numpy를 사용하면 더 간단하게 풀 수 있다.
import numpy as np

def solution(arr):
    matrix = np.array(arr)
    return int((matrix == matrix.T).all())

# matrix.T는 전치행렬 (Transpose)
# (matrix == matrix.T).all()은 대칭인지 빠르게 확인 (C 레벨 연산)