# 문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, m, c):
    a = []
    r = ''
    
    for i in range(0, len(my_string), m):
        a.append(my_string[i:i + m])
    
    for row in a:
        if c - 1 < len(row):
            r += row[c - 1]
    
    return r

# 다른 사람 풀이
# def solution(s, m, c):
#     return s[c-1::m]

# 와...