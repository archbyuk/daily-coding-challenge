# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다. queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다. my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        while s < e:
            answer[s], answer[e] = answer[e], answer[s]
            s += 1
            e -= 1
            
    return ''.join(answer)

# for s, e in queries: → 각 쿼리마다 뒤집을 시작(s)과 끝(e) 구간을 줌
# 그 안에서 while s < e: → 양쪽에서 한 문자씩 안쪽으로 가면서 서로 교환
# 그래서 s += 1, e -= 1로 서로 가까워지게 하면서 반복
# 이렇게 하면 인덱스 뒤집기랑 같은 효과가 나서 문자열이 뒤집힘

# 근데 풀이 보니까 answer[s:e+1]=answer[s:e+1][::-1]로 했으면 더 간단했을듯