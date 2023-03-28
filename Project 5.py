StringOne = input("Enter String: ")
StringTwo = input("Enter String: ")
StringOne = StringOne.lower()
StringTwo = StringTwo.lower()
StringOneSplit = StringOne.split()
StringTwoSplit = StringTwo.split()


def permutation():
    flag = True
    for Values in range(len(StringOneSplit)):
        if StringOneSplit[Values] in StringTwoSplit:
            flag = False
            break
        else:
            StringTwoSplit.remove(StringTwoSplit[Values])
    if flag:
        print('Lists are permutation of each other')
    else:
        print('Lists are different from each other')

permutation()