"""

두 정수 X, Y의 읨의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을
이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝궁이라고 한다.

# 여기서 짝지을 수 있다는 건 예를 들어, X=3403, Y=13203이라면
# 두 수에서 공통으로 나타나는 3과 0을 이용하여 짝궁 303을 만들 수 있다는 뜻임.

if X, Y의 짝궁이 존재한다면,
    result = -1

elif X, Y의 짝궁이 only 0이라면,
    result = 0

else:
    result = 짝궁인데 짝궁으로 만들 수 있는 수 중에 가장 큰 수


"""

from collections import Counter

def solution(x, y):
    arr_x = list(x)
    arr_y = list(y)
    
    # 일단 여기서 정수를 리스트로 쪼개
    
    count_x = Counter(arr_x)
    count_y = Counter(arr_y)
    
    """
    
    count_x = Counter({'0': 2, '1': 1})
    count_y = Counter({'1': 1, '2': 1, '3': 1, '4': 
    1, '5': 1, '0': 1})
    
    """
    
    setting = count_x & count_y
    
    # setting = Counter({'1': 1, '0': 1})
    
    elements_list = list(setting.elements())

    # if max(elements_list[]) == 0:
    #     return False
    
    
    result = ''.join(sorted(elements_list, reverse = True))
    
    
    if len(result)  == 0:
        return "-1"
    
    elif int(result) < 1:
        return "0"
    
    
    return result

# 몇 개의 테스트 케이스에서 시간 초과가 발생함.
# sorted() 함수가 문제인 것 같은데...
# sorted()로 정렬한 후에 새 리스트를 만드는 게 아닌 for문으로 하나씩 비교하면서 하면

# 최적화 코드: sorted()를 사용하지 않고 for문으로 직접 각 자리 숫자가 몇 개가 나왔는지 확인하는 방법

from collections import Counter

def solution(x, y):
    arr_x = list(x)
    arr_y = list(y)
    
    count_x = Counter(arr_x)
    count_y = Counter(arr_y)

    result = ''

    for i in range(9, -1, -1):

        common_count = min(count_x(str(i)), count_y(str(i)))
        # 이렇게 하면 각 'n'이 몇 개씩 공통으로 있는지를 검사하고, 작은 개수를 common_count에 저장함.

        result += str(i) * common_count
        # 그리고 그 개수만큼 result에 추가함.

    if len(result)  == 0:
        return "-1"
    
    elif int(result) < 1:
        return "0"
    
    
    return result

# 왜 sorted()보다 for문이 더 빠를까
"""
sorted() 함수는 내부적으로 Timsort 알고리즘을 사용하며, 
이는 평균적으로 O(n log n)의 시간 복잡도를 가진다고 한다.

반면에 for문을 사용하여 각 자리 숫자를 직접 확인하는 방법은
고정된 범위(0부터 9까지) 내에서 반복하기 때문에 O(1)의 시간 복잡도를 가진다.

"""