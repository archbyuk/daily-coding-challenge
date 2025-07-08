# 두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(q, r, code):
    
    answer = ''
    
    for i in range (len(list(code))):
        if i % q == r: 
            answer += code[i]
    
    return answer

# # 다른 사람 풀이
# def solution(q, r, code):
#     return code[r::q]

# 슬라이싱을 왜 자꾸 생각을 못하지
