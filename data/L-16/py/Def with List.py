### Def with List
### 用def添加值給List
print("用def添加值給List")
print("Def with List:")
print("建立: def 動物(someParameter):")
def 動物(someParameter):
    import random
    i = random.randint(1, 5)
    if i == 1:
        someParameter.append('dog')
    if i == 2:
        someParameter.append('fish')
    if i == 3:
        someParameter.append('cat')
    if i == 4:
        someParameter.append('bird')
    if i == 5:
        someParameter.append('crocodile')
print("定義: 數列 = [1, 2, 3]")
數列 = [1, 2, 3]
print("執行: 動物(數列)")
動物(數列)
print('')

print("結果:")
print("動物:", 動物)
print("數列:", 數列)
print("說明: 利用def建議給List值的程式")

print('.............................................')
print('')
