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
