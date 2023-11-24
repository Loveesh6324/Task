import turtle as t
t.bgcolor("orangered")
t.screensize(1600,1000)

corr = [(780,-209),(750,-208),(700,-207),(650,-206),
        (580,-205),(560,-203),(540,-200),(520,-198),
        (520,-193),(526,-190),(530,-180),(536,-172),
        (538,-160),(543,-123),(540,-112),(533,-100),
        (525,-86),(525,-80),(530,-60),(532,-40),
        (531,-24),(534,-21),(540,-23),(550,-26),
        (553,-30),(556,-40),(540,-90),(540,-108),
        (543,-120),(550,-126),(567,-136),(562,-120),
        (562,-115),(567,-100),(578,-80),(580,-76),
        (584,-60),(586,-40),(582,-20),(580,-14),
        (570,-9),(560,-5),(550,-6),(540,-8),
        (530,-11),(518,0),(512,8),(502,8),(500,10),
        (482,20),(470,36),(460,49),(468,63),(465,66),
        (470,80),(468,100),(466,110),(460,120),
        (458,123),(455,122),(452,130),(456,136),
        (460,145),(463,133),(459,128),(472,128),
        (468,140),(463,157),(470,157),(478,152),
        (475,166),(471,165),(460,162),(457,165),
        (443,165),(437,160),(427,153),(423,149),
        (424,138),(419,133),(419,130),(422,128),
        (423,127),(426,124),(423,120),(423,118),
        (420,116),(420,114),(428,116),(430,118),
        (432,118),(432,116),(428,114),(414,92),
        (405,84),(390,77),(386,79),(377,79),
        (375,76),(364,76),(357,88),(352,86),
        (348,92),(340,93),(330,96),(326,96),
        (320,92),(312,97),(307,92),(304,95),
        (306,100),(308,102),(307,104),(307,108),
        (304,107),(304,120),(303,124),(308,132),
        (300,129),(298,128),(288,120),(282,104),
        (283,100),(284,97),(288,92),(285,89),
        (278,87),(283,77),(281,72),(288,67),
        (287,59),(284,57),(284,54),(287,50),
        (286,48),(290,43),(288,40),(300,26),
        (298,17),(305,14),(312,15),(316,17),
        (320,20),(322,40),(324,47),(326,49),
        (333,40),(342,18),(343,3),(345,-6),
        (342,-18),(342,-22),(346,-36),(350,-38),
        (348,-43),(340,-41),(336,-37),(320,-33),
        (312,-40),(307,-47),(303,-100),(308,-115),
        (314,-118),(320,-120),(328,-122),(328,-110),
        (324,-103),(318,-100),(319,-61),(322,-57),
        (340,-60),(366,-78),(366,-100),(368,-106),
        (366,-120),(363,-140),(361,-157),(358,-163),
        (350,-166),(340,-178),(320,-164),(300,-151),
        (280,-140),(260,-130),(240,-122),(220,-112),
        (200,-102),(180,-100),(150,-98),(125,-96),
        (100,-94),(75,-92),(50,-90),(25,-88),
        (0,-86),(-25,-83),(-50,-81),(-75,-79),
        (-100,-77),(-125,-75),(-150,-72),(-175,-70),
        (-800,-68),
        (-800,-500),(800,-500),(800,-210)]

part1 = [(418,70),(412,73),(404,67),(393,64),
         (382,66),(382,60),(390,58),(392,50),
         (400,46),(402,48),(408,51),(417,58),(418,60)]

part2 = [(380,-186),(400,-190),(420,-193),(440,-195),
         (460,-197),(503,-199),(508,-186),(520,-174),
         (520,-162),(528,-158),(531,-127),(520,-113),
         (500,-106),(495,-102),(500,-117),(500,-123),
         (480,-132),(452,-153),(440,-153),(440,-163),
         (430,-177),(424,-180),(420,-176),(426,-160),
         (437,-144),(440,-145),(467,-122),(467,-120),
         (460,-107),(453,-100),(450,-85),(450,-72),
         (440,-74),(408,-72),(400,-80),(397,-80),
         (390,-77),(386,-85),(380,-108),(377,-123),
         (375,-140),(370,-160),(374,-166),(362,-180)]


name = [[(-560,320),(-560,300),(-590,300),(-590,220),(-560,220),
         (-560,200),(-610,200),(-610,320)],
        [(-530,320),(-530,270),(-510,270),(-510,320),(-490,320),
         (-490,200),(-510,200),(-510,250),(-530,250),(-530,200),
         (-550,200),(-550,320)],
        [(-460,320),(-460,270),(-440,270),(-440,320),(-420,320),
         (-420,200),(-440,200),(-440,250),(-460,250),(-460,200),
         (-480,200),(-480,320)],
        [(-350,320),(-350,200),(-370,200),(-370,250),(-390,250),
         (-390,200),(-410,200),(-410,320)],
        [(-280,320),(-280,300),(-300,300),(-300,200),(-320,200),
         (-320,300),(-340,300),(-340,320)],
        [(-210,320),(-210,250),(-230,250),(-210,200),(-230,200),
         (-250,250),(-250,200),(-270,200),(-270,320)],
        [(-140,320),(-140,200),(-160,200),(-160,250),(-180,250),
         (-180,200),(-200,200),(-200,320)],
        [(-70,320),(-70,250),(-110,250),(-110,200),
         (-130,200),(-130,320)],
        [(0,320),(0,200),(-20,200),(-20,250),(-40,250),
         (-40,200),(-60,200),(-60,320)],
        [(10,320),(70,320),(70,300),(50,300),(50,200),(30,200),
         (30,300),(10,300),(10,320)],
        [(80,320),(140,320),(140,300),(120,300),(120,220),(140,220),
         (140,200),(80,200),(80,220),(100,220),(100,300),(80,300),(80,320)]]

#points = [(-390,300),(-250,300),(-180,320),(-110,320),(-40,320)]
points = [[(-390,300),(-370,300),(-370,270),(-390,270),(-390,300)],
          [(-250,300),(-230,300),(-230,270),(-250,270),(-250,300)],
          [(-180,300),(-160,300),(-160,270),(-180,270),(-180,300)],
          [(-110,300),(-90,300),(-90,270),(-110,270),(-110,300)],
          [(-40,300),(-20,300),(-20,270),(-40,270),(-40,300)]]

def sun():
    t.penup()
    t.speed(5)
    t.goto(420,-220)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    t.circle(240)
    t.end_fill()

def draw(c):
    t.penup()
    t.speed(7)
    t.goto(800,-210)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for i in range(len(c)):
        x, y = c[i]
        t.goto(x, y)
    t.end_fill()

def part(p,g):
    t.penup()
    t.speed(6)
    t.goto(g)
    t.pendown()
    t.color("gold")
    t.begin_fill()
    for i in range(len(p)):
        x, y = p[i]
        t.goto(x, y)
    t.end_fill()

def names(n,p):
    #C
    t.penup()
    t.goto(-610,320)
    t.speed(5)
    t.pendown()
    t.color("#fdfae5")
    t.begin_fill()

    for i in range(len(n[0])):
        x, y = n[0][i]
        t.goto(x, y)
    t.end_fill()
    #H
    t.penup()
    t.goto(-550, 320)
    t.speed(5)
    t.pendown()
    t.color("#faf3c0")
    t.begin_fill()

    for i in range(len(n[1])):
        x, y = n[1][i]
        t.goto(x, y)
    t.end_fill()
    #H
    t.penup()
    t.goto(-480, 320)
    t.speed(5)
    t.pendown()
    t.color("#f5ea92")
    t.begin_fill()

    for i in range(len(n[2])):
        x, y = n[2][i]
        t.goto(x, y)
    t.end_fill()
    #A
    t.penup()
    t.goto(-410, 320)
    t.speed(5)
    t.pendown()
    t.color("#f3e260")
    t.begin_fill()

    for i in range(len(n[3])):
        x, y = n[3][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-390,300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[0])):
        x, y = p[0][i]
        t.goto(x, y)
    t.end_fill()


    #T
    t.penup()
    t.goto(-340, 320)
    t.speed(5)
    t.pendown()
    t.color("#f5dd29")
    t.begin_fill()

    for i in range(len(n[4])):
        x, y = n[4][i]
        t.goto(x, y)
    t.end_fill()

    #R
    t.penup()
    t.goto(-270, 320)
    t.speed(5)
    t.pendown()
    t.color("#f2d600")
    t.begin_fill()

    for i in range(len(n[5])):
        x, y = n[5][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-250, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[1])):
        x, y = p[1][i]
        t.goto(x, y)
    t.end_fill()

    #A
    t.penup()
    t.goto(-200, 320)
    t.speed(5)
    t.pendown()
    t.color("gold")
    t.begin_fill()

    for i in range(len(n[6])):
        x, y = n[6][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-180, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[2])):
        x, y = p[2][i]
        t.goto(x, y)
    t.end_fill()

    #P
    t.penup()
    t.goto(-130, 320)
    t.speed(5)
    t.pendown()
    t.color("#e6c60d")
    t.begin_fill()

    for i in range(len(n[7])):
        x, y = n[7][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-110, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[3])):
        x, y = p[3][i]
        t.goto(x, y)
    t.end_fill()

    #A
    t.penup()
    t.goto(-60, 320)
    t.speed(5)
    t.pendown()
    t.color("#d9b51c")
    t.begin_fill()

    for i in range(len(n[8])):
        x, y = n[8][i]
        t.goto(x, y)
    t.end_fill()

    t.penup()
    t.goto(-40, 300)
    t.speed(5)
    t.pendown()
    t.color("orangered")
    t.begin_fill()

    for i in range(len(p[4])):
        x, y = p[4][i]
        t.goto(x, y)
    t.end_fill()

    #T
    t.penup()
    t.goto(10, 320)
    t.speed(5)
    t.pendown()
    t.color("#cca42b")
    t.begin_fill()

    for i in range(len(n[9])):
        x, y = n[9][i]
        t.goto(x, y)
    t.end_fill()

    #I
    t.penup()
    t.goto(80, 320)
    t.speed(5)
    t.pendown()
    t.color("#bd903c")
    t.begin_fill()

    for i in range(len(n[10])):
        x, y = n[10][i]
        t.goto(x, y)
    t.end_fill()


part1Goto = (417,60)
part2Goto = (362,-180)

t.speed(15)
wn = t.Screen()
wn.screensize()
wn.setup(width = 1.0, height = 1.0)
sun()
names(name,points)
draw(corr)
part(part1,part1Goto)

part(part2,part2Goto)

t.hideturtle()
t.Screen().exitonclick()







































# import turtle
# t1 = turtle.Turtle()
# t1.pensize(0)
# t1.speed(3)
# #t1.color("white", "white")
# t1.color("white", "blue")
# turtle.bgcolor("black")
# t1.begin_fill()
# t1.left(90)
# t1.forward(200)
# t1.left(120)
# t1.forward(200)
# t1.left(45)
# t1.forward(150)
# t1.left(30)
# t1.forward(100)
# t1.right(30)
# t1.forward(30)
# t1.left(40)
# t1.forward(80)
# t1.left(30)
# t1.forward(201)
# t1.left(126)
# t1.forward(110)
# t1.right(80)
# t1.forward(75)
# t1.left(168)
# t1.forward(130)
# t1.right(160)
# t1.forward(58)
# t1.left(70)
# t1.forward(40)
# t1.right(45)
# t1.forward(30)
# t1.left(150)
# t1.forward(20)
# t1.right(103)
# t1.forward(200)
# t1.left(180)
# t1.forward(30)
# t1.left(160)
# t1.forward(40)
# t1.left(40)
# t1.forward(40)
# t2 = turtle.Turtle()
# t2.pensize(0)
# t2.speed(0)
# t2.color("black", "black")
# t2.begin_fill()
# t2.right(90)
# t2.forward(158)
# t2.right(110)
# t2.forward(20)
# t2.left(160)
# t2.forward(30)
# t2.left(130)
# t2.forward(30)
# t3 = turtle.Turtle()
# t3.pensize(0)
# t3.speed(0)
# t3.color("black", "black")
# t3.begin_fill()
# t3.left(90)
# t3.forward(10)
# t3.left(20)
# t3.forward(40)
# t3.right(40)
# t3.forward(40)
# t4 = turtle.Turtle()
# t4.pensize(0)
# t4.speed(0)
# t4.color("white", "white")
# t4.penup()
# t4.setposition(30, 0)
# t4.left(10)
# t4.forward(80)
# t4.pendown()
# t4.begin_fill()
# t4.right(170)
# t4.forward(80)
# t4.right(110)
# t4.forward(15)
# t4.end_fill()
# t4.penup()
# t4.right(180)
# t4.forward(30)
# t4.pendown()
# t4.begin_fill()
# t4.left(90)
# t4.forward(50)
# t4.right(160)
# t4.forward(50)
# t4.right(110)
# t4.forward(20)
# t4.end_fill()
# t5 = turtle.Turtle()
# t5.pensize(0)
# t5.speed(0)
# t5.color("black", "black")
# t5.penup()
# t5.setposition(-30, 0)
# t5.pendown()
# t5.begin_fill()
# t5.left(170)
# t5.forward(80)
# t5.left(170)
# t5.forward(90)
# t5.left(110)
# t5.forward(15)
# t5.end_fill()
# t5.penup()
# t5.right(180)
# t5.forward(30)
# t5.pendown()
# t5.begin_fill()
# t5.right(90)
# t5.forward(50)
# t5.left(160)
# t5.forward(50)
# t5.left(110)
# t5.forward(20)
# t5.end_fill()
# t6 = turtle.Turtle()
# t6.pensize(0)
# t6.speed(0)
# t6.color("white", "white")
# t6.penup()
# t6.left(90)
# t6.forward(240)
# t6.pendown()
# t6.begin_fill()
# t6.left(0)
# t6.forward(40)
# t6.right(100)
# t6.forward(150)
# t6.right(40)
# t6.forward(30)
# t6.right(130)
# t6.forward(167)
# t6.right(90)
# t6.forward(50)
# t6.end_fill()
# t6.penup()
# t6.left(0)
# t6.forward(20)
# t6.pendown()
# t6.begin_fill()
# t6.left(0)
# t6.forward(20)
# t6.right(85)
# t6.forward(90)
# t6.right(45)
# t6.forward(60)
# t6.right(145)
# t6.forward(135)
# t6.end_fill()
# t6.penup()
# t6.right(85)
# t6.forward(50)
# t6.pendown()
# t6.begin_fill()
# t6.left(0)
# t6.forward(10)
# t6.right(70)
# t6.forward(60)
# t6.right(80)
# t6.forward(40)
# t6.right(125)
# t6.forward(80)
# t6.end_fill()
# t6.penup()
# t6.right(85)
# t6.forward(50)
# t6.pendown()
# t6.begin_fill()
# t6.left(0)
# t6.forward(10)
# t6.right(70)
# t6.forward(40)
# t6.right(80)
# t6.forward(25)
# t6.right(120)
# t6.forward(50)
# t6.end_fill()
# t6.penup()
# t6.right(90)
# t6.forward(40)
# t6.pendown()
# t6.begin_fill()
# t6.left(0)
# t6.forward(40)
# t6.right(150)
# t6.forward(45)
# t6.right(120)
# t6.forward(20)
# t6.end_fill()
# t7 = turtle.Turtle()
# t7.pensize(0)
# t7.speed(0)
# t7.color("white", "white")
# t7.penup()
# t7.setposition(-70, 530)
# t7.pendown()
# t7.begin_fill()
# t7.right(70)
# t7.forward(60)
# t7.right(60)
# t7.forward(50)
# t7.right(40)
# t7.forward(60)
# t7.right(170)
# t7.forward(60)
# t7.left(30)
# t7.forward(30)
# t7.left(45)
# t7.forward(60)
# t7.end_fill()
# t8 = turtle.Turtle()
# t8.pensize(0)
# t8.speed(0)
# t8.color("white", "white")
# t8.penup()
# t8.setposition(5, 500)
# t8.pendown()
# t8.begin_fill()
# t8.left(20)
# t8.forward(100)
# t8.right(90)
# t8.forward(600)
# t8.left(175)
# t8.forward(630)
# t8.left(75)
# t8.forward(60)
# t8.left(46)
# t8.forward(110)
# t8.end_fill()
# t9 = turtle.Turtle()
# t9.pensize(0)
# t9.speed(0)
# t9.color("white", "white")
# t9.penup()
# t9.setposition(-230, -40)
# t9.pendown()
# t9.begin_fill()
# t9.right(75)
# t9.forward(110)
# t9.right(40)
# t9.forward(120)
# t9.right(140)
# t9.forward(90)
# t9.right(30)
# t9.forward(80)
# t9.right(100)
# t9.forward(30)
# t9.left(118)
# t9.forward(70)
# t9.end_fill()
# t9.penup()
# t9.right(177)
# t9.forward(120)
# t9.pendown()
# t9.color("black", "black")
# t9.begin_fill()
# t9.right(35)
# t9.forward(60)
# t9.right(125)
# t9.forward(40)
# t9.right(45)
# t9.forward(60)
# t9.right(125)
# t9.forward(50)
# t9.end_fill()
# t3.end_fill()
# t2.end_fill()
# t1.end_fill()
# t1.hideturtle()
# t3.hideturtle()
# t2.hideturtle()
# t4.hideturtle()
# t5.hideturtle()
# t6.hideturtle()
# t7.hideturtle()
# t8.hideturtle()
# t9.hideturtle()
# turtle.done()