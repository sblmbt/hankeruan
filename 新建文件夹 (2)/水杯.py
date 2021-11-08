''''''
import time
class cup:
    __high = 0
    __volume= 0.0
    __color = ""
    __texture = ""
    def sethigh(self,high):
        if high>60 or high<10:
            print("没有这种大小的水杯")
        else:
            self.__high=high

    def gethigh(self):
        return self.__high

    def setvolume(self,volume):
        if volume>6 or volume<0.2:
            print("水杯容量不合理")
        else:
            self.__volume=volume

    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        if color==" ":
            print("水杯颜色不能为空！别瞎弄！")
        else:
            self.__color=color
    def getcolor(self):
        return self.__color

    def settexture(self,texture):
        if texture=="":
            print("水杯材质不能为空！别瞎弄！")
        else:
            self.__texture=texture
    def gettexture(self,texture):
        return self.__texture

    def deposit(self,content):
        print("杯子能存放",content,"升液体")
    def showcup(self):
        print("水杯的高度",self.__high,"厘米，水杯容量",self.__volume,"升，水杯颜色",self.__color,"水杯材质",self.__texture)
p=cup()
p.sethigh(20)
p.setvolume(0.5)
p.setcolor("粉色")
p.settexture("不锈钢")
p.deposit(0.5)


p.showcup()






