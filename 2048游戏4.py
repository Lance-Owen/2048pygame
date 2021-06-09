"""
# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 12:53
# @Author  : 源来很巧
# @FileName: 2048游戏4.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44793283
"""

"""
实现每个相同操作的模块化
"""


import pygame
import sys
import random
import numpy as np
import pygame.freetype
pygame.init()                            #初始化
size=width,height=500,500
screen=pygame.display.set_mode(size)    #设置屏幕分辨率
screen.fill(pygame.Color("gray"))       #屏幕背景颜色
pygame.display.set_caption("2048游戏")   #标题名字
icon=pygame.image.load("2048.jpg")
pygame.display.set_icon(icon)           #标题图标
#数字和数字对应的颜色
num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
num_color = ['burlywood', 'oldlace', 'moccasin', 'orange',
             'coral', 'tomato', 'orangered', 'khaki',
             'gold','goldenrod', 'lightgreen', 'limegreen']
#初始矩阵
a = [[0, 2, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
#调出字体的颜色
BLACK=pygame.Color("black")
def draw(a):
    screen.fill(pygame.Color("gray"))  # 屏幕背景颜色
    for i in range(0, 4):
        for j in range(0, 4):
            num_index=num.index(a[i][j])
            r1rect=pygame.draw.rect(screen,pygame.Color(num_color[num_index]),
                                    (120 * j + 10, 120 * i + 10, 118, 118),0)
            f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', 10)
            if a[i][j] != 0:
                f1rect = f1.render_to(screen, (120 * j + 55, 120 * i + 55),
                                      str(a[i][j]), fgcolor=BLACK, size=30)
draw(a)
def compute(b):
    for i in range(0, 4):
        for j in range(0, 4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)
    #从左向右计算将每一种情况都检查一遍，进行计算。
    for i in range(0, 4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1] = b[i][2]
                b[i][2] = b[i][3]
                b[i][3] = 0
        else:
            if b[i][1] == b[i][2]:
                b[i][1] = 2 * b[i][1]
                b[i][2] = b[i][3]
                b[i][3] = 0
            else:
                if b[i][2] == b[i][3]:
                    b[i][2] = 2 * b[i][2]
                    b[i][3] = 0
def new_num(a):
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1)  # 产生一个元素为零的随机地址
    index_num = random.choice([2, 4])  # 随机产生一个数字2或4
    a[r_i[index_random]][r_j[index_random]] = index_num  # 替换对应位置的数字
    print(np.array(a))
def exist_in_list(list, find):
    for line in list:
        if find in line:
            return False
    return True
def cant_contiue(a):
    for i in range(len(a)):
        for j in range(len(a[0])-1):
            if a[i][j]==a[i][j+1]:
                return False
    for i in range(len(a)-1):
        for j in range(len(a[0])):
            if a[i][j]==a[i+1][j]:
                return False
    return True
def game_over():
    if exist_in_list(a, 0):
        if cant_contiue(a):
            # screen.fill(pygame.Color("moccasin"))
            f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', 10)
            f1.render_to(screen, (150, 220), "游戏结束！", fgcolor=BLACK, size=50)
            return True
        else:
            return False
#每个按键对应的函数操作
def up():
    global a                        #设为全局变量，实现不同按钮之间可以循环使用a
    if game_over():
        return 0
    c = a
    b=[]
    # 我们将所有的需要计算的矩阵，计算方向全都转化为在行方向，从左到右的计算方式进行，简化计算
    #不同的方向转化的方式也不相同，有难有易
    for i in range(0, 4):
        b.append([])
        for j in range(0, 4):
            b[i].append(a[j][i])
    compute(b)
    #计算完以后，我们需要还原之前转化的矩阵，还原到他应该展示的视角。并且还给a，保证后续的操作顺利
    a = []
    for i in range(0, 4):
        a.append([])
        for j in range(0, 4):
            a[i].append(b[j][i])
    if game_over():
        return 0
    if a==c:
        return 0
    new_num(a)
    if game_over():
        return 0
    draw(a)

def down():
    global a
    if game_over():
        return 0
    c = a
    b = [[], [], [], []]
    for i in range(0, 4):
        for j in range(3, -1, -1):
            b[i].append(a[j][i])
    for i in range(0, 4):
        for j in range(0, 4):
            if b[i][j] == 0:
                b[i].remove(0)
                b[i].append(0)
    compute(b)

    a = []
    i = 0
    for j in range(3, -1, -1):
        a.append([])
        for k in range(0, 4):
            a[i].append(b[k][j])
        i=i+1
    if game_over():
        return 0
    if a==c:
        return 0
    if game_over():
        return 0
    new_num(a)
    draw(a)
def left():
    global a
    c = a
    b = []
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[i][j])
    compute(b)
    a=b
    if game_over():
        return 0
    if a==c:
        return 0
    new_num(a)
    if game_over():
        return 0
    draw(a)
def right():
    global a
    if game_over():
        return 0
    c = a
    b = []
    for i in range(0, 4):
        b.append([])
        for j in range(3, -1, -1):
            b[i].append(a[i][j])
    compute(b)
    a=[]
    for i in range(0, 4):
        a.append([])
        for j in range(3, -1, -1):
            a[i].append(b[i][j])
    if game_over():
        return 0
    if a==c:
        return 0
    new_num(a)
    if game_over():
        return 0
    draw(a)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #键盘按键落下
            if event.key == pygame.K_UP:    #判断是那个键
                up()
            elif event.key == pygame.K_LEFT:
                left()
            elif event.key == pygame.K_RIGHT:
                right()
            elif event.key == pygame.K_DOWN:
                down()
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()                 #重绘屏幕




