T = int(input())
for tc in range(1,1+T):
    k = int(input())
    word = input()
    result = []
    for q in range(len(word)):
        for w in range(len(word)):
            if w+q+1 <= len(word):
                result.append(word[w:w+q+1])
    #set ㅎㅏㅁㅅㅜㄹㅡㄹ ㅌㅗㅇㅎㅏㅇㅕ ㅈㅜㅇㅂㅗㄱ ㅈㅔㄱㅓ
    result = list(set(result))
    result.sort()
    if len(result) > k-1:
        print('#{} {}'.format(tc,result[k-1]))
    else:
        print('#{} {}'.format(tc,'none'))