print('What is your name?')
name = input()
print('What is your password?')
password = input()
if name == name: # 達成if後方的條件,才會執行在這if內的程式
    print('Hello ' + name)
    if password == '1234':
        print('歡迎登入')
    else:
        print('密碼錯誤')
