# 문자열 myString과 pat가 주어집니다. myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return 하는 solution 함수를 완성해 주세요.

def solution(myString, pat):

    idx = myString.rfind(pat)

    return myString[:idx + len(pat)]

# rindex
def solution(myString, pat):

    idx = myString.rindex(pat)

    return myString[:idx + len(pat)]

# rfind: 문자열에서 마지막으로 등장하는 부분 문자열의 시작 인덱스를 반환, 패턴을 찾지 못하면 -1을 반환
# rindex: 문자열에서 마지막으로 등장하는 부분 문자열의 시작 인덱스를 반환, 패턴을 찾지 못하면 ValueError를 발생시킴