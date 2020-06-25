def pal(num):
    x=num[::-1]
    if x == num:
        print ("palindrome")
    else:
        print("not a palindrome")
num=input("ENTER INPUT HERE")
pal(num)