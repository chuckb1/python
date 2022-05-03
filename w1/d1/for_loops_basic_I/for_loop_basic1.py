
for x in range(151):
    print(x)


for x in range(5,1001):
    if x % 5 == 0:
        print(x)



for x in range(1,101):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print(" Dojo")
    else:
        print(x)



sum = 0
for x in range(1,500000):
    if x % 2 != 0:
        sum = sum + x
print(sum)


lowNum = ()
highNum = ()
mult = ()


def flexCounter(lowNum, highNum, mult):
    for i in range(lowNum, highNum):
        if i % mult == 0:
            print(i)
flexCounter(2,9,3)    