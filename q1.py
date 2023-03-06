
# ******************************
num1 = int(input())

while True:
    num2 = int(input())
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        print(num1, num2, end=' ')
        break
    
    num1 = num2

print()
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
