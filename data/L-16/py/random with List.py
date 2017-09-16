### random with List
### 隨機顯示列表內容
print("隨機顯示列表內容")
print('帶入random模組')
print("執行: import random")
import random
# 原來列表可以不用一行打完
print("定義: 心情 = ['It is happy',")
print("            'It is sad',")
print("            'It is angry',")
print("            'It is calm']")
心情 = ['It is happy',
      'It is sad',
      'It is angry',
      'It is calm']
n = 3
print("顯示", n, "個心情:")
for i in range(n):
    print(心情[random.randint(0, len(心情)-1)])
print('')

print('.............................................')
print('')
