"""
date: 2025-07-04
author: anil kumar

"""

def ispal(x):
    assert type(x) == list, "x must be a list"
    temp = x.copy()  # Make a copy to avoid mutating the original
    temp.reverse()
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []  # Initialize result before the loop
    for i in range(n):
        elem = input("Enter an element: ")
        result.append(elem)
    print("List entered:", result)
    if ispal(result):
        print("Yes")
    else:
        print("No")

silly(3)



