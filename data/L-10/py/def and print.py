print('eggs => Local Variables')

print('')

print('print() in spam')
def spam():
    eggs = 10
    print(eggs)
spam()

print('')

print('print() not in spam')
def spam():
    eggs = 10
spam()
print(eggs)

