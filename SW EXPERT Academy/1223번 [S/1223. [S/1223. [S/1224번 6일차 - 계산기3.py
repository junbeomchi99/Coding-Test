for tc in range(10):
    N = int(input())
    tmp = input()
    exp = []
    operator = []
    result = []

# 중위표기식 -> 후위표기식으로 전환 함수
    for i in range(N):
        if tmp[i].isdigit():
            exp.append(int(tmp[i]))
        else:
            if tmp[i] == ')':
                chk = ''
                # 우선순위가 가장 높은 '('를 찾을때까지
                while chk != '(':  
                    chk = operator.pop()
                    exp.append(chk)
                 # exp의 마지막에 '('가 들어가버렸으므로 pop으로 제거 
                exp.pop() 
                continue
            elif tmp[i] == '*':
                # '('가 * 보다 우선순위가 높아서, 뽑아낼수없음
                while operator and operator[-1] == '*' and operator[-1] != "(":  
                    exp.append(operator.pop())
            elif tmp[i] == '+':
                # '('는 '+'보다 우선순위가 높아서, 뽑아낼수없음
                while operator and operator[-1] != "(":  
                    exp.append(operator.pop())
            operator.append(tmp[i])

    while operator:  # operator가 비어있지 않으면, 모두 비워서 exp에 넣기
        exp.append(operator.pop())

# 후위표기식 -> 숫자로 계산
    for i in exp:
        if i in range(0, 10):
            result.append(i)
        else:
            if i == "+":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 + p1)
            elif i == "*":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 * p1)

    print(f'#{tc+1} {result[-1]}')