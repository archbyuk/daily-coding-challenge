# 문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

def solution(binomial):
    
    a, op, b = binomial.split()
    
    a = int(a)
    b = int(b)
    
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    
# lambda로 풀어보기
def solution(binomial):
    
    a, op, b = binomial.split()
    a, b = int(a), int(b)

    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }

    return ops[op](a, b)