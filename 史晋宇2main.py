'''
猜金币游戏
开始有5个金币，每猜错一次减一个，为0就退出或充钱，连续猜错3次也退出

'''
import random
jb=5
i=0
while jb>=1:
    random1= random.randint(1, 10)
    num=int(input("请输入您猜到的数字"))
    if num== random1:
        print("猜对了")
        print("现有金币数量",jb)
        jb=5
        break
    else:
        print ("猜错了,金币少一枚")
        jb = jb - 1
        print("现有金币数量",jb)
    i=i+1
    if i==3:
        print("猜错次数为3次游戏结束")
        break
    if jb==0:
        print("金币数量不足，请充值")
