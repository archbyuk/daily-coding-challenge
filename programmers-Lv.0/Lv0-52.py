# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
# 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, is_prefix):
    
    return 1 if my_string.startswith(is_prefix) else 0

# 접두사: 문자열의 시작 부분에서부터 특정 길이까지의 문자열을 의미합니다.
# 접미사: 문자열의 끝 부분에서부터 특정 길이까지의 문자열을 의미합니다.

# 뜻의 차이를 잘 알고 쓰자..허헣...