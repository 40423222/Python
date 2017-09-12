### L-15
### 放入L-15內全部的程式
print("L-15內全部的程式")
print('')

print('.............................................')
print('')

### 大發現 中文也能當變數
# 一 = 13
# print(一)

# .....................................................

### index ( )
### 收巡出List內的值
print("收巡出List內的值")
print('index( ):')
print("定義: 對話框 = ['hello', 'hi', 'howdy']")
對話框 = ['hello', 'hi', 'howdy']
# 指令越長 製作成Blog後 字體會變小
# 所以這時就能使用 end = ''
print("對話框.index('hi'): ", end = '')
print('在第', 對話框.index('hi'), '位')
print('')

print("執行: 對話框.index('123'):")
try:
    print(對話框.index('123'))
except ValueError:
    print("錯誤: 因為print內沒有'123'", end = '')
    print(",所以為ValueError:")
print('')

print('.............................................')
print('')

### append and insert
### 添加新的值給列表
print("添加新的值給列表")
print('append( ):')
print("定義: 寵物 = ['dog', 'cat', 'fish']")
寵物 = ['dog', 'cat', 'fish']
print('寵物:', 寵物)
# append( )只能新增在尾端的位子
print("執行: 寵物.append('bird')")
寵物.append('bird')
print('寵物:', 寵物)
print('')

print('insert( ):')
print("定義: 點心 = ['cookies', 'muffin']")
點心 = ['cookies', 'muffin']
print("點心:", 點心)
# insert( )可以選擇新增的位子
print("執行: 點心.insert(1, 'waffle')")
點心.insert(1, 'waffle')
點心.insert(10, '10') # 放超過List內的位子
點心.insert(10, '9')  # 會自動放置在尾端位子
print("點心:", 點心)
print('')

# 這兩指令只能用於List
print("注意: 這兩指令只能用於List")
print("定義: 顏色 = 'white'")
顏色 = 'white'
print("執行: 顏色.append('black')")
try:
    print(顏色.append('black'))
except AttributeError:
    print("錯誤: 因為只能用於List", end = "")
    print("所以為AttributeError")
print('')

print("執行: 顏色.insert(0, 'black')")
try:
    print(顏色.insert(0, 'black'))
except AttributeError:
    print("錯誤: 因為只能用於List", end = "")
    print("所以為AttributeError")
print('')

print('.............................................')
print('')

### remove( )
### 刪除列表中的值
print("刪除列表中的值")
print("remove( ):")
print("定義: 顏色 = ['white', 'black', 'yellow']")
顏色 = ['white', 'black', 'yellow']
print("顏色:", 顏色)
print("執行: 顏色.remove('yellow')")
顏色.remove('yellow')
print("顏色:", 顏色)
print('')

# 要刪除的值在List有重複
# 只會刪除List內最前面的值
print("要刪除的值有重複")
print("定義: 數列 = [1, 1,2, 1]")
數列 = [1, 1,2, 1]
print("數列:", 數列)
print("執行: 數列.remove(1)")
數列.remove(1)
print("數列:", 數列)

print('')

print("要刪除實際存在的值")
print("執行: 顏色.remove('123')")
try:
    顏色.remove(123)
except ValueError:
    print("錯誤: 因為List內沒123,", end = "")
    print("所以為ValueError")

print('.............................................')
print('')

### sort( )
### 排列List內值的順序
### 數字由小到大
### 字母由小寫到大寫 a到z
print('排列List內值的順序')
print("sort( ):")
print("定義: 數列 = ['1', '3', '2']")
數列 = ['1', '3', '2']
print('數列:', 數列)
print('執行: 數列.sort()')
數列.sort()
print('數列:', 數列)
print('')

### 數字跟字串排列
### 要將數字轉為字串
print("數字跟字串排列")
print("定義: 數列 = [1, 3]")
數列 = [1, 3]
print('數列:', 數列)
print("定義: 動物 = ['dog', 'Cat']")
動物 = ['dog', 'Cat']
print('動物:', 動物)
print("執行: sumList = 動物+數列")
sumList = 動物+數列
print('sumList:', sumList)
print("執行: sumList.sort()")
try:
    sumList.sort()
except TypeError:
    print("錯誤: 因為int(整數)跟str(字串)", end = '')
    print('會發生衝突,所以為TypeError')
    print('所以要將整數改為字串')
    print("定義: 數列 = ['1', '3']")
    數列 = ['1', '3']
    print("執行: sumList = 動物+數列")
    sumList = 動物+數列
    print('sumList:', sumList)
    print('執行: sumList.sort()')
    sumList.sort()
    print('sumList:', sumList)
print('')

### 相反的排列
### 數字由大到小
### 字母由小寫到大寫 z到a
print("相反的排列")
print("定義: 動物 = ['dog', 'Cat', 'elephants']")
動物 = ['dog', 'Cat', 'elephants']
print('動物:', 動物)
print('執行: 動物.sort( reverse = True )')
動物.sort( reverse = True )
print('動物:', 動物)
print('')

### 排列中文
### sort( )不是合使用在中文上
### 注意: 中文排列不是ㄅ到ㄦ
print("排列中文")
print("定義: chinese = ['東', '西', '南', '北']")
chinese = ['東', '西', '南', '北']
print('chinese:', chinese)
print('執行: chinese.sort()')
chinese.sort()
print('chinese:', chinese)
print('')

print('.............................................')
print('')
