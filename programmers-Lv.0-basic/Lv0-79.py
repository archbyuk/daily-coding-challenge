# 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.

def solution(strArr):
    
    answer = []
    
    for i in strArr:
        if "ad" not in i:
            answer.append(i)
        
    
    return answer

# not in을 잘 사용하자. a not in b는 b에 a가 없다는 뜻!