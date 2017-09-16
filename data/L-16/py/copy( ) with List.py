### copy() with List
### 複製列表
print("複製列表")
print("copy() with List:")
import copy
print("定義: 食物 = ['ramen', 'hanburger']")
食物 = ['ramen', 'hanburger']
print("執行: 午餐 = copy.copy(食物)")
午餐 = copy.copy(食物)
print("執行: 午餐[0] = 'coke'")
午餐[0] = 'coke'
print("食物:", 食物)
print("午餐:", 午餐)
print('說明: 使用copy就可以複製出新的List')
print('')

print('.............................................')
print('')
