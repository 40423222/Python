for i in range(5):
    print('i =', i)

try:
    10 / (4-i)
except : # 沒限定錯誤種類
    print('ZeroDivisionError(分母為零)')

try:
    10 / maber
except : # 沒限定錯誤種類
    print('NameError(變數沒定義)')
