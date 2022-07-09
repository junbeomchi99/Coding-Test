# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18GHd6IskCFAZN&categoryId=AV18GHd6IskCFAZN&categoryType=CODE
# 접미어 = suffix = 단어뒤에붙은 글자의 조합
# e.g. monster의 접미어 = onster, nster, ster, ter, er, r

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    word = input()
    word_suffixes = [word[i:] for i in range(len(word))]
    ans = sorted(word_suffixes)[K-1] if K <= len(word) else 'none'
    print('#{} {}'.format(tc, ans))