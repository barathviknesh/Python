def fac(num):
    if num ==1:
        return num
    else:
        return num*fac(num-1)
num =int(input("enter number here:"))
fac(num)
print(fac(num))