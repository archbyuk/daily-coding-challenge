# 1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은 점수를 얻습니다.

# 네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
# 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점을 얻습니다.
# 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점을 얻습니다.
# 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r점을 얻습니다.
# 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수를 얻습니다.
# 네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.

from collections import Counter

def solution(a, b, c, d):
    answer = [a, b, c, d]
    
    counter = Counter(answer)
    
    keys = list(counter.keys())
    vals = list(counter.values())

    if len(counter) == 1:
        p = keys[0]
        
        return 1111 * p
    
    elif len(counter) == 2:
        
        # 3:1
        if 3 in vals:
            p = keys[vals.index(3)]
            q = keys[vals.index(1)]
            
            return (10 * p + q) ** 2
        
        # 2:2
        elif 2 in vals:
            p, q = keys
            
            return (p + q) * abs(p - q)
    
    elif len(counter) == 3:
        p = None
        q = None
        r = None
        
        for n, v in counter.items():
            if v == 2:
                p = n
            
            elif v == 1:
                if q is None:
                    q = n
                else:
                    r = n
        return q * r
        
    else:
        return min(answer)