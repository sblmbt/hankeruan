import time

from DBUtils import select,insert_into,update,delete
import random
class Bank:
    __bank_name = "中国工商银行"  #定义一个开户银行
    __account=None  #定义账户账号
    __name=None     #定义账户姓名
    __password=None #定义账户密码
    __country=None  #定义账户国籍
    __province=None #定义账户省份
    __street=None   #定义账户街道
    __doot=None     #定义账户门牌号
    __money=0       #定义账户初始金额
    __date=time.strftime("%Y-%m-%d") #定义账户开户时间为当前时间

    def show(self):
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
        print("*6、注销                   *")
        print("*7、欢迎下次光临             *")
        print("***************************")

    # 提供set/get方法用于间接赋值和取值
    def setAccount(self,account):
        self.__account=account

    def getAccount(self):
        return self.__account

    def setName(self,name):
        self.__name=name

    def getName(self):
        return self.__name

    def setPassword(self,password):
        self.__password=password

    def getPassword(self):
        return self.__password

    def setCountry(self,country):
        self.__country=country

    def getCountry(self):
        return self.__country

    def setProvince(self,province):
        self.__province=province

    def getProvince(self):
        return self.__province

    def setStreet(self,street):
        self.__street=street

    def getStreet(self):
        return self.__street

    def setDoot(self,doot):
        self.__doot=doot

    def getDoot(self):
        return self.__doot

    def setMoney(self,money):
        self.__money=money

    def getMoney(self):
        return self.__money

    #定义添加到银行 定义函数元素对应元素  不是名称对名称
    def bankadd(self):

        sql="select count(*) from user"
        param=[]
        date=select(sql,param,mode="one")
        if date[0]>=100:
            return 3

        sql1="select * from user where account=%s"
        param1=[self.getAccount()]
        date1=select(sql1,param1,mode="one")
        if date1 != None:
            return 2

        sql2="insert into user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2=[self.getAccount(), self.getName(), self.getPassword(), self.getCountry(), self.getProvince(), self.getStreet(),
     self.getDoot(),
     self.getMoney(), self.__date, self.__bank_name]
        insert_into(sql2,param2)
        return 1



    #定义用户入参
    def useradd(self):

        self.setAccount(random.randint(10000000,99999999))
        self.setName(input("请输入您的名称"))
        self.setPassword(input("请输入您的密码"))
        print("请输入你的详细信息")
        self.setCountry(input("\t\t请输入您的国籍"))     #\t ==tab
        self.setProvince(input("\t\t请输入您的省份"))
        self.setStreet(input("\t\t请输入您的街道"))
        self.setDoot(input("\t\t请输入您的门牌号"))
        num=self.bankadd()
        if num ==3:
            print("本银行已满请到其他银行开户")
        elif num== 2:
            print("用户已存在")
        elif num==1:
            print("恭喜你开户成功")
    #存钱过程
    def cunqianguocheng(self,account,money):

        sql="select * from user where account=%s"
        sql2="update user set money=%s where account=%s"
        param=[account]
        date=select(sql,param,mode="one")
        if account ==date[0]:
            money1=date[7]+money
            param2 = [money1,param]
            update(sql2,param2)
            return True
        else:
            return False
    #存钱结果
    def cunqian(self):
        account = int(input("请输入账号："))
        money = int(input("请输入存入余额："))
        zh=self.cunqianguocheng(account,money)
        if zh==True:
            print("存入成功！")
        else:
            print("用户不存在！")
    #取钱结果account,name,password,country,province,steert,door,0,2021-11-2,bank_name
    def quqian(self):

        account=int(input("请输入账号："))
        password =int(input("请输入密码："))
        jine = int(input("请输入取钱金额："))
        jieguo=self.quqianguocheng(account,password,jine)
        if jieguo==0:
            print("取款成功！")
        elif jieguo==1:
            print("账号不存在！")
        elif jieguo==2:
            print("密码不对！")
        elif jieguo==3:
            print("钱不够！")
    # 取钱过程
    def quqianguocheng(self,account,password,jine):

        sql="select * from user where account=%s"
        param=[account]
        date=select(sql,param,mode="one")
        if account ==date[0]:
            if password==date[2]:
                if date[7]>=jine:
                    sql2="update user set money=%s where account=%s"
                    money1 = date[7] - jine
                    param2=[money1,param]
                    update(sql2,param2)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    #转账结果
    def zhuanzhang(self):

        ZCaccount=int(input("请输入转出账户："))
        ZRaccount=int(input("请输入转入账户："))
        password =int(input("请输入转出账号的密码："))
        ZCjine = int(input("请输入转出的金额："))
        zhuanzhang=self.zhuanzhanguocheng(ZCaccount,ZRaccount,password,ZCjine)
        if zhuanzhang==0:
            print("转账成功！")
        elif zhuanzhang==1:
            print("转出账号不对！")
        elif zhuanzhang==2:
            print("密码不对！")
        elif zhuanzhang==3:
            print("钱不够！")
        elif zhuanzhang==4:
            print("转入账号不对！")
    #转账过程
    def zhuanzhanguocheng(self,ZCaccount,ZRaccount,password,ZCjine):

        sql = "select * from user where account=%s"
        param = [ZCaccount]
        param2=[ZRaccount]
        date = select(sql, param,mode="one")
        date2=select(sql,param2,mode="one")

        if ZCaccount==date[0] and ZRaccount==date2[0]:
            if password==date[2]:
                if ZCjine<=date[7]:
                    sql2="update user set money=%s where account=%s"
                    money1 = date[7] - ZCjine
                    param3=[money1,ZCaccount]
                    update(sql2, param3)
                    money2 = date2[7] + ZCjine
                    param4 = [money2, ZRaccount]
                    update(sql2, param4)
                    return 0
                else:
                    return 3
            else:
                return 2
        else:
            return 1
    #查询过程
    def chaxunguocheng(self,account,password):

        sql = "select * from user where account=%s"
        param=[account]
        date=select(sql,param,mode="one")

        if account==date[0]:
            if password==date[2]:
                print("====================")
                print("账号为：",date[0])
                print("用户名为：", date[1])
                print("国家为：", date[3])
                print("\t\t省份为：", date[4])
                print("\t\t街道为：", date[5])
                print("\t\t门牌号为：", date[6])
                print("金额为：", date[7])
                print("注册日期为：", date[8])
                print("开户行为：", date[9])
                print("====================")
            else:
                return 2
        else:
            return 1
    #输入查询内容
    def chaxun(self):

        account=int(input("请输入查询账号："))
        password=int(input("请输入查询密码："))
        jieguo=self.chaxunguocheng(account,password)
        if jieguo==1:
            print("该用户不存在")
        elif jieguo==2:
            print("你输入的密码不正确")

    #注销过程
    def zhuxiaoguocheng(self,account,password):

        sql="select * from user where account=%s"
        param=[account]
        date=select(sql,param,mode="one")
        if account==date[0]:
            if password==date[2]:
                sql2="delete from user where account=%s"
                delete(sql2,account)
                return 3
            else:
                return 2
        else:
            return 1

    #注销结果
    def zhuxiao(self):

        account=int(input("请输入注销账号："))
        password=int(input("请输入注销密码："))
        jieguo=self.zhuxiaoguocheng(account,password)
        if jieguo==1:
            print("账号不存在！")
        elif jieguo==2:
            print("密码错误！")
        elif jieguo==3:
            print("账号注销成功！")

    def start(self):
        self.show()
        while False==0:
            index=int(input("请输入您需要的业务"))
            if index ==1:
                print("开户")
                self.useradd()
            elif index ==2:
                print("存钱")
                self.cunqian()
            elif index ==3:
                print("取钱")
                self.quqian()
            elif index ==4:
                print("转账")
                self.zhuanzhang()
            elif index ==5:
                print("查询")
                self.chaxun()
            elif index ==6:
                print("注销")
                self.zhuxiao()
            elif index ==7:
                print("下次光临")
                break

c=Bank()
c.start()