print('def eggs for global variables')

# 因沒定義eggs,會讀取全局變數
def spam():
    print('local eggs =', str(eggs))

# 因有定義eggs,不會讀取全局變數
def abc():
    eggs = 10
    print('has local eggs =', str(eggs))

eggs = 42 # 定義eggs為全局變量

abc()     # 啟動abc()
spam()    # 啟動spam()

print('global eggs =', str(eggs))

