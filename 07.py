import random
a = random.randint(0 ,100)
print()
for h in range(5):
    m = int(input("number: "))
    if a > m:
        print("adad shoma kochek tar ast!")
    elif a < m:
        print("ada shoma bosorg tar ast!")
    elif a == m:
        print("to bordi")
    elif h == 0:
        print("to bachty")