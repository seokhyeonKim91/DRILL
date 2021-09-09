import turtle
turtle.shape('turtle')
x = 90
turtle.left(x)


for grid in range(5): 
 turtle.forward(500) 
 turtle.right(x)
 turtle.forward(100)
 turtle.right(x)
 x = x * -1

turtle.forward(500)
turtle.left(x)
turtle.forward(500)
turtle.left(x)

for grid in range(5): 
 turtle.forward(100) 
 turtle.left(x)
 turtle.forward(500)
 turtle.right(x)
 x = x * -1
