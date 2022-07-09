T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def convert_num(n):
    dict = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    return dict[n]

def code_location(word):
    for i in range(N):
        for j in range(M-1, 0, -1):
            if info[i][j]:
                line = i
                idx = j
                return line,idx

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    info = [list(map(int, input())) for _ in range(N)]

    line = code_location(info)[0]
    idx = code_location(info)[1]

    code = info[line][idx-55:idx+1]
    result = ''

    for i in range(0, len(code), 7):
        tmp = ''
        for j in range(i, i+7):
            tmp += str(code[j])
        result += convert_num(tmp)
    odd = 0
    even = 0

    for i in range(7):
        if i%2:
            even += int(result[i])
        else:
            odd += int(result[i])
    validation = odd * 3 + even + int(result[7])

    if validation % 10:
        total = 0
    else:
        total = 0
        for i in range(8):
            total += int(result[i])
    
    print("#{} {}".format(test_case,total))
