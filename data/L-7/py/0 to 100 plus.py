total = 0               
for num in range(101):  #num將會跑101次,每次+1,從0開始
   total = total + num  #total會壘加,每次的num值,也就是0加到100
   # print(total)       #顯示total增加的過程(因為占Shell空間所以先隱藏)
print(total)            #只顯示增加後的過程
print(str(num))         #str()能將數字轉成文字
#  因為print()不是放在for 內, 所以不會顯示0~100

