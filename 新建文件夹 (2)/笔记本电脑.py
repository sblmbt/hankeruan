''''''
class computer:
    __size=0.0
    __price=0.0
    __cpu=""
    __content=0
    __time=0

    def setsize(self,size):
        if size==0 or size<13 or size>19:
            print("电脑的屏幕大小不合理")
        else:
            self.__size=size
    def getsize(self):
        return self.__size

    def setprice(self,price):
        if price==0 or price<1000 or price>20000:
            print("电脑的价格不合理")
        else:
            self.__price=price
    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        if cpu=="":
            print("电脑cpu型号不能为空！别瞎弄！")
        else:
            self.__cpu=cpu
    def getcpu(self):
        return self.__cpu

    def setcontent(self,content):
        if content==0 or content>300:
            print("电脑内存大小不存在")
        else:
            self.__content=content
    def getcontent(self):
        return self.__content

    def settime(self,time):
        if time>7:
            print("电脑待机时间不能过长")
        else:
            self.__time=time
    def gettime(self):
        return self.__time

    def write(self):
        print("笔记本电脑可以打字")
    def playgame(self,gamename):
        print("笔记本电脑可以玩",gamename)
    def watch(self,videoname):
        print("笔记本电脑可以看",videoname)

    def show(self):
        print("电脑屏幕大小",self.__size,"英寸，电脑价格",self.__price,"元，电脑型号",self.__cpu,"电脑内存大小",
              self.__content,"G,电脑待机时间",self.__time,"小时")

p=computer()
p.setsize(15.6)
p.setprice(4200.0)
p.setcpu("i5酷睿")
p.setcontent(32)
p.settime(1)
p.write()
p.playgame("英雄联盟")
p.watch("抖音视频")
p.show()