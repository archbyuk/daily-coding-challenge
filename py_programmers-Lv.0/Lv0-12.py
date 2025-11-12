# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

def solution(s1, s2):
    a = ''
    
    for i in range (len(s1)):
        a += s1[i]  + s2[i]
        
    return a

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(s1, s2):
    return ''.join(a + b for a, b in zip(s1, s2))