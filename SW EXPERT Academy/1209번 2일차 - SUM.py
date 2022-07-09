
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(10):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    answer = 0
    for x in range (100):
        row = column = diagonal = reverse_diagonal = 0
        for y in range(100):
            row += arr[x][y]
            column += arr[y][x]
            diagonal += arr[y][y]
            reverse_diagonal += arr[y][99-y]
        answer = max(row, column, diagonal, reverse_diagonal, answer)
    print("#{} {}".format(N, answer))
