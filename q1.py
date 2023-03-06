
# ******************************
count = 0
prev = 1
flag = False

for i in range(10):
    num = int(input())
    if num % 2 == 0 and prev % 2 == 0:
        if flag == False:
            count += 1
            flag = True
    else:
        flag = False
    prev = num

print(count)
    
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
