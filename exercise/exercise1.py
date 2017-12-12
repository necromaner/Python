#exercise1:99乘法口诀

print("99乘法口诀:")
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+" * "+str(j)+" = "+str(i*j),end="   ")
    print("")


#逆向输出乘法口诀
print("\n逆向输出乘法口诀:")
print("1.")
for i in range(1,10):
    for j in range(1,11-i):
        print(str(10-i)+" * "+str(j)+" = "+str((10-i)*j),end="   ")
    print("")
print("2.")

for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(i)+" * "+str(j)+" = "+str(i*j),end="   ")
    print("")
