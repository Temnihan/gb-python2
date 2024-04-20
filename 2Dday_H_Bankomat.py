# началь сумма = 0
# Допустимые дейставия: снять пополнить выйти
# Сумма пололнение и снятия кратно 50
# комиссия от снятия 1.5%  но не менее 30  и не более 600 уе 
# После каждой 3 операции пополнении или снятия начисляются 3%
# Нельзя снимать больше чем на счете
# При превышении 5 млн  налог на богадтсво 10%  перед каждой операцией даже ошибочной
# любое действие выодит сумму денег
my_money = 0
rkatno = 50
print(" finish operation click 'space'\n or another keyb")
print("put, remove, only in multiples of 50 dollars")
operation = ''
commission = 30
ball_bonus = 0

while not operation ==' ':
    bonus = 0
    print(f' you have {my_money} enger number  ')
    money  = int(input('how mach money?'))
    if  money%50:
        print('enter only multiples of 50 ')
        continue
    operation = input('take = "t"\n put = "p" \n')
    if operation =='t':
        if money> my_money:
            print(" you have not money ")
            money = 0
            continue
# сдесь money это не прсто сумма а еще и комиссия
        if money*0.015<30:
            commission =30
        elif money*0.015>600:
            commission = 600
        else:
            commission =money*0.015
        print(f'comisston is {commission}')
        money = -money- commission
    elif operation =='p':
        money = +money
    else:
        operation = " "
    if ball_bonus ==3:
        bonus = money*0.03
        ball_bonus = 0
    ball_bonus +=1
    my_money+=money +bonus
oper = input('Сянть = С,')