# 정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요

def solution(arr, delete_list):
    answer = []
    
    for i in arr:
        if i not in delete_list:
            answer.append(i)
            
    return answer

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(arr, delete_list):
    return [x for x in arr if x not in delete_list]