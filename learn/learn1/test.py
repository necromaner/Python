
print("hello")
print("hello"*8)
print("hello",end="")#end=末尾输出字符，不输入时为换行符

#单行注释
"""多行注释1"""
'''多行注释2'''


# 数据类型：数、字符串、列表（List)、元组(tuple)、集合(set)、字典(dictionry)
# 字符串：引号引起来的就叫字符串,单引号和双引号，三引号意义一样，相当于最后变成一样的
print("\n\n字符串：")
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
print(b[-2])#取取倒数第几个元素，从后数，-1为最后一个
b[0]="abc"#修改某位元素
print(b)
print('.append(插入元素)')#往list中追加元素到末尾
b.append('Adam')
print(b)
print('.insert(位置,插入元素)')#把元素插入到指定的位置
b.insert(3,111)
print(b)
print(".pop(删除位置)")#删除指定位置的元素
b.pop(-1)
print(b)




#元组：存储多个元素的东西(元素0,元素1,元素2)，元组里元素是不可以重新赋值的
print("\n元组：")
c=(1,"aa",2)
print(c)
print(c[0])#取某位元素
#只有1个元素的元组定义时必须加一个逗号,，来消除歧义
t = (1,)#如果不加",",定义的不是元组，是1这个数！这是因为括号()既可以表示元组，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
print(t)
#“可变的”元组
t1 = ('a', 'b', ['A', 'B'])
t1[2][0] = 'X'
t1[2][1] = 'Y'
print(t1)#tuple指向内容没有改变，只改变list的指向

#字典：{键：值，键：值，键：值...}dict
print("\n字典：")
d={"abc":1,"abcd":"aaa",'a':100,1:20,}
print(d)
print(d["abc"])
#取值格式：字典名[对应键名]
print(d[1])#取某键对应的值

d1={"name":"xiaohong","sex":"woman","age":12}
print(d1)
print(d1["name"])

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

print('Thomas' in d)

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas'))
print(d.get('Thomas', -1))
#删除一个key，用pop(key)方法


#集合：去重set
print("\n集合：")
e=set("qqqqweqwasdewgfads")
print(e)
f=set("Afdvcagrfg")
print(f)
print("交集",end=" ")
print(e & f)#交集
print("并集",end=" ")
print(e|f)#并集
print(e-f)#e中有，f中没有的
print(f-e)#f中有，e中没有的
#add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
e.add(1)
print(e)
#remove(key)方法可以删除元素
e.remove(1)
print(e)


#算数运算
print("\n算数运算：")
print(10/3)#有小数
print(10//3)#整数
print(10%3)#余数
#if
print("\nif：")
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

#while
print("\nwhile：")
j=10
while(j>1):
    print(j,end=" ")
    j-=1
print("")
print(j)

#for
print("\nfor：")
h=[1,2,"q","w","e"]
for i in h:
    print(i,end=" ")

print('\n')
for j in range(0,10):
    print(j,end="  ")
print()
for j in range(9,-1,-1):#最后的-1为步长
    print(j,end="  ")
print()
for j in range(9,-1,-2):#最后的-2为步长
    print(j,end="  ")
print()

#break:中断所有循环(提前结束循环)
#continue:中断当前循环(跳过当前的这次循环，直接开始下一次循环

#str()转换成字符串
'''
函数定义的格式
def 函数名(参数):
   函数体
'''
def fan(i):
    print(i)
fan('wew')

#import 模块名
#from ... import ... 从某模块导入某个方法
import cgi
cgi.closelog()

from cgi import closelog
'''
模块的来源：
1、自带模块
2、第三方模块
3、自定义模块
'''

#文件的操作
print("\n文件的操作：")
#open(文件地址，操作形式)
'''
w：写入（直接抹去内容，重新写入）
    w新建只写，w+新建读写，二者都会将文件内容清零
r：读取
    r只读，r+读写，不创建
w+与r+区别：
    r+：可读可写，若文件不存在，报错；
    w+：可读可写，若文件不存在，创建。
b：以二进制进行操作
a：追加操作（不改变文件，在文件末尾追加内容）
a+:追加写入
    a：附加写方式打开，不可读；
    a+: 附加读写方式打开
r+与a+区别：
    fd = open("1.txt",'w+')
    fd.write('123')
    fd = open("1.txt",'r+')
    fd.write('456')
    fd = open("1.txt",'a+')
    fd.write('789')
结果：456789
说明r+进行了覆盖写。

不可读的打开方式：w和a

若不存在会创建新文件的打开方式：a，a+，w，w+

当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
'''
#打开
print("\n打开：")
fh=open("/Users/necromaner/Python/learn/练习文本操作.txt","r")
print(fh.readline(),end=" ------\n")#读取一行
print(fh.read(),end=" ------\n")#读取所有
fh.close()#关闭文件
print(fh)
#写入
print("\n写入：")
fh2=open("/Users/necromaner/Python/learn/练习文本操作.txt","w")#如果没有文本则创建并打开
fh2.write("66666\n")
fh2.write("77777")
fh2.close()#只有关闭了才保存，不关闭，之前将会一直写入内容，直到关闭为止
fh2=open("/Users/necromaner/Python/learn/练习文本操作.txt","w")#关闭后如果从新写入要再执行写入命令
fh2.write("8888\n999\n100")
fh2.close()
fh2=open("/Users/necromaner/Python/learn/练习文本操作.txt","a+")
fh2.write("8888\n999\n100")
fh2.close()

#异常处理
print("\n异常处理：")
#异常处理格式
'''
try:
    程序
except Exception as 异常名称:
    异常处理部分
'''
for i in range(1,10):
    print(i,end=" ")
    try:
        if(i==4):
            print(i)
    except Exception as q:
        print(q,end=" ")
print("")
#类和对象
print("\n类和对象：")
'''
class 类名：
    类里面的内容
'''
#创建一个类
class cl1:
    pass#占位语句，不进行任何操作
print(cl1)
#实例化一个类
a=cl1()
print(a)

# 构造函数（构造方法）
# 类在实例化的时候自动首先触发的方法
#__init__(self,参数)
#self:在类中的方法必须加上self参数
#构造函数实际意义：初始化
class cl2:
    def __init__(self):
        print("---------cl2 self--------")
cl2()
#给类加上参数：给构造方法加上参数
class cl3:
    def __init__(self,name,job):
        print("My name is "+name+",job is "+job)
cl3("xiao","student")

#属性和方法
#属性：静态的特征。如手臂，头发等
#方法：动态的特征。如唱歌、写字等
print("-------------")
#属性：类里面的变量:self.属性名
class cl4:
    def __init__(self,name,job):
        self.myname =name
        self.myjob=job
c=cl4("qwe","asd")
print(c.myname)

#方法：类里面的函数：def 方法名(self,参数名)
class cl5:
    def my(self):
        print("hello")
c=cl5()
c.my()

cl5().my()

class cl5_1:
    def my(self,name):
        print("hello "+name)
c=cl5_1()
c.my("sy")

cl5_1().my("12")
print("----------")
class cl6:
    def __init__(self,name):
        self.myname=name
    def my(self,age):
        print("name is "+self.myname+",age is "+age)
c=cl6("shiyi")
c.my("23")

cl6("shier").my("24")

#继承与重载：
#继承：把m某一个或多个类（基类）的特征拿过来。
#重载：在子类（派生类）里面对继承过来的特征重新定义。
#父类：基类
#子类：派生类

#继承（单继承，多继承）
#例：某一个家庭，父亲，母亲，儿子，女儿，父亲可以说话，母亲可以写字，儿子继承了父亲，女儿继承了父母的能力,并有新能力，听东西，小儿子继承了父亲，但是优化（减弱）了父亲的说话能力
#父亲类
class father:
    def speak(self):
        print("I can speak !")
#母亲类：
class mather:
    def write(self):
        print("I can write !")
#儿子类：单继承：子类（父类）
class son(father):
    pass
#女类：多继承：子类（父类，父类）
class daughter(father,mather):
    def listen(self):
        print("I can listen !")
#小儿子类：(重写：重载）
class son1(father):
    def speak(self):
        print("I can speak English !")
father().speak()
mather().write()
son().speak()
daughter().speak()
daughter().write()
daughter().listen()
son1().speak()









