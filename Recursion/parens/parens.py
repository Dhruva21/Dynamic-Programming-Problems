def addParen(list, leftRem, rightRem, str, index):
    if leftRem < 0 or rightRem < leftRem:
        return 
    if leftRem == 0 and rightRem == 0:
        list.append(str)
    else:
        str[index] = '(' # add left and recurse
        addParen(list, leftRem - 1, rightRem, str, index + 1)
        str[index] = ')' # add right and recurse
        addParen(list, leftRem, rightRem - 1, str, index + 1)
