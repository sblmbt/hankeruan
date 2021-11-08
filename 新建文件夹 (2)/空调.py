''''''

class aircondit:
    __brand=""
    __price=0.0

    def setbrand(self,brand):
        if brand=="":
            print("空调品牌不能为空！")
        else:
            self.__brand=brand
    def getbrand(self):
        return self.__brand

    def setprice(self,price):
        if price==0 or price<1000 or price>100000:
            print("空调价格不合适")
        else:
            self.__price=price
    def getprice(self):
        return self.__price

    def open(self):
        print("空调开机了.......")

    def show(self):
        print("空调的品牌是",self.__brand,"空调的价格是",self.__price,"元")

    def close(self,time):
        print("空调在",time,"分钟后自动关闭......")

p=aircondit()
p.setbrand("长虹")
p.setprice(10000)
p.open()
p.show()
p.close(2)






















