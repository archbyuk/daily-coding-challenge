# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, queries): 
    m = list(my_string)    
    
    for s, e in queries:
        print(s, e)
        save = m[s]
        m[s] = m[e]
        m[e] = save 
        
    return ''.join(m)

# 틀림.. 문제 이해를 잘못함. 슬라이싱 기준으로 s ~ e + 1까지를 뒤집어서 교체하라는 건데,
# s 랑 E + 1이랑 바꾸라는줄.

def solution(my_string, queries): 
    m = list(my_string)
    
    for s, e in queries:
        print(s, e)
        m[s: e + 1] = m[s:e+1][::-1]

    return ''.join(m)

# 답은 이거임. 

# [::-1] 은 자주 쓸듯