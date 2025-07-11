# 정수 배열 arr가 주어집니다. arr를 이용해 새로운 배열 stk를 만드려고 합니다.

# 변수 i를 만들어 초기값을 0으로 설정한 후 i가 arr의 길이보다 작으면 다음 작업을 반복합니다.

# 만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
# stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
# stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.
# 위 작업을 마친 후 만들어진 stk를 return 하는 solution 함수를 완성해 주세요.

def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if not stk or stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1
        
        else:
            stk.pop()
                
    return stk

# 처음에는 for문으로 했는데, while로 변경했다.
# 이뉴는 조건에 따라 i를 유연하게 증가시켜야 하기 때문에, for문으로 단순 대체는 어렵기 때문이다.
# i를 없애려면 재귀적으로 처리하거나 스택 외에 임시 상태를 둬야 하는데 오히려 코드 복잡도만 커질 거 같다.