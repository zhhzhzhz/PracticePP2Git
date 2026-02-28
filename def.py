def valid(x):
    for c in x:
        if int(c) % 2 != 0:
            print("Not valid")
            return
        print("Valid")

n = input()
valid(n) 
