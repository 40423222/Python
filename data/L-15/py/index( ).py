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
    print("錯誤: 因為print內沒有'123',所以為ValueError:")
print('')

print('.............................................')
print('')
