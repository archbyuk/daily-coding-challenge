# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요

def solution(s, e):
    a = []
    
    for i in range(s, e + 1):
        a.append(i)    
    
    return a