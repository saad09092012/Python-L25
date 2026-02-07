# create class
class IOString():

    # constructer to set defualt value
    def __init__(self):
        self.strl = ""

    # function to get input from user
    def get_String(self):
        self.strl = input("Enter String :" )

    # function to print the string in upper case
    def print_String(self):
        print("Result is :", self.strl.upper())

# Object creation
strl = IOString()

# Call functions
strl.get_String()
strl.print_String()