# Have an infinite loop here
import turtle
fred = turtle.Pen()
# Accept user input
user_command = input()

# Check user input
while user_command != "x":

	if user_command == "r":
		print("Color will change to RED")

	if user_command == "b":
		print("Color will change to BLUE")
	
	if user_command == "w":
		fred.up(100)

	if user_command == "d":
		fred.left(100)

	if user_command == "s":
		fred.down(100)

	if user_command == "a":
		fred.left(100)

	user_command = input()


print("Terminating draw program")

