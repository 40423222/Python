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

