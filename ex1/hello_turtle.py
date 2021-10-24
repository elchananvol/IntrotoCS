#############################################################

# LOGIN : volberstan

# ID NUMBER : 206136749

# WRITER : elchanan volbersten

# I discussed the exercise with : no one

# Internet pages I looked for : no
##############################################################



import turtle


#this function will draw fatal
def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    print(draw_petal)

#this function will draw flower
def draw_flower():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

#this function will draw flower and move the turtle forword
def draw_flower_and_advance():
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

#this function will draw 3 flowers
def  draw_flower_bed():
    turtle.up()
    turtle.forward(150)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done