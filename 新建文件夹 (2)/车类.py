class car:
    __model=""
    __tires=0
    __color=""
    __weight=0.0
    __size=0

    def setmodel(self,model):
        if model=="":
            print("车型号不能为空")
        else:
            self.__model=model
    def getmodel(self):
        return self.__model

    def settires(self,tires):
        if tires<0 or tires>5:
            print("车轮数不合理")
        else:
            self.__tires=tires
    def gettires(self):
        return self.__tires

    def setcolor(self,color):
        if color=="":
            print("车身颜色不能为空")
        else:
            self.__color=color
    def getcolor(self):
        return self.__color

    def setweight(self,weight):
        if weight<1.0 or weight>3.0:
            print("汽车重量不合适")
        else:
            self.__weight=weight
    def getweight(self):
        return self.__weight

    def setsize(self,size):
        if size<30 or size>100:
            print("油箱储存大小不合理")
        else:
            self.__size=size
    def getsize(self):
        return self.__size

    def run(self):
        print(self.__model,"型号的车在跑来跑去！")
    def showcar(self):
        print("车型号",self.__model,"车轮胎数",self.__tires,"个，车身颜色",self.__color,"车的重量",self.__weight,"吨，油箱储存大小",
              self.__size,"升")

p=car()
p.setmodel("法拉利")
p.settires(4)
p.setcolor("白色")
p.setweight(2.5)
p.setsize(80)
p.run()
p.showcar()
