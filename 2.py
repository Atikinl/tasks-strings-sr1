s=input()
for i in s:
    if not(i.islower() or i.isdigit() or i==' '):
        print('Неверный символ:', i)
        break
else:
    print('OK')
