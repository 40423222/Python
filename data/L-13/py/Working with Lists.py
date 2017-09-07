### 手動輸入列表
print("手動輸入列表")
catNames = []
catNumber = 0
while True:
    catNumber = catNumber + 1
    print("輸入" + str(catNumber) + "號catNames 直接案Enter會產生列表")
    inputNames = [input()]
    if inputNames == ['']:
        break
    catNames = catNames + inputNames
print("catNames列表 :")
print(catNames)
print('')

# for能使用在列表上
# emptyBox不用定義 這是用來裝catNames列表
catNumber = 0 # 之前的記錄要洗去
print('貓的名子')
for emptyBox in catNames:
    catNumber = catNumber + 1
    print(str(catNumber) + '號貓: ' + str(emptyBox))

