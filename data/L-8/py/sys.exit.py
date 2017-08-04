import sys          # 啟動sys模組
while True:         # 無限迴圈
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()  # 強制跳出程式
    if response == 'break':
        print('bye')
        break       # 強制跳出程式
    print('You typed ' + response + '.')
