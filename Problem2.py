input_str = input("enter")

def isPalindrome(input_str):
    return input_str == input_str[::-1]
 

ans = isPalindrome(input_str)
 
if ans:
    print("Yes")
else:
    print("No")