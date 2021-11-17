file=open(r'E:\\day15\\day14\\baidu_x_system.log')
ip_list=[]
for i in file.readlines():
    ip_list.append(i[0:13])
for j in ip_list:
    print(j,"->{}".format(ip_list.count(j)))
    while True:
        if j in ip_list:
             ip_list.remove(j)
        else:
            break