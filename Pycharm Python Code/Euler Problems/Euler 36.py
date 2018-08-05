def DenToBin(d):
    columns = [128,64,32,16,8,4,2,1]
    bin = [0,0,0,0,0,0,0,0]

    denary = d

    for i in range(0,columns.__len__()):
        fac = divmod(denary,columns[i])[0]
        bin[i] = fac
        denary -= fac * columns[i]

    return  bin

def split_list(a_list):
    half = int(len(a_list)/2)
    return a_list[:half], a_list[half:]

def isPalindrome(s):
    split = []
    split = split_list(s)

    if split[0] == list(reversed(split[1])):
        return True
    else:
        return False
