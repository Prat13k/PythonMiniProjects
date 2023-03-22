Input = int(input("Enter the value "))
MultipleofFive = []
MultipleofSeven = []

def solution():
    sumoffive = 0
    sumofseven = 0

    for Values in range(Input):
        if Values % 5 == 0:
            MultipleofFive.append(Values)
        elif Values % 7 == 0:
            MultipleofSeven.append(Values)
        elif Values % 5 == 0 and Values % 7 == 0:
            MultipleofFive.append(Values)
            MultipleofSeven.append(Values)

    for ValuesTwo in MultipleofFive:
        sumoffive += ValuesTwo

    for ValuesThree in MultipleofSeven:
        sumofseven += ValuesThree

    print(sumoffive + sumofseven)


if Input <= 0:
    print('Not a natural number')
else:
    solution()
