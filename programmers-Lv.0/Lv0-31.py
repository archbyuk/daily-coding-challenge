# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    a = 0
    
    p = '' # 홀수합
    q = '' # 짝수합
    
    for i, v in enumerate(n):
        if v % 2 != 0:
            p += str(v)
        
        else:
            q += str(v)
            
    return int(p) + int(q)

# 