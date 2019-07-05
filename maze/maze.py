# Have an infinite loop here
import turtle
fred = turtle.Pen()
# Accept user input
user_command = input()

# the maze making/drawing code
fred.speed(0)
fred.forward(50)
fred.right(90)
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.forward(50)
fred.forward(50)
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.right(90)
fred.right(90)
fred.forward(50)
fred.forward(50)
fred.forward(50)
fred.up()
fred.right(90)
fred.forward(50)
fred.forward(50)
fred.right(90)
fred.forward(50)
fred.down()
fred.forward(50)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.up()
fred.right(90)
fred.right(90)
fred.forward(50)
fred.right(90)
fred.forward(50)
fred.forward(50)
fred.right(90)
fred.down()
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.up()
fred.forward(50)
fred.right(90)
fred.down()
fred.forward(50)
fred.left(180)
fred.forward(100)
fred.right(90)
fred.right(180)
fred.forward(50)
fred.up()
fred.forward(200)
fred.down()
fred.right(90)
fred.forward(150)
fred.left(180)
fred.forward(150)
fred.down()
fred.forward(150)
fred.left(90)
fred.forward(250)
fred.up()
fred.left(90)
fred.forward(50)
fred.left(90)
fred.down()
fred.forward(200)
fred.right(180)
fred.forward(50)
fred.left(90)
fred.forward(50)
fred.up()
fred.left(180)
fred.forward(75)
fred.left(90)
fred.forward(150)
fred.right(180)


# turtle move/ misc code

while user_command != "x":

	if user_command == "u":
		fred.up()

	if user_command == "i":
		fred.down()

	if user_command == "r":
		print("Color will change to RED")

	if user_command == "b":
		print("Color will change to BLUE")
		fred.color("blue")
	
	if user_command == "w":
		fred.forward(25)

	if user_command == "d":
		fred.right(90)

	if user_command == "s":
		fred.backward(25)

	if user_command == "a":
		fred.left(90)

	user_command = input()


print("Terminating draw program")

