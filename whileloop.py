n = int(input())
while n > 1:
    if n % 2 == 1:
        print("Not even")
        break
    else:
        n = n / 2
print(n)