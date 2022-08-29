import turtle
 
wn = turtle.Screen()
wn.bgcolor("blue")       #starting main coding with blue background
 
carl = turtle.Turtle()  # I named my turtle carl, Hi carl!
carl.speed(1000)
carl.color("black")              
carl.pensize(3)                 
carl.fillcolor("white")

carl.up()                   # this is my first circle for my snowman starting from bottom to top with attribute
carl.setposition(-20, -270)
carl.down()
carl.width(width=5)

carl.begin_fill()
for i in range (360):
    carl.forward(2)
    carl.left(1.15)
carl.end_fill()

carl.up()                  # the second circle in the middle
carl.setposition(45, -40)
carl.down()
carl.width(width=5)

carl.begin_fill()
for i in range (340):
    carl.forward(1.5)
    carl.left(1.15)
carl.end_fill()

carl.up()                  #the third circle on top
carl.setposition(37, 125)
carl.down()
carl.width(width=5)

carl.begin_fill()
for i in range (313):
    carl.forward(1)
    carl.left(1.15)
carl.end_fill()

# these two dot() code attribute are for the snowman eyes.
carl.up()
carl.setposition(10,150) #right eye
carl.down()
carl.color("black")
carl.dot(20)

carl.up()
carl.setposition(-35,150) #left eye
carl.down()
carl.color("black")
carl.dot(20)

# this code are for the buttons on the snowman
carl.up()
carl.setposition(-15,50)
carl.down()
carl.color("green")
carl.dot(20)

carl.up()
carl.setposition(-15,25)
carl.down()
carl.color("red")
carl.dot(20)

carl.up()
carl.setposition(-15,-0)
carl.down()
carl.color("green")
carl.dot(20)

carl.up()
carl.setposition(-15,-25)
carl.down()
carl.color("red")
carl.dot(20)

# this is the code for the nose for the snowman
carl.up()
carl.setposition(-12,125)
carl.down()
carl.color("orange")      
carl.dot(15)
carl.hideturtle()

#Arms for the snowman( well i tried my best to make the arms)
carl.up()
carl.goto(60,-15)
carl.down()
carl.color("black")
carl.width(width=5)
carl.right(80)
carl.forward(150)          
carl.left(90)               
carl.forward(10)

carl.up()
carl.goto(-89,-15)
carl.down()
carl.color("black")
carl.width(width=5)
carl.right(80)
carl.forward(-180)          
carl.left(90)               
carl.forward(10)




wn.exitonclick()                
