
#sum
def sum():
    inclement = 1
    ni = int(input("put a number to add: "))
    if ni <= 0:
        print(f"{ni}: number must be greater than zero !")
    elif ni > 0:
        n2 = int(input("put a number to finish: "))
        while inclement <= n2:
            print(f"{ni} + {inclement} = {ni + inclement} ")
            inclement += 1
print(sum())

#less
def less():
    ni = int(input("put a number to decrease: "))
    inclement = ni + 1
    if ni <= 0:
        print(f"{ni}: number must be greater than zero !")
    elif ni > 0:
        n2 = int(input("put a number to finish: "))
        while inclement <= n2:
            print(f"{inclement} - {ni} = {inclement - ni}")
            inclement += 1
print(less())

#multiplication
def multiplication():
    inclement = 1
    ni = int(input("put a number to multiply: "))
    if ni <= 0:
        print(f"{ni}: number must be greater than zero !")
    elif ni > 0:
        n2 = int(input("put a number to finish: "))
        while inclement <= n2:
            print(f"{ni} x {inclement} = {ni * inclement} ")
            inclement += 1
print(multiplication())

#division
def division():
    ni = int(input("put a number to divide: "))
    inclement = ni
    if ni <= 0:
        print(f"{ni}: number must be greater than zero !")
    elif ni > 0:
        n2 = int(input("put a number to finish: "))
        while inclement <= n2:
            print(f"{inclement} / {ni} = {inclement // ni}")
            inclement += ni
print(division())



