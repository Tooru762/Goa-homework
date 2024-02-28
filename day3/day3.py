from turtle import * 
speed(30)
width(7) 
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90) 
#square
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60) 
right(90)
forward(120)
end_fill()
#door

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#window 
pendown()
left(30)
color("purple")

forward(120)
color("brown")
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

color("purple") 
begin_fill()
penup()
goto(-100,-10)
pendown() 

right(90)
forward(200)
right(90)
forward(250)
right(90)
forward(200)
right(90)
forward(250)
end_fill()
#door 
color("red") 
begin_fill()
right(90)
forward(90)
right(90)
forward(120) 
right(90) 
forward(90) 
right(90) 
forward(120)  
end_fill()
 
 
 #square 
penup() 

goto(-100,240) 
pendown() 
right(140)  
forward(160) 
left(100) 
forward(160) 
left(130) 
forward(210)
 
 #window
penup() 
goto(-270,100) 
pendown()  
color("blue") 
begin_fill()
left(90) 
forward(50) 
right(90) 
forward(50) 
right(90)  
forward(50) 
right(90) 
forward(50) 
end_fill() 

#grass
penup()
goto(-480,-10) 
pendown() 
color("green") 
begin_fill()
left(180)
forward(950)
right(90)
forward(380)
right(90)
forward(950)
right(90) 
forward(380) 
end_fill() 



#tree 

exitonclick()  


