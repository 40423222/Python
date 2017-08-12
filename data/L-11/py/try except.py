# 定義spam並設變數
def spam(divideBy):
    # try內發生錯誤,執行except
    try:
        return 42 / divideBy
    except ZeroDivisionError: # 打上錯誤的名稱
        print('Error: Invalid argument.')

# spam(數字),數字 = divideBy,並啟動spam
print(spam(2))
print(spam(12))
print(spam(0)) # 分母為零時,會發生錯誤
print(spam(1))
print(spam(-1))
