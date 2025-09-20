from typing import *

# Test Sets
numbers0 = [] # Empty lists are ascending
numbers1 = [0] # Single int or float lists are ascending
numbers2 = [1,-2,3]
numbers3 = [1,2]
numbers4 = [1,1,1] # Multiple entries do not count as ascending
    

def isAscending(numberList: list[int, float])->bool:

    # Checks that input is a list
    if not isinstance(numberList, list):
        raise TypeError("Value must be type list")
    
    # Checks for empty lists to return true
    if len(numberList) == 0:
        return True
    
    # Checks for valid data type in list
    if not all(isinstance(number, (int, float)) for number in numberList):
        raise TypeError("List must contain only Int and Float instances")
    
    # Checks for single value list to return true
    if len(numberList) == 1:
        return True

    # Checks ensuring the list contents are ascending
    num1 = 1
    num2 = 0

    while num1 < len(numberList):
        if numberList[num2] >= numberList[num1]:
            return False
        num1 += 1
        num2 += 1
    return True

def main():
    print(isAscending(numbers0))
    print(isAscending(numbers1))
    print(isAscending(numbers2))
    print(isAscending(numbers3))
    print(isAscending(numbers4))

main()