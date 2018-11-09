#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
print('小明的成绩从去年的%d分提升到了今年的%d分，小明成绩提升%.1f%%'%(72,85,72/85))

#请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

'''
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

    低于18.5：过轻
    18.5-25：正常
    25-28：过重
    28-32：肥胖
    高于32：严重肥胖

用if-elif判断并打印结果：
'''
h=1.75
g=80.5
BMI=g/(h*h)
if(BMI<18.5):
    print("过轻")
elif(BMI<25):
    print("正常")
elif(BMI<28):
    print("过重")
elif(BMI<32):
    print("肥胖")
else:
    print("严重肥胖")


#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L1 = ['Bart', 'Lisa', 'Adam']
for i in L1:
    print(i)

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。

提示：计算平方根可以调用math.sqrt()函数：
'''
import math
def quadratic(a, b, c):
    a1=b*b-4*a*c
    if(a1<0):
        return False,False
    x1=(-b+math.sqrt(a1))/(2*a)
    x2=(-b-math.sqrt(a1))/(2*a)
    # print(x1)
    return x1,x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

