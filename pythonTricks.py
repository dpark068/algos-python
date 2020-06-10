def createNestedDic(word):
    """ Can created nested dictionaries with pointers"""

    dic = {}
    pointer = dic
    # iterate through word and add
    for i in word:
        if i not in pointer:
            pointer[i] = {}
            pointer = pointer[i]
    pointer = '-'
    print(dic)


# tests
createNestedDic('apps')