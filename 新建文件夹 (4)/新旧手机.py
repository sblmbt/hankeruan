''''''
import time
class oldphone:
    __brand=""
    def setbrand(self,brand):
        if brand=="":
            print("老式手机品牌不能为空")
        else:
            self.__brand=brand
    def getbrand(self):
        return self.__brand

    def call(self,number):
        print("正在给",number,"打电话")
    def troudece(self):
        print("品牌为",self.__brand,"的手机很好用....")
class newphone(oldphone):
    __voice=False

    def call(self, number):
         super().call(number)
         self.__voice=True
         print("语音拨号中",end="")

         for i in range(5):
             print(".", end="")
             time.sleep(1)

         print()
    def troudece(self):
        super().troudece()

p=newphone()
p.setbrand("苹果")
p.call(13457845697)
p.troudece()