
def isPalindrome(s):

    s = [int(n) for n in str(s)]

    if s == list(reversed(s)):
        return True
    else:
        return False


complete = False

i = 0
palindromes = []

while not complete:
    if isPalindrome(bin(i)[2:]):
        if isPalindrome(i):
            palindromes.append(i)

    if i == 1000000:
        complete = True

    i+=1
print(palindromes)
print(sum(palindromes))