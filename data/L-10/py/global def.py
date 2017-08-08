# 將eggs定義為spam全局變數
def spam():
    global eggs
    eggs = 'spam'

# spam() # 要是不放置在eggs下方,global eggs就會被洗去

eggs = 'global'

spam() # 放置這防止被eggs = 'global'洗去

print(eggs)

