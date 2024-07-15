def merge(c, d):
    w = []

    # c と d の配列をマージして、w に入れてみてください！
    # w の最後に要素を追加するときは w.append(???) という命令を使います。
    # 2016 の疑似コード C1 に似ています。が、結構違います。

    # 参考: ただただ二つをつなげるだけのコード
    i = 0
    j = 0

    while (i < len(c)):
        w.append(c[i])
        i = i + 1

    while (j < len(d)):
        w.append(d[j])
        j = j + 1

    print(w)

# ここからメイン
c1 = [ 1, 5, 8, 10 ]
d1 = [ 2, 3, 6, 7, 9 ]

merge(c1, d1)