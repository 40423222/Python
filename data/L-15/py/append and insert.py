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
