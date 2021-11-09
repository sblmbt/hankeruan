''''''
import time
class maker:
    __name=""
    __age=0
    def setname(self,name):
        if name=="":
            print("厨师姓名不能为空")
        else:
            self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        if age<16 or age>80:
            print("厨师年龄不合理")
        else:
            self.__age=age
    def getage(self):
        return self.__age
    def show(self):
        print("姓名是",self.__name,"年龄是",self.__age)

    def steam(self):
        print("用电饭锅蒸米饭")
class newmaker(maker):
    def stirfry(self):
        print("用炒菜锅倒油炒菜")
class newmaker1(newmaker):
     def steam(self):
         print("学会用电饭锅蒸饭")

     def stirfry(self):
         print("学会用炒锅蒸饭")
     def show(self):
         super().show()

p=newmaker1()
p.setname("张三")
p.setage(35)
p.steam()
p.stirfry()
p.show()
