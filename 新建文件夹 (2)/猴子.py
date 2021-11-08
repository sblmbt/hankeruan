class monkey:
    __kind=""
    __gender=""
    __color=""
    __weight=0.0

    def setkind(self,kind):
        if kind=="":
            print("猴子种类不能为空")
        else:
            self.__kind=kind
    def getkind(self):
        return self.__kind

    def setgender(self,gender):
        if gender=="":
            print("性别不能为空")
        else:
            self.__gender=gender
    def getgender(self):
        return self.__gender

    def setcolor(self,color):
        if color=="":
            print("猴子颜色不能为空")
        else:
            self.__color=color
    def getcolor(self):
        return self.__color

    def setweight(self,weight):
        if weight<10 or weight>40:
            print("没有这种体重的猴子")
        else:
            self.__weight=weight
    def getweight(self):
        return self.__weight
    def makefire(self,texture):
        print("猴子可以用",texture,"的材料来造火")
    def study(self,program):
        print("猴子可以学习",program)
    def show(self):
        print("猴子种类",self.__kind,"猴子性别",self.__gender,"猴子身体的颜色",self.__color,"猴子的体重",self.__weight,"公斤")
p=monkey()
p.setkind("金丝猴")
p.setgender("公")
p.setcolor("黄色")
p.setweight(30)
p.makefire("石头")
p.study("直立行走，数数")
p.show()
