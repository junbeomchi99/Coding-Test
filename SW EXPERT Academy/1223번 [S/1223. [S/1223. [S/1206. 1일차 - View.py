# https://swexpertacademy.com/main/code/problem/problemSolver.do?contestProbId=AV134DPqAA8CFAYh
# 1206. [S/W 문제해결 기본] 1일차 - View

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# 첫번째 input = 땅의 가로 길이 
# 두번쨰 input = 아파트의 높이 list
for test_case in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))

    view_total = 0
    for i in range(2, N-2):
        left_2 = building[i] - building[i-2]
        left_1 = building[i] - building[i-1]
        right_1 = building[i] - building[i+1]
        right_2 = building[i] - building[i+2]
        if left_2 > 0 and left_1 > 0 and right_1 > 0 and right_2 > 0 :
            view_total += min(left_2, left_1, right_1, right_2)

    print("#{} {}".format(test_case,view_total))
