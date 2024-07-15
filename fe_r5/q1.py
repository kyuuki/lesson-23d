# 【 a 】【 b 】に入れる正しい答えを答えてください (試験問題の選択肢から選ばず Python の形式で答えてください)

import math

def findPrimeNumbers(maxNum):
    pnList = []

    for i in range(2, 【 a 】):
        print(i)
        divideFlag = True

        # ↓ j を 2 から i の正の平方根の整数部分まで 1 ずつ増やしている
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            print ("i%j", i % j)
            if 【 b 】:
                divideFlag = False
                break

        if (divideFlag == True):
            pnList.append(i)

    return pnList

# メイン
print(findPrimeNumbers(20))