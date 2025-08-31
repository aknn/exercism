def append(list1, list2):
    return list1 + list2

def concat(lists):
    result = []
    for l in lists:
        result += l
    return result

def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result

def length(list):
    count = 0
    for _ in list:
        count += 1
    return count

def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result

def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc

def foldr(function, list, initial):
    acc = initial
    for item in reverse(list):
        acc = function(acc, item)
    return acc

def reverse(list):
    result = []
    for item in list:
        result.insert(0, item)
    return result
