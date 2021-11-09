''''''
class people:
    __age=0
    __sex=""
    __name=""
    def setage(self,age):
        if age<16 or age>50:
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
    def setname(self,name):
        if name=="":
            print("姓名不能为空")
        else:
            self.__name=name
    def getname(self):
        return self.__name
    def renzuo(self):
        print("这个人名字是",self.__name)
class worker(people):
    def renzuo(self):
        super().renzuo()
    def work(self):
        print("这位是工人，正在干活")

p=worker()
p.setname("李四")
p.renzuo()
p.work()
class student(people):
    __number=""

    def setnumber(self,number):
        if number < 0 :
            print("学号不能为负")
        else:
            self.__number = number

    def getage(self):
        return self.__number
    def renzuo(self):
        super().renzuo()
    def study(self):
        print("这位是学生，正在学习")
    def sing(self):
        print("这位是学生，正在唱歌")
q=student()
q.setname("张三")
q.renzuo()
q.study()
q.sing()