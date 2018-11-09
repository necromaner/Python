
#r''表示''内部的字符串默认不转义
print("r''")
print('\\\t\\')
print(r'\\\t\\')

#'''...'''的格式表示多行内容
print("\n'''...'''")
print('''line1
line2
line3''')

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print('\nord()')
print(ord('A'))
print('\nchr()')
print(chr(66))

print('\u4e2d\u6587')
print('中文')

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('\nencode()')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# '中文'.encode('ascii')

#把bytes变为str，就需要用decode()方法
print('\ndecode()')
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print('\nerrors=\'ignore\'')
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

#计算str包含多少个字符，可以用len()函数：
print('\nlen()')
print('ABC %s' %len('ABC'))
print('b\'ABC\' %s'%len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
print('\n')

# 占位符 	替换内容
# %d 	整数
# %f 	浮点数
# %s 	字符串
# %x 	十六进制整数
print('%3d+%4s'%(3,'qwe'))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('Age: %s. Gender: %s' % (25, True))

#字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)

#另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
print('\nformat()')
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#input()读取用户的输入
'''
print("input()")#input()返回的数据类型是str
s = input('birth: ')
birth = int(s)#强转
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
