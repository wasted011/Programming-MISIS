n = int(input("in_1:"))
counterochn = 0
counterzaochn = 0
def function(a):
    if a == "True":
        return True
    elif a == "False":
        return False
for i in range(n):
    stroka = input(f"in_{i+2}:")
    stroka = stroka.split()
    if function(stroka[3]) == True:
        counterochn += 1
    elif function(stroka[3]) == False:
        counterzaochn += 1
print(f"out: {counterochn} {counterzaochn}")