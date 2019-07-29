import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# *匹配成功返回<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
# *匹配失败返回None
'''
正则表达式
\d可以匹配一个数字，\w可以匹配一个字母或数字，\W非字母数字，\s可以匹配一个空格（也包括Tab等空白符）
.可以匹配任意字符
用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符
要做更精确地匹配，可以用[]表示范围
[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'
^表示行的开头，^\d表示必须以数字开头也就是只匹配开头的abc(雨敲窗的例子)。$表示行的结束，\d$表示必须以数字结束
由于'-'是特殊字符，在正则表达式中，要用'\'转义，同理,;
用()表示的就是要提取的分组Group。比如：^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码
如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来
注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串
正则匹配默认是贪婪匹配，加个？非贪婪匹配（也就是尽可能少匹配）  \d+?
出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤
'''

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# *编译
print(re_telephone.match('010-12345').groups())
'''
match
匹配string 开头，成功返回Match object, 失败返回None，只匹配一个。
search
在string中进行搜索，成功返回Match object, 失败返回None, 只匹配一个。
findall
在string中查找所有 匹配成功的组, 即用括号括起来的部分。返回list对象，每个list item是由每个匹配的所有组组成的list。
'''

m = re.findall("abc", "abcdABc", re.I)
# *不再区分大小写了
print(m)

s = "<div>hello\nworld</div>"
m = re.findall(r"<div>(.*)</div>", s, re.S)
# *匹配换行，也就是整个串看做一行
print(m)
# *输出的是['hello\nworld']

s = "<dIv>hello\nworld</DIV>"
m = re.findall(r"<div>(.*)</div>", s, re.S | re.I)
# *匹配换行且不区分大小写,|位运算符，or逻辑运算符
print(m)


m = re.findall("^abc", "abc\nabc")
print(m)
m = re.findall("^abc", "abc\nabc", re.M)
# *匹配多行
print(m)

m = re.findall("ab?", "abbbbaba")
# *问号表示只匹配0个或者1个
print(m)

m = re.findall("ab+", "abbbbaba")
# *加号匹配一个或者多个
print(m)

m = re.findall("ab*", "aaabbb")
# *星号匹配零个或者多个
print(m)

m = re.findall("\w+@\w+\.org", "7636874@qq.com;763687@qq.org")
print(m)
