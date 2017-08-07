import random                 # 啟動random模組
def getAnswer(answerNumber):
    # 可用retune 或 print(),來顯示
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        print ("It is decidedly so")
    elif answerNumber == 3:
        print("Yes")
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        print('My reply is no')
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
for i in range(5):            # 執行5次
    r = random.randint(1, 9)  # r將會是1~9之中的一個數字
    fortune = getAnswer(r)    # 將r輸入到getAnswer程式,以fortune表示
    print(fortune)
