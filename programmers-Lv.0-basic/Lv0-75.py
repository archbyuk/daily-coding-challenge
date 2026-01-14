# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

def solution(num_list):
    num_list.sort()
    return num_list[:5]

# 처음에는 return에서 sort를 쓰려고 했는데, sort는 리스트를 정렬만 하고, 아무것도 반환하지 않아서 안 되더라