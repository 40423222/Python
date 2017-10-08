###
### 製作HTML表格生產程式

print("輸入表格線寬度 建議輸入5")
bor = input()

while True:
    print("輸入表格放置位置 1=left(左) 2=center(中) 3=right(右):")
    ali = input()
    if ali == '1':
        ali = 'left'
        break
    elif ali == '2':
        ali = 'center'
        break
    elif ali == '3':
        ali = 'right'
        break
    else:
        print('請輸入1~3')

TableFrame = "<table border='" + bor + "' width='100%' align='" +\
             ali + "'>"

print("接下來要對Table內部設計")


while True:
    print("輸入文字放置位置 1=left(左) 2=center(中) 3=right(右):")
    FontAlign = input()
    if FontAlign == '1':
        FontAlign = 'left'
    elif FontAlign == '2':
        FontAlign = 'center'
    elif FontAlign == '3':
        FontAlign = 'right'
    else:
        print("請輸入1~3")
        continue

    while True:
        print("輸入文字背景顏色 1=淺灰色 2=橘色 3=淺藍色 4=白色:")
        color = input()
        if color == '1':
            color = '#DDDDDD'
            break
        elif color == '2':
            color = '#FFD78C'
            break
        elif color == '3':
            color = '#B0E0E6'
            break
        elif color == '4':
            color = '#FFFFFF'
            break
        else:
            print('請輸入1~4')
            continue

    print("輸入內容:")
    content = input()

    while True:
        print("輸入下一步驟 1=連接 2=下一行 3=結束:")
        step = input()
        if step == '1':
            continue
        elif step == '2':
            print("<tr>")
        elif step == '3':
            break
        else:
            print("請輸入1~3")
    if step == '3':
        break
        

print(TableFrame)
print("<tr>")
print("<td style='text-align:" + FontAlign, "bgcolor='" + color + "'>" +\
      content + "</td>")
print("</table>")


