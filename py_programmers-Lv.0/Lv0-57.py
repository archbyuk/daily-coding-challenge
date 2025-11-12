# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.

def solution(n, k):
    answer = []
    
    for i in range (1, n + 1):
        if i % k == 0:
            answer.append(i)
    
    return answer

# # 다른 사람 풀이

# def solution(n, k):
#     return [i for i in range(k,n+1,k)]

# k의 배수니까 k부터 n까지 k씩 증가하는 수열을 만들면 되네?