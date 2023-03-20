# Define infinity as the large enough value
# This value will be used for vertices not connected to each other
def infinite():
	return 9999


# Determines coordinates of the intended vertices in the output
def coord(list):
    print(str(list[0]) + "," + str(list[1]))