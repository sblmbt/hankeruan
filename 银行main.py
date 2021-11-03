import random
from DBUtils import update
from DBUtils import select
import math
print("***************************")
print("*    中国工商银行          *")
print("*     账户管理系统         *")
print("***************************")
print(" ")
print("*1、开户                   *")
print("*2、存钱                   *")
print("*3、取钱                   *")
print("*4、转账                   *")
print("*5、查询                   *")
print("*6、欢迎下次光临            *")
print("****************************")
#初始化银行
bank={}
#定义一个开户银行}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
#定义一个开户银行
bank_name="保熟银行"
#定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account,name,password,country,province,steert,door):
    sql="select count(*) from bank "
    param = []
    data = select(sql, param, mode="one")
    if data[0] >= 100:
        return 3
    sql1 = "select * from bank  where account=%s"
    param1 = [account]
    data1 = select(sql1, param1, mode="one")
    if  data1 !=None:
        return 2
    else:
        sql2 = "insert into bank  value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param12 = [name,account,password,country,province,steert,door,0,bank_name]
        update(sql2, param12)
        return 1

#定义用户入参
def useradd():
    account=random.randint(10000000,99999999)
    name=input("请输入您的名称")
    password=int(input("请输入您的密码"))
    print(math.log10(password) +1)
    while int(math.log10(password) +1) !=6:
        password=int(input("请输入您的密码"))
    print("请输入你的详细信息")
    country=input("\t\t请输入您的国籍")#\t ==tab
    province=input("\t\t请输入您的省份")
    steert=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)
    if num ==3:
        print("本银行已满请到其他银行开户")
    elif num== 2:
        print("用户已存在")
    elif num==1:
        print("恭喜你开户成功，一下是您的相信信息")
        sql1 = "select * from bank  where account=%s"
        param1 = [account]
        data1 = select(sql1, param1, mode="one")
        for i in data1:
            print(i)
# 存钱
def moneyadd(account,money):
      sql = "select * from bank  where account=%s"
      param = [account]
      data = select(sql, param, mode="one")
      if data != None:
          money1=data[7]+money
          sql1="update bank set money=%a where account=%a"
          param1 = [money1,account]
          update(sql1,param1)
          return True
      else:
          return False
def cunqian():
    account=int(input("请输入账户"))
    money=int(input("请输入存钱金额"))
    shu=moneyadd(account,money)
    print(shu)
    if shu==False:
        print("该用户不存在")
    else:
        print("打印存钱信息")
        sql1 = "select * from bank  where account=%s"
        param1 = [account]
        data1 = select(sql1, param1, mode="one")
        for i in data1:
            print(i)


# 取钱
def quadd(account,password,money):
    sql = "select * from bank  where account=%s"
    param = [account]
    data = select(sql, param, mode="one")
    if data != None:
       sql1 = "select * from bank  where account=%s and password=%s"
       param1 = [account,password]
       data1 = select(sql1, param1, mode="one")
       if data1!= None:
          if data[7]>=money:
             money1=data[7]-money
             sql2="update bank set money=%s where account=%s"
             param12=[money1,account]
             update(sql2,param12)
             return 0
          else:
             return 3
       else:
             return 2
    else:
         return 1
def quqian():
    account = int(input("请输入账户"))
    for i,j in bank.items():
        if account ==bank[i]["account"]:
            name=i
    money = int(input("请输入取钱金额"))
    password=int(input("请输入取钱密码"))
    lv=quadd(account,password,money)
    if lv==1:
        print("该账户不存在")
    elif lv==2:
        print("密码不对")
    elif lv==3:
        print("钱不够")
    elif lv==0:
        print("恭喜你取钱成功，以下是你的详细信息")
        sql1 = "select * from bank  where account=%s and password=%s"
        param1 = [account,password]
        data1 = select(sql1, param1, mode="one")
        for i in data1:
            print(i)



# 转账
def zuanadd(caccount,raccount,password,money):
     sql = "select * from bank  where account=%s"
     param =[caccount]
     data = select(sql, param, mode="one")
     param1 =[raccount]
     data1 = select(sql, param1, mode="one")
     if data !=None and data1!=None:
         sql1 = "select * from bank  where account=%s and password=%s"
         param2 = [caccount,password]
         data2 = select(sql1, param2, mode="one")
         if data2!= None:
            if data[7]>= money:
               money1=data[7]-money
               money2=data1[7]+money
               sql2="update bank set money=%s where account=%s"
               param12=[money1,caccount]
               param13=[money2,raccount]
               update(sql2,param12)
               update(sql2,param13)
               return 0
            else:
                return 3
         else:
              return 2
     else:
             return 1


def zuzang():
    caccount = int(input("请输入转出账户"))
    raccount = int(input("请输入转入账户"))
    password = int(input("请输入转出账号的密码"))
    money = int(input("请输入转出的金额"))
    for i in bank:
        if caccount == bank[i]["account"]:
            name=i
    te=zuanadd(caccount,raccount,password,money)
    if te==1:
        print("账号不对")
    elif te==2:
        print("密码不对")
    elif te==3:
        print("钱不够")
    elif te==0:
        print("转账成功，以下是详细信息")
        sql1 = "select * from bank  where account=%s and password=%s"
        param1 = [caccount,password]
        data1 = select(sql1, param1, mode="one")
        for i in data1:
            print(i)




# 查询
def chaxunadd(account,password):
   sql = "select * from bank  where account=%s"
   param = [account]
   data = select(sql, param, mode="one")
   if data != None:
      sql1 = "select * from bank  where account=%s and password=%s"
      param1 = [account,password]
      data1 = select(sql1, param1, mode="one")
      if data1!= None:
         return 0
      else:
          return 2
   else:
       return 1


def chaxun():
    account = int(input("请输入查询账户"))
    password = int(input("请输入查询账户的密码"))
    de=chaxunadd(account,password)
    if de==2:
        print("密码不对")
    elif de==1:
        print("账号不存在")
    elif de==0:
        print("查询成功，以下是查询信息")
        sql1 = "select * from bank  where account=%s and password=%s"
        param1 = [account,password]
        data1 = select(sql1, param1, mode="one")
        for i in data1:
            print(i)


while False==0:
    index=int(input("请输入您需要的业务"))
    if index ==1:
        print("开户")
        useradd()
        print(bank)
    elif index ==2:
        print("存钱")
        cunqian()
    elif index ==3:
        print("取钱")
        quqian()
    elif index ==4:
        print("转账")
        zuzang()
    elif index ==5:
        print("查询")
        chaxun()
    elif index ==6:
        print("下次光临")
        break
