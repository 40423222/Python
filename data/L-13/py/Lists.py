### Lists 列表
### 注意: 字串要使用''  例用print在Shell上顯示資訊
print("Lists 列表")
print("定義: spam = ['cat', 'bat', 'rat', 'elephant']")
spam = ['cat', 'bat', 'rat', 'elephant']
print('')
print('spam :')
print(spam)
print('')

print('...................................................')
print('')

### 使用Indexes(索引)功能
### 注意: 索引要使用整數 搜尋的整數不能大於定義的範圍
print("使用Indexes(索引)功能")
print("['cat'，'bat'，'rat'，'elephant'] [3] :")
print(['cat', 'bat', 'rat', 'elephant'] [3])
print('')
print('spam [0] :')
print(spam [0])
print('')
print('spam [1] :')
print(spam [1])
print('')
print('spam [2] :')
print(spam [2])
print('')
print('spam [3] :')
print(spam [3])
print('')

print('...................................................')
print('')


### 負整數索引
### 注意: -1代表倒數第一位
print('負整數索引')
print("['cat', 'bat', 'rat', 'elephant'] [-1] :")
print(['cat', 'bat', 'rat', 'elephant'] [-1])
print('')

print('...................................................')
print('')

### 列表在列表的索引
### 就像Arduino矩陣
print("列表在列表的索引")
print("定義: spam = [['cat', 'bat'], [10, 20, 30]]")
spam = [['cat', 'bat'], [10, 20, 30]]
print('')
print('spam [0] [1] :')
print(spam [0] [1])
print('')
print('spam [1] [2] :')
print(spam [1] [2])
print('')

print('...................................................')
print('')

### 列表的Slices(切片)
### 注意: [從前面開始跳過幾個:顯示到第幾位前一個位]
### 注意: 使用這方法顯示會有[]符號
print('列表的Slices(切片)')
print("定義: spam = ['cat', 'bat', 'rat', 'elephant']")
spam = ['cat', 'bat', 'rat', 'elephant']
print('')

print('整數')
print('spam[0:4] :')
print(spam[0:4])
print('')
print('spam[1:3] :')
print(spam[1:3])
print('')

print('負整數')
print('spam[0:-1] :')
print(spam[0:-1])
print('')

### 不輸入數值的一方 將從最頂端開始
print('快速輸入法')
print('spam[:2] :')
print(spam[:2])
print('')
print('spam[1:] :')
print(spam[1:])
print('')

print('...................................................')
print('')

### 列表的索引加字串
print("列表的索引加字串")
print("spam [0], 'eat', spam [2] :")
print(spam [0], 'eat', spam [2])
print('')
print("spam [-4], 'eat', spam [-2] :")
print(spam [-4], 'eat', spam [-2])
print('')

print('...................................................')
print('')

### 利用索引來改變定義值
print("利用索引來改變定義值")
print("定義: changeSpam = ['一號', '二號', '三號', '四號']")
changeSpam = ['一號', '二號', '三號', '四號']
print('')
print('顯示changeSpam [1] :' + changeSpam [1])
print('')
print("更改定義: changeSpam [1] = '零號'")
changeSpam [1] = '零號'
print('')
print('顯示changeSpam [1] :' + changeSpam [1])
print('')

print('...................................................')
print('')

### 列表的連接與複製
### 注意: aSpam [1]得出的是值 不是列表  # 所以必須要加上[] 
### sSpam = aSpam + [aSpam [1]]         # 列表只能連接列表
print("列表的連接與複製")
print("定義: aSpam = ['A', 'BC', 'D']")
aSpam = ['A', 'BC', 'D']
print("定義: bSpam = [12, 3, 45]")
bSpam = [12, 3, 45]
print('')
print("列表連結: sSpam = aSpam + bSpam + aSpam [1]")
sSpam = aSpam + bSpam + [aSpam [1]] # 列表只能連接列表
print('顯示sSpam :' + str(sSpam)) # 列表需要使用str() 來轉為字串
print('')
print("列表複製: sSpam = aSpam*3")
sSpam = aSpam*3
print('顯示sSpam :' + str(sSpam))
print('')

print('...................................................')
print('')

### 刪除列表內容
print("刪除列表內容")
print("定義: delSpam = ['0號', '1號', '2號', '3號']")
delSpam = ['0號', '1號', '2號', '3號']
print("索引刪除: del delSpam [1]")
del delSpam [1]
print("顯示delSpam :" + str(delSpam))
print('')
print("刪除列表: del delSpam")
del delSpam
# print不能顯示沒定義的變數 會發生錯誤
# 所以使用try指令
try:
    print("顯示delSpam :" + str(delSpam))
except NameError:
    print('顯示delSpam :已沒定義不能顯示')
print('')

print('...................................................')
print('')

### len顯示列表長度
print('len顯示列表長度')
print("定義: lenSpam = ['A', 'B', 'C']")
lenSpam = ['A', 'B', 'C']
print('len(lenSpam) :')
print(len(lenSpam))
print('')
print("定義: lenSpam2 = ['0', '1', '2', '3', '4']")
lenSpam2 = ['0', '1', '2', '3', '4']
print('len(lenSpam2) :')
print(len(lenSpam2))
print('')






