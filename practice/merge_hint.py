def merge(c, d):
    w = []

    # c と d の配列をマージして、w に入れてみてください！
    # ??? の部分を埋めてみてください
    i = 0
    j = 0

    while (i < len(c) or j < len(d)):
        if (j >= len(d) or ??? < ???):
            w.append(???)
            i = i + 1
        else:
            w.append(???)
            j = j + 1

    print(w)

# ここからメイン
c1 = [ 1, 5, 8, 10 ]
d1 = [ 2, 3, 6, 7, 9 ]

merge(c1, d1)