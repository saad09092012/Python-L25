# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __def__(self):
        print("Destuctor called")

def Create_obj():
    print('Making object...')
    obj = Employee()
    print('function end...')
    del obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')