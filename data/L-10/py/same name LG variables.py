def spam():
    eggs = 'spam local'
    print('spam =>', eggs) # 顯示spam eggs
    # bacon() 在這啟動bacon()會造成無限輪迴

def bacon():
    eggs = 'bacon local'
    print('bacon =>', eggs) # 顯示bacon eggs
    spam()
    print('bacon =>', eggs) # 因為bacon還沒結束,所以顯示bacon eggs

eggs = 'global'

bacon()

print('notDef =>', eggs) # def都跑完了,所以執行global eggs

