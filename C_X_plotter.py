# -*- coding: utf-8 -*-
'''
@Time    : 2020/12/17 12:06
@Author  : Junfei Sun
@Email   : sjf2002@sohu.com
@File    : C_X_plotter.py
'''
import numpy as np
import matplotlib.pyplot as plt

def modify(degree):
    i=0
    xcumodify=[]
    for x in xcu:
       i+=1
       if i==len(xcu)/2+1:
           pass
       elif i<len(xcu)/2+1:
           x-=2*(len(xcu)/2-(i-1))*degree/len(xcu)
       elif i>len(xcu)/2+1:
           x+=2*((i-1)-len(xcu)/2)*degree/len(xcu)
       xcumodify.append(x)
    return xcumodify


file_name=input('Please input the file name')
f=open(file_name,'r')
data=f.readlines()
f.close()
coordinate_up={}
coordinate_down={}
lines = []
dicV={}
counter=0
for line in data:
    counter+=1
    line = line.strip()
    line = line.strip('\n')
    if counter==3:
        line=line.split(' ')
        newline = []
        for x in line:
            if x != '':
                try:
                    x=float(x)
                except ValueError:
                    pass
                newline.append(x)
        y_coordinate = newline[2:]

    if counter>=5:
        line=line.split(' ')
        line=[x for x in line if x!='']
        num=len(line[3:])
        lines.append(line[1])
        for i in range(1,num):
            if counter==5:
                dicV['%d'%i]=[]
            dicV['%d'%i].append(line[i+2])
            if counter-7>=0 and lines[counter-5]<lines[counter-6]:
                if dicV['%d' % i][counter - 6] >= dicV['%d' % i][counter - 5] and dicV['%d'%i][counter-6]>dicV['%d' % i][counter - 7]:
                    coordinate_up[y_coordinate[i-1]]=(1-float(lines[counter-6]))*30
            elif lines[counter-5]>lines[counter-6] and lines[counter-6]<lines[counter-7]:
                pass
            elif counter-8>0 and lines[counter-6]>lines[counter-7] and lines[counter-7]<lines[counter-8]:
                pass
            elif lines[counter - 5] > lines[counter - 6] > lines[counter - 7]:
                if dicV['%d' % i][counter - 6] >= dicV['%d' % i][counter - 5] and dicV['%d'%i][counter-6]>dicV['%d' % i][counter - 7]:
                    coordinate_down[y_coordinate[i-1]]=(1+float(lines[counter-6]))*30
ycu=[]
for key in list(coordinate_up.keys()):
    ycu.append(float(key))
ycufinal=np.array(ycu)
xcu=[]
for key in list(coordinate_up.values()):
    xcu.append(float(key))
xcufinal=np.array(xcu)


z1 = np.polyfit(xcufinal, ycufinal, 2)  # 用2次多项式拟合
p1 = np.poly1d(z1)
print(p1)
plot1=plt.plot(xcufinal, ycufinal, '*',label='points')
plt.xlabel('φ')
plt.ylabel('α')
plt.legend(loc=4)
plt.title('Upper surface X_Ctr graph')
X=np.linspace(float(list(coordinate_up.values())[0])-2,30,150)
Y=p1(X)
plt.plot(X,Y)
plt.show()

#the lower surface curve generally does not possess a analystic valye
'''ycd=[]
for key in list(coordinate_down.keys()):
    ycd.append(float(key))
ycdfinal=np.array(ycd)
xcd=[]
for key in list(coordinate_down.values()):
    xcd.append(float(key))
xcdfinal=np.array(xcd)

z2 = np.polyfit(xcdfinal, ycdfinal, 2)  # 用2次多项式拟合
p2 = np.poly1d(z2)
print(p2)
plot2=plt.plot(xcdfinal, ycdfinal, '*',label='points')
plt.xlabel('φ')
plt.ylabel('α')
plt.legend(loc=4)
plt.title('Lower surface X_Ctr graph')
x=np.linspace(30,float(list(coordinate_down.values())[-1])+2,150)
y=p2(X)
plt.plot(x,y)
plt.show()'''


modifychoice=input('Do you want to modify the graph for better performance?[t/f]')
if modifychoice=='t':
    degree=int(input('Please input how much φ you want to change'))
    xcumodify=np.array(modify(degree))
    zm = np.polyfit(xcumodify, ycufinal, 2)  # 用2次多项式拟合
    pm = np.poly1d(zm)
    print(pm)
    plot1 = plt.plot(xcufinal, ycufinal, '*', label='original')
    plotm = plt.plot(xcumodify,ycufinal, '.', label='modified')
    plt.xlabel('φ')
    plt.ylabel('α')
    plt.legend(loc=4)
    plt.title('Upper surface X_Ctr modified graph')
    X = np.linspace(float(list(coordinate_up.values())[0]) - 2, 33, 150)
    Y = p1(X)
    Xm = np.linspace(float(list(coordinate_up.values())[0]) - 2, 33, 150)
    Ym = pm(Xm)
    plt.plot(X, Y)
    plt.plot(Xm,Ym)
    plt.show()



