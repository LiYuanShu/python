import csv
import datetime
from geopy.distance import geodesic
from geopy.distance import geodesic
import xlwings as xw
def route(fileDir):
    temp_count_km=0
    time=0
    lists = []
    dictt={}
    routeDate=[]
    v_list=[0]
    time_list = [1]
    with open(fileDir, "r") as csvfile:
        reader = csv.reader(csvfile)
        for j, line in enumerate(reader):
            list4 = []
            if line[5] == '1' and int(line[11]) > 0:
                list4.append(line[3:5])
                list4.append(line[10])
                list4.append(line[11])
            if len(list4) != 0 and len(lists) == 0:
                lists.append(list4)
                routeDate.append(lists[-1][0:2])
            if len(lists) > 0 and len(list4) != 0:
                if lists[-1][0] != list4[0]:
                    a = lists.append(list4)
                    d1 = datetime.datetime.strptime(lists[-2][1], '%Y-%m-%d %H:%M:%S')
                    d2 = datetime.datetime.strptime(lists[-1][1], '%Y-%m-%d %H:%M:%S')
                    d = d2 - d1
                    h = int(format(d.seconds)) / 3600
                    # print(format(d.seconds))
                    list1 = lists[-2][0]
                    list2 = lists[-1][0]
                    list1 = list(map(float, list1))
                    list2 = list(map(float, list2))
                    list1[0], list1[1] = list1[1], list1[0]
                    list2[0], list2[1] = list2[1], list2[0]
                    tup1 = tuple(list1)
                    tup2 = tuple(list2)
                    # 两个经纬度之间的距离
                    km = geodesic(tup1, tup2).km
                    v = km / h
                    v_list.append(v)
                    a = (v_list[-1] - v_list[-2]) / time_list[-1]
                    temp_count_km=km+temp_count_km
                    time=time+h
                    routeDate.append(lists[-1][0])
                    distance_v_a=[temp_count_km,v,a]
                    dictt[str(lists[-1][0:2])]=str(distance_v_a)
                    print(a)
    with open('F:\\pycharm\\jiqi\\'+ fileDir[17:24]+'.txt','a+') as fw:
        fw.write("汽车总行程公里"+str(temp_count_km)+"km \n"+"汽车总行驶时间："+str(time)+"h \n"+"汽车总行程公里平均速度："+str(temp_count_km/time)+"km/h \n"+"运输线路每个经纬度、时间及对应的行车里程、平均行车速度、急加速急减速情况:"+str(dictt))
    fw.close()
    return routeDate
if __name__ == '__main__':
    ff = ['AA00001', 'AB00006', 'AD00003', 'AD00013', 'AD00053', 'AD00083', 'AD00419', 'AF00098', 'AF00131', 'AF00373']
    route_lists=[]
    for i in ff:
        fileDir = 'F:\\pycharm\\shuju\\' + i + '.csv'
        route_list=route(fileDir)
        dict = {}
        dict['name'] = fileDir
        dict['path'] = route_list
        route_lists.append(dict)
    with open('F:\\pycharm\\jiqi\\'+'route.txt','a+') as fw:
        fw.write(str(route_lists))
    fw.close()
