# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my, ps):
    a = []
    
    for str, (s, e) in zip(my, ps):
        a.append(str[s : e +1])
        
    return ''.join(a)

# 시간 복잡도를 비교해봤다.

# result = ''
# for str, (s, e) in zip(my, ps):
#     result += str[s:e+1]

# return result

# 이 방법을 썼을때 문자열 += 연산은 문자열을 새로 복사해서 붙이는 방식이기 때문에 시간 복잡도가 O(n^2)에 가까워질 수 있다.
# 반면에 ''.join(a) 방식은 각 문자열을 리스트에 저장한 후 한 번에 결합하기 때문에 O(n)으로 처리할 수 있다.
# 따라서 ''.join(a) 방식이 더 효율적인 거 같다.

# zip은 딕셔너리보다 더 좋은건가?