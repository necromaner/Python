
print("hello")
print("hello"*8)

#单行注释
"""多行注释1"""
'''多行注释2'''


# 数据类型：数、字符串、列表（List)、元组(tuple)、集合(set)、字典(dictionry)
# 字符串：引号引起来的就叫字符串,单引号和双引号，三引号意义一样，相当于最后变成一样的
print("\n字符串：")
a1="abc1 "
a2='abc2 '
a3='''abc3 '''
a4="""abc4 """
print(a1+a2+a3+a4)

# 列表：相当于数组，存储多个元素的东西 [元素0,元素1,元素2]，列表里元素是可以重新赋值的
print("\n列表：")
b=[1,"aa",2]
print(b)
print(b[0])#取某位元素
b[0]="abc"#修改某位元素
print(b)

#元组：存储多个元素的东西(元素0,元素1,元素2)，元组里元素是不可以重新赋值的
print("\n元组：")
c=(1,"aa",2)
print(c)
print(c[0])#取某位元素

#字典：{键：值，键：值，键：值...}
print("\n字典：")
d={"abc":1,"abcd":"aaa",'a':100,1:20,}
print(d)
print('abc')
#取值格式：字典名[对应键名]
print(d[1])#取某键对应的值

d1={"name":"xiaohong","sex":"woman","age":12}
print(d1)
print(d1["name"])

#集合：去重
print("\n集合：")
e=set("qqqqweqwasdewgfads")
print(e)
f=set("Afdvcagrfg")
print(f)
print(e-f)#e中有，f中没有的
print(f-e)#f中有，e中没有的

f1=1
f2=3
if(f1==1 and f2<3):#且用and
    print(f1)
    if(f2==3):
        print(f2)
    if(f1<2):
        print("<")
elif(f2==3):
    print(3)
else:
    print("else\n")

j=10
while(j>1):
    j-=1
print(j)
print('\n')

h=[1,2,"q","w","e"]
for i in h:
    print(i)

print('\n')
for j in range(0,10):
    print(j)

#break:中断所有循环
# continue:中断所有循环

