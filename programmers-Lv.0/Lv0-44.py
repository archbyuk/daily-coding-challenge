# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

from collections import Counter

def solution(a, b, c, d):
    
    dice = [a, b, c, d]
    
    counts = Counter(dice)
    print("주사위 숫자와 반복수", counts)
    
    key = list(counts.keys())
    print("key(숫자) = ", key)
    
    values = list(counts.values())
    print("values(반복수): ", values)
    
    if len(counts) == 1:
        return 1111 * key[0]
    
    elif sorted(values) == [1, 3]:
        p = key[values.index(3)]
        q = key[values.index(1)]
        
        return (10 * p + q) ** 2
    
    elif sorted(values) == [2, 2]:
        p, q = key
        
        return (p + q) * abs(p - q)
    
    elif sorted(values) == [1, 1, 2]:
        p = key[values.index(2)]
        q = key[values.index(1)]
        q, r = [k for k in key if k != p]
        
        return q * r
    
    else:
        return min(dice)
    
