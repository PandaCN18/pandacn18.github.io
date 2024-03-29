
# 引入画笔库
import turtle

# 创建画笔
t = turtle.Turtle()

# 画笔速度
t.speed(0)

# 画笔颜色
t.color("black")

# 画天空
t.penup()
t.goto(-300, -300)
t.pendown()
t.begin_fill()
t.fillcolor("skyblue")
for i in range(4):
    t.forward(600)
    t.left(90)
t.end_fill()

# 画太阳
t.penup()
t.goto(200, 200)
t.pendown()
t.begin_fill()
t.fillcolor("red")
t.circle(50)
t.end_fill()

# 画云的函数
def draw_cloud(x, y):
   
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.begin_fill()
    t.fillcolor("white")
    for i in range(4):
        t.circle(20)
        t.forward(20)
    t.end_fill()

# 画三朵云
draw_cloud(-200, 150)
draw_cloud(-50, 250)
draw_cloud(100, 100)

# 画飞机
t.begin_fill()
t.penup()
t.home()
t.pendown()
t.pensize(5)
t.goto(-300,150)
t.goto(100,50)
t.goto(0,0)
t.end_fill()

t.begin_fill()
t.goto(-30,-125)
t.goto(-50,-50)
t.end_fill()

t.begin_fill()
t.goto(-300,150)
t.goto(-125,-125)
t.goto(-50,-50)
t.goto(-30,-125)
t.goto(-85,-85)
t.end_fill()

# 移动画笔
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)

# 画“2”
t.color("black")
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# 移动画笔
t.penup()
t.goto(60, -200)
t.pendown()

# 画“0”
t.color("black")
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)

# 移动画笔
t.penup()
t.goto(120, -200)
t.pendown()

# 画“2”
t.color("black")
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# 移动画笔
t.penup()
t.goto(180, -200)
t.pendown()

# 画“1”
t.color("black")
t.right(90)
t.forward(100)

#移动画笔
t.penup()
t.goto(240, -250)
t.pendown()

# 画“8”
for i in range(2):
  t.forward(50)
  t.right(90)
  t.forward(50)
  t.right(90)

for i in range(2):
  t.forward(-50)
  t.right(-90)
  t.forward(-50)
  t.right(-90)

t.hideturtle()  # 隐藏画笔
turtle.done()   # 释放画笔

