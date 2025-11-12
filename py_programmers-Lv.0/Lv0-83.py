# 정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

def solution(num_list):
    짝수 = 0
    홀수 = 0
    
    for i in range (1, len(num_list), 2):
        짝수 += num_list[i]
        
    for i in range (0, len(num_list), 2):
        홀수 += num_list[i]
    
    
        
    if 짝수 > 홀수:
        return 짝수
    
    else:
        return 홀수
    
# 슬라이싱으로 풀어보기
def solution(num_list):
    짝수 = sum(num_list[1::2])
    홀수 = sum(num_list[0::2])
    
    return max(짝수, 홀수)