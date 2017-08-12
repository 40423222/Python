# 定義spam並設變數
def spam(divideBy):
    return 42 / divideBy

# 不會執行spam(1),因為spam(0)會發生錯誤,spam(1)就無法執行,
# 之後執行except結束
try:
    # spam(數字),數字 = divideBy,並啟動spam
    print(spam(2))
    print(spam(12))
    print(spam(0)) # 分母為零時,會發生錯誤
    print(spam(1))
except ZeroDivisionError: # 打上錯誤的名稱
    print('Error: Invalid argument.')
    print(spam(-1))
