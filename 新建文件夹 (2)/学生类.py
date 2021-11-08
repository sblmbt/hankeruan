class student:
    __number=0
    __name=""
    __age=0
    __sex=""
    __high=0.00
    __weight=0.0
    __resuit=0.0
    __address=""
    __call=""

    def setnumber(self,number):
       if number<0:
           print("学号不合理")
       else:
           self.__number=number
    def getnumber(self):
        return self.__number
    def setname(self,name):
       if name=="":
           print("姓名不能为空")
       else:
           self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
       if age<5 or age>30:
           print("年龄不合理")
       else:
           self.__age=age
    def getage(self):
        return self.__age
    def setsex(self,sex):
       if sex=="":
           print("性别不能为空")
       else:
           self.__sex=sex
    def getsex(self):
        return self.__sex
    def sethigh(self,high):
       if high<1.40 or high>2.00:
           print("身高不合理")
       else:
           self.__high=high
    def gethigh(self):
        return self.__high
    def setweight(self,weight):
       if weight<35.0 or weight>90.0:
           print("体重不合理")
       else:
           self.__weight=weight
    def getweight(self):
        return self.__weight
    def setresult(self,result):
       if result<0 or result>120:
           print("成绩不合理")
       else:
           self.__result=result
    def getresult(self):
        return self.__result
    def setaddress(self,address):
       if address=="":
           print("地址不能为空")
       else:
           self.__address=address
    def getaddress(self):
        return self.__address
    def setcall(self,call):
       if call=="":
           print("电话号码不能为空")
       else:
           self.__call=call
    def getcall(self):
        return self.__call
    def study(self,time):
        print("学习了",time,"小时")
    def playgame(self,programe):
        print("玩",programe,"游戏")
    def write(self,line):
        print("编写了",line,"行代码")
    # 求总和
    def qiuhe(self,*shu):
        he=0
        for i in shu:
            he=he+i
        print("总和是",he)
        return he
    def show(self):
        print("学号是",self.__number,"姓名是",self.__name,"年龄是",self.__age,"岁，性别是",self.__sex,"身高是",self.__high,
              "米，体重是",self.__weight,"公斤，成绩是",self.__result,"分，家庭地址是",self.__address,"电话是",self.__call)
p=student()
p.setnumber(49)
p.setname("李四")
p.setage(20)
p.setsex("男")
p.sethigh(1.78)
p.setweight(54.8)
p.setresult(98)
p.setaddress("北京市昌平区")
p.setcall(14567359872)
p.study(3)
p.playgame("英雄联盟")
p.write(10)
p.qiuhe(67,86,32,18,53)
p.show()