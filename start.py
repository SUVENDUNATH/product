user=int(input("enter a number"))
if user%2==0:
    print("even")
else:
    print("add")
    
def palindrome(word):
    return word == word[::-1]