# 定義spam並設變數
def spam(divideBy):
    return 42 / divideBy

# spam(數字),數字 = divideBy,並啟動spam
print(spam(2))
print(spam(12))
print(spam(0)) # 分母為零時,會發生錯誤
print(spam(1))
