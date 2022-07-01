## https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYFCb80K3PsDFAR7&contestProbId=AV14tDX6AFgCFAYD&probBoxId=AYFCb80K3PwDFAR7&type=PROBLEM&problemBoxTitle=D4&problemBoxCnt=8
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD
## 1223. [S/W 문제해결 기본] 6일차 - 계산기3
## 후위표기식 - stack 활용법


## 참고 강의 영상: https://www.youtube.com/watch?v=Svhp73MIOqY
## 1. 피연산자들 (숫자들)은 오른쪽 (스택이 아닌 다른곳)에 넣음
## 2. 연산자들 (+, *)은 스택에 넣음 
## - 만약 현재 넣으려는 연산자보다 stack에 있는 연산자의 우선순위가 높거나 같으면, 우측으로 이동 시킴 (피연산자들 뒤로) 그 이후에 연산자 스택에 넣음
## 3. 열린 괄호는 무조건 stack에 넣음  
## - 그 이후 닫힌 괄호가 오면 열린/닫힌괄호 둘다 삭제 


"""
## 연산자들 우선순위 정의하는 dictionary 
priority = {'*':3, '/':3, '+':2, '-':2, '(':1}
## 연산자를 저장할 stack을 준비
expr = []
operator = Stack()
result = []
tmp = input('식을 입력하세요: ')


## 띄어쓰기를 제거하여 expr에 저장
for i in tmp:
    if i == ' ':
        continue
    expr.append(i)

## 열린 괄호는 무조건 stack에 넣어줌 
for i in expr:
    if i == '(':
        operator.push(i)
    
    ## 연산자는 stack이 비워있을시 그냥 넣고 
    elif i in '+-*/':
        if operator.is_empty():
            operator.push(i):

        ## 아닐시 stack 가장 위에 있는 연산자의 우선순위와 비교 
        else:
            ## stack에 연산자가 높거나 같다면, list로 빼주고, 연산자 stack에 넣기 
            if priority[operator.peek()] >= priority[i]:
                result.append(operator.pop())
                operator.push(i)
            ## 아닐시 연산자 stack에 넣기
            else:
                operator.push(i)
    
    ## 닫힌 괄호를 만나게되면, stack에 있는 연산자를 모두 뽑아서 결과 list에 넣고, ( ) 는 '삭제' 처리
    elif i == ')':
        while True:
            tmp = operator.pop()
            if temp == '(':
                break
            result.append(tmp)

    ## i가 피연산자라면 결과 list에 바로 넣어주기 
    else:
        result.append(i)  

## 처음 시작을 모두 넘겼다면, stack에 있는 연산자들을 모두 결과 list에 넘겨주기
while not(operator.is_empty()):
    result.append(operator.pop())

print(''.join(result))
"""


# 중위표기식 -> 후위표기식으로 전환 함수
def convert_to_postfix(input):
    global priority 
    result =''
    stack = []
    for i in input:
        if i.isdigit():
            result += i
            continue

        if len(stack) == 0 or i == '(':
            stack.append(i)
            continue

        if i == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
            continue

        while len(stack) and priority[stack[-1]] >= priority[i]:
            result += stack.pop()
        stack.append(i)

    while len(stack):
        result += stack.pop()

    return result


# 후위표기식 -> 숫자로 계산
def postfix_calculate(result):
    stack = []
    for i in result:
        if i.isdigit():
            stack.append(int(i))
            continue
        B = stack.pop()
        A = stack.pop()
        result = 0
        if i == '+':
            result = B + A
        if i == '*':
            result = B * A
        stack.append(result)
    return stack.pop()

## 연산자들 우선순위 정의하는 dictionary 
if __name__ == '__main__':
    priority = {'*':3, '/':3, '+':2, '-':2, '(':1}

    for tc in range(1, 11):
        N = int(input())
        string = input().rstrip()
        result = postfix_calculate(convert_to_postfix(string))
        print('#{} {}'.format(tc, result))



