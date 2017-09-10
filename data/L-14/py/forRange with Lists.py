### range(someNuber) 可等於 [List]
### range(someNumber) = [someList1, someList2, some.....]
print("range(someNuber) 可等於 [List]")
print("for i in range(4):")
for i in range(4):
    print(i)
print('')

print("for i in [0, 1, 2, 3]:")
for i in [0, 1, 2, 3]:
    print(i)
print('')

print("for i in [0, 2, 3]:")
for i in [0, 2, 3]:
    print(i)
print('')

print("..........................................................")
print('')

### Note 注意 Pthon常見的range範圍定義 range(len([someList]))
### 也就是range是看列表的長度
print("for的range用法: range(len(someList))")
print("先定義: supplies = ['pens', 'staplers', 'flame-throwers', 'binder']")
supplies = ['pens', 'staplers', 'flame-throwers', 'binder']
# 再利用for來得出要顯示的範圍數值並用len訂出最大範圍界線
print('for i in range(len(supplies)):')
print("    print('Index', str(i), 'in supplies is:', supplies[i])")
print('')

print('顯示:')
for i in range(len(supplies)):
    print('Index', str(i), 'in supplies is:', supplies[i])
print('')

print("..........................................................")
print('')

### 利用List來建立operators(運算符號)
### 利用值in列表得出True or False
print("利用List來建立operators(運算符號)")
print("'howdy' in ['hello', 'hi', howdy', 'heyas']:")
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('')

print("定義: spam = ['hello', 'hi', howdy', 'heyas']")
spam = ['hello', 'hi', 'howdy', 'heyas']
print("'cat' in spam:")
print('cat' in spam)
print('')

print("'car' not in spam:")
print('car' not in spam)
print('')

print("..........................................................")
print('')

### 利用List來建立operators(運算符號)的方式
### 寫出一個名稱判斷的程式
print("判斷名稱")
dogName = ['小白', '小黑', '小小']
print('提示: 有', len(dogName), '個小狗名稱')
while True:
    name = input()
    if name not in dogName:
        print('I do not have a pet named ' + name)
        continue
    else:
        print(name, 'is my pet')
        break
print('')

print("..........................................................")
print('')

### 分配多重列表
### 注意: 要是分配數量不對稱 會發生ValueError
### 例: dog, cat = '1', '2'. '3' 會發生ValueError
print("分配多重列表")
print("定義: dog = ['DJ', 'Penky', 'WOW']")
dog = ['DJ', 'Penky', 'WOW']
a = dog[0]
print('a = dog[0]:', a)
b = dog[1]
print('b = dog[1]:', b)
c = dog[2]
print('c = dog[2]:', c)
print('')

print("puppy = ['1', '2', '3']")
puppy = ['1', '2', '3']
print('定義: D, E, F = puppy')
D, E, F = puppy
print('D:', D)
print('E:', E)
print('F:', F)
print('')

print("定義: a, b = 'dog', 'cat'")
a, b = 'dog', 'cat'
print('a:', a)
print('b:', b)
print('a, b = b, a:')
a, b = b, a
print('a:', a)
print('b:', b)
print('')

print("..........................................................")
print('')

### Operators(運算符號)快速輸入法
print("Operators(運算符號)快速輸入法")
print('定義: spam = 40')
spam = 40
print('spam + 1')
spam = spam + 1
print('spam =', spam)
print('')

print("使用快速輸入法")
print('spam +=1')
spam += 1
print('spam =', spam)
print('')

print("除了 + 還可使用 - * / % 這些符號")
print('')

print('定義: roll = LOL ~ ')
roll = 'LOL ~ '
roll *= 3
print('roll *= 3:', roll)
print('')
