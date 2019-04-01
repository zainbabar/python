# Have an infinite loop here
import turtle
fred = turtle.Pen()
# Accept user input
user_command = input()

# Check user input
while user_command != "x":

	if user_command == "u":
		fred.up()

	if user_command == "i":
		fred.down()

	if user_command == "r":
		print("Color will change to RED")

	if user_command == "b":
		print("Color will change to BLUE")
	
	if user_command == "w":
		fred.forward(100)

	if user_command == "d":
		fred.right(90)

	if user_command == "s":
		fred.backward(100)

	if user_command == "a":
		fred.left(90)

	user_command = input()


print("Terminating draw program")

