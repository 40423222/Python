def spam():
    eggs = 99
    bacon()     # 啟動bacon程式
    print('eggs =', str(eggs))
# 因為bacon執行結束,所以bacon的eggs的定義消失,只剩下spam的eggs,eggs = 99
def bacon():    # 當bacon執行結束,ham跟eggs,的定義將消失
    ham = 101
    eggs = 0    # bacon的eggs只有在,啟動bacon時才有定義

# 啟動spam程式
print('start spam()')
spam()
