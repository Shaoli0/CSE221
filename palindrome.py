def palindrome(word):
    n=len(word)
    if n==0:
        x= word + " is not a palindrome"
        return x
    for i in range(0,n//2):
        if word[i] != word[n-1-i]:
            x= word + " is not a palindrome"
            return x
    x= word + " is a palindrome"
    return x
    


print(palindrome("madam"))