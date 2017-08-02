while True:              # 無限迴圈
  print('Who are you?')
  name = input()         # 對name輸入
  if name != '123':      # 符合條件執行
   continue              # 回到迴圈頂端
  print('Hello. What is the password? (It is a 4X6.)') 
  password = input()     # 對password輸入
  if password == '456':  # 符合條件值型
    break                # 跳出迴圈
print('Access granted.') # 在Shell顯示

