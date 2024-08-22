def Binary1(n):
    if n < 2:
        return str(n)
        # return str(n % 2)

        # どっちでもいいはず。
        # str(n) の方が無駄な計算がなくてシンプル。
        # str(n % 2) の方が Binary1(n // 2) + str(n % 2) の先頭部分がなくなっている意味をよく表している。
    return Binary1(n // 2) + str(n % 2)
    
print(Binary1(10))