import easygui as g
import sys
import random

def random_dice(): #模拟3个骰子的随机数
    import random
    dice_1 = random.randint (1,6)
    dice_2 = random.randint (1,6)
    dice_3 = random.randint (1,6)
    dice = str(dice_1) + str(dice_2) + str(dice_3)
    return dice

def add_dice(x):#将结果相加
    dice_plus = int(x[0]) + int(x[1]) + int(x[2])
    return dice_plus

def big_small(x):#用相加的结果判断大小
    x = int(x)
    if (x >= 4) and (x <= 10):
        return 'small'
    elif (x >= 11 and x <= 17):
        return 'big'
    else:
        return 'none'


#开始游戏
#设置用户名称，和起始金额
name_list = ['Jack','James','Tom','Bigwiner','Lucker','Neverlose','Cowboy','Superman']
playername = random.choice (name_list)
msg = 'Welcome to Dice Game'
title = 'Dice Game'
fields = ['Player name','Player Money']
values = [playername]
player_info = g.multenterbox(msg,title,fields,values)
if player_info == None:
    print('exit')
    sys.exit()

while True:
    dice_num = random_dice()
    dice_plus = add_dice(dice_num)
    dice_result = big_small(dice_plus)
    
    #选择大小，点数，(单选)
    msg = 'Hi: ' + str(player_info[0]) + '\n' + 'Choose Big or Small' + '\n' +'One wins One' + '\n' + 'Now you have money: ' + str(player_info[1])
    title = 'Money: ' + str(player_info[1])
    images = ['Big.png','Small.png']
    choices = ['Cancle']
    choose = g.buttonbox(msg,title,choices,images)
        
    if choose == 'Cancle' or None:
        sys.exit()
    else:
        choose == 'Big.png' or 'Small.png'
        msg = 'Pick the amount of the bet'
        title = 'Now you have $' + str(player_info[1])  #要计算每次的输赢
        images = ['20.png','50.png']
        butten = ['Cancle']
        amount = g.buttonbox(msg,title,butten,images)
        amount = str(amount[0]) + str(amount[1])
        if amount == 'Cancle' or None:
            sys.exit()


        elif ((choose == 'Big.png') and (dice_result == 'big')) or ((choose == 'Small.png') and (dice_result == 'small')):
            amount = int(amount) * 2
            msg = 'Your choose is' + choose + '\n' + dice_result + '\n' + 'You are win' + '\n' + 'Now you win $'+ str(amount)
            g.msgbox(msg)
            player_info[1] = int(amount) + int(player_info[1])
        else:
            amount = int(player_info[1]) - int(amount)
            msg = 'Your choose is' + choose + '\n' + dice_result + '\n' + 'You are lose' + '\n' + 'Now you have $'+ str(amount)
            g.msgbox(msg)          
            player_info[1] = amount 
            
            

       
        









