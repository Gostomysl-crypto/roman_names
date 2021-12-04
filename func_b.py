
def isAscending(b):
    # loop for as many digits in the array
    for j in range(len(b)-1):
        # if the next number is less than the previous return false
        if b[j] > b[j+1]:
            return False
    #  did not fail so return true
    return True
