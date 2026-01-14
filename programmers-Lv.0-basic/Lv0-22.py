# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(todo_list, finished):
    a = []
    
    for i in range (len(todo_list)):
        if finished[i] == 0:
            a.append(todo_list[i])
            
    return a

# 이렇게 풀었으면 조금 더 좋지 않았을까?
def solution(todo_list, finished):
    return [task for task, done in zip(todo_list, finished) if not done]