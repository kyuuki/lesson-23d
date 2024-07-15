data = [2, 1, 3, 5, 4]

def sort(first, last):
    pivot = data[(first + last) // 2]  # "//" は商を求める。Java 等は "/" で OK
    i = first
    j = last

    while True:
        while (data[i] < pivot):
            i = i + 1
        
        while (pivot < data[j]):
            j = j - 1

        if (i >= j):
            break

        w = data[i]
        data[i] = data[j]
        data[j] = w

        i = i + 1
        j = j - 1

    print(data)   # *** α ***

    if (first < i - 1):
        sort(first, i - 1)
    
    if (j + 1 < last):
        sort(j + 1, last)

# メイン
# 基本情報技術者試験の疑似言語と配列の数え方が違うので sort(1, 5) ではなく sort(0, 4) になります。
sort(0, 4)

