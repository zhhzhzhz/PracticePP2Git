a = [1, 2, 3, 4,5 ,6,7]
for x in a:
    print(x)
    if x == 4:
        continue


thislist = ["apple", "banana", "cherry"]
print("Size:", len(thislist))
print(type(thislist))
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(*thislist)


b = [0,1,2 , 3, 4 ,5 ,6, 7, 8]
s = 0 
for c in b:
    if c == 5:
        s = s + 1
print(s)