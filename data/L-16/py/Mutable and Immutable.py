### Mutable and Immutable
### 可變和不可變的數具類型
print("可變和不可變的數具類型")
print("Mutable and Immutable:")
print("定義: catName = 'Liso a cat'")
catName = 'Liso a cat'
print('')

# 空格不會算在index內
print("catName[5]:", catName[5])
# 但len會算空格
print("len(catName)", len(catName))
print('')

try:
    print("catName[5] = 'the':")
    catName[5] = 'the'
except TypeError:
    print("錯誤: 因為字串不像列表可以改變," +\
          "所以為TypeError")
    # Slices(切片)要包含空格
    # L-13有範例
    print("執行: catName = catName[0:5] + 'the'" +\
          " + catName[6:10]:")
    catName = catName[0:5] + 'the' + catName[6:10]
    print("catName:", catName)
    # 這樣第5位字的a 就會被忽略掉了
print("")

print('.............................................')
print('')

### 列表的變更
print("列表的變更")
print('覆蓋:')
print('定義: 數列 = [1, 2, 3]')
數列 = [1, 2, 3]
print('定義: 數列 = [4, 5, 6]')
數列 = [4, 5, 6]
print('數列:',  數列)
print('[4, 5, 6]覆蓋掉[1, 2, 3]')
print('')

print('改變:')
print('定義: 數列 = [1, 2, 3]')
數列 = [1, 2, 3]
print('先刪除[1, 2, 3]')
print('執行: del 數列[2]')
print('執行: del 數列[1]')
print('執行: del 數列[0]')
del 數列[2]
del 數列[1]
del 數列[0]
print('在使用append( )來新增')
print('執行: 數列.append(4)')
print('執行: 數列.append(5)')
print('執行: 數列.append(6)')
數列.append(4)
數列.append(5)
數列.append(6)
print('數列:', 數列)
print('先刪除列表內的值,再新增要的值')
print("")

print('.............................................')
print('')

### 非List的字串不能被改變
print("非List的字串不能被改變")
print("定義: 值 = ('Value', 1, 0.123)")
值 = ('Value', 1, 0.123)
print("執行: 值[1] = 'noValue'")
try:
    值[1] = 'noValue'
except TypeError:
    print("錯誤: 因為非List的字串不能改變," +\
          "只能覆蓋或改類型")
    print('所以為TypeError')
print('')

print("覆蓋:")
print("定義: 值 = ('覆蓋', '1', '0.123')")
值 = ('覆蓋', '1', '0.123')
print("值:", 值)
print("說明: 用於值數量少時")
print('這樣才好覆蓋')
print('')

print("改類型:")
print('轉成list')
print("執行: 列表值 = list(值)")
列表值 = list(值)
print("列表值:", 列表值)
print("執行: 列表值[0] = '改類型'")
列表值[0] = '改類型'
print("列表值:", 列表值)
print("最後再轉回tuple")
print("執行: 值 = tuple(列表值)")
值 = tuple(列表值)
print(值)
print("說明: 用於值數量太多時")
print('這樣才不用改全部')
print('')

print('.............................................')
print('')
