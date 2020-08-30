while True:
 temp = int(input('\033[0;37mQual a temperatura:'))
 if temp <= 12:
    print('\033[0;36mEsta frio!')
 elif temp < 19:
    print('\033[0;30mEsta mediano')
 else:
    print('\033[0;31mEsta Calor!')
