### Strings with List
### 對字串使用列表的指令
print("對字串使用列表的指令")
print("定義: 螞蟻 = 'Ant'")
print('')

# listName.[nuber]
# 顯示第n位字的字串
print("顯示第n位字的字串")
print("listName.[nuber]:")
螞蟻 = 'Ant'
print("螞蟻[1]:", 螞蟻[1])
print("螞蟻[-0]:", 螞蟻[-0])
# [0:10]確保完全顯示字串的內容
print("螞蟻[0:10]", 螞蟻[0:10])
print('')

# Strings in listName
# 這字是否有在字串內
print("這字是否有在字串內")
print("Strings in listName:")
print("'A' in 螞蟻:", 'A' in 螞蟻)
print("'123' in 螞蟻:", '123' in 螞蟻)
print('')

# for i in listName
# 個別顯示字串的字
print('個別顯示字串的字')
print('for i in listName:')
print('執行: for i in 螞蟻')
n = 0
for i in 螞蟻:
    n = n+1
    print('第' + str(n) + '位字 =', i)

print('.............................................')
print('')








