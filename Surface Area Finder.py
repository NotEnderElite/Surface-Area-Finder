import os 
import math
#Functions

def cylinder_func():
    cond = True
    while cond:
        try:
            circle_radius = float(input("Please input the radius of the circles:"))
            length = float(input('Please enter the length of the shape:'))
            cond = False
        except Exception as e:
            os.system('cls')
            print("Please put in a valid answer.")
    circles_surface = round(2*((circle_radius**2) * math.pi), 2)
    square_surface = round(((circle_radius*2)*math.pi)*length, 2)
    print(f'The surface area of this cylinder is {round(square_surface + circles_surface, 2)}')

def cube_func():
    cond = True
    while cond:
        try:
            square_length = float(input("Please input the length of the Cube:"))
            cond = False
        except Exception as e:
            os.system('cls')
            print("Please put in a valid answer.")
        square_surfacearea = (square_length**2)*6
        print(f"The surface area of this cube is {round(square_surfacearea, 2)}.")


identified_shapes = {1:'cylinder', 2:'cube'}
identified_formulas = {1:cylinder_func, 2:cube_func}
inp_cond = False
while inp_cond == False:
    inp_cond = True
    print("These are the identified shapes that you can choose.")

    for key in identified_shapes.keys():
        print(f'{key} - {identified_shapes[key].capitalize()}')
    try:
        user_input = int(input("Please pick the number of the shape you would like to do:"))
    except:
        inp_cond = False
        os.system('cls')
        continue
    check = identified_shapes.get(user_input, -1)
    if check == -1:
        inp_cond = False
        os.system('cls')
identified_formulas[user_input]()

