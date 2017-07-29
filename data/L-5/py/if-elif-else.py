print('Name?')
name = input()
print('Age?')
age = input()
if name == 'ABCD':
    print('Hi, ABCD')
elif int(age) < 12:
    print('You are not ABCD, kiddo.')
elif int(age) < 100:
    print('You are not ABCD....')
else:
    print('Who are you ?')
