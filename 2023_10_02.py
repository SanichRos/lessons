cod = int(input ('Введите шифр: '))
if cod < 3 or cod >20:
    print('Шифр не может быть меньше "3" или больше 20')
    exit()
my_list = []
x = 1
while cod > x:
    y = 1
    while cod-x-y >=0:
       if cod % (x+y) == 0 and x != y:
           str_x = str(x)
           str_y = str(y)
           str_shifr = str_x+'+'+str_y
           rev_str_sifr = str_y+'+'+str_x
           if str_shifr not in my_list:
               if rev_str_sifr not in my_list :
                    my_list.append(str_shifr)
       y+=1
    x+=1
print('расшифровка завершена')
print('получен код: ',(''.join(my_list)).replace('+', ""))
