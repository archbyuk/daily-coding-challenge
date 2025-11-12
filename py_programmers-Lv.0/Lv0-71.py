# 정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(n_str):
    return str(int(n_str))

# 다른 사람 풀이를 봤는데 이런 게 있었다.
def solution(n_str):
    return n_str.lstrip('0')

# str.lstrip([chars]) -> 문자열에서 왼쪽에 있는 문자들을 전부 제거한 문자열을 반환

# 그럼 둘에 시간복잡도는 누가 더 빠를까?
# 첫 번째 방법은 int로 변환하는 과정이 있기 때문에 O(n)이라고 볼 수 있다.
# 두 번째 방법은 str.lstrip()이 내부적으로 O(n)으로 구현되어 있기 때문에 O(n)이라고 볼 수 있다.
# 따라서 두 방법 모두 시간복잡도는 O(n)이다. 근데 두 번째가 더 빠름

# 하지만 두 번째 방법이 더 간결하고 가독성이 좋기 때문에 추천한다.