def Binary(n):
    ans = ""
    while n > 0:
        ans = str(n % 2) + ans
        n = n // 2
    print(ans)

Binary(10)