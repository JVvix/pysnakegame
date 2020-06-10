from turtle import*

def main():
    speed("fastest")
    background()
    pu()
    home()
    pod()
    speed("normal")
    head()
    shell()
    feet()
    tail()

    done()

def background():

    size=0

    for i in range (350) :
        if i%2==0:
            colour = "blue"
    else:
        colour ="red"
    color(colour)
    forward(size)
    right(91)
    size+=4

main()
