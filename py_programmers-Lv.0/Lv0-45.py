# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(m, n):
    m_list = list(m)
    a = ''
    
    for i in n:
        a += m_list[i]
        
    return a

# join() 함수를 사용하면 더 간단하게 작성할 수 있다.    
def solution(m, n):
    return ''.join(m[i] for i in n)

# # join() 함수는 문자열을 연결하는 데 사용된다.
# # m[i]는 my_string의 i번째 글자를 의미한다.
# # n은 index_list로, my_string에서 가져올 인덱스들을 나타낸다.
# # ''.join()은 빈 문자열을 기준으로 m[i]의 값을 연결하여 최종 문자열을 생성한다.
# # 이 코드는 my_string에서 index_list의 인덱스에 해당하는 글자들을 순서대로 이어 붙인 문자열을 반환한다.

# ''.join(['a', 'b', 'c'])  # → 'abc'