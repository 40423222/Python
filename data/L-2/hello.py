# This program says hello and asks for my name

print('Hello world! / ' + str(20170723))
# 可以選擇要顯示int還是float
# 數字要加上str因為在python中,文字+整數會產生錯誤
# str(12) = '12'
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# 如果改成print('You will be ' + 'int(myAge) + 1' + ' in a year.')
# 會顯示You will be int(myAge) + 1 in a year.
# myAge就不會改變了
# 要加上int(),因為input()以''來顯示,例如: 輸入11,myAge = '11'
# 所以就需要使用int(),這樣就能+1,之後再用str(),轉回''字串模式
