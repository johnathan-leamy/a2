'''
this progam solve the physics problen of calculating the gravitational or electric force on an object
given the mass/charge of that object as well as the mass/charge or the other objects that are near by it.
'''


'''
class to hold the different atributes of each object
'''
class thing:
    def __init__(self,posx,posy,posz):
        #the positions for the object which are out in when the object is created
        self.posx = posx
        self.posy = posy
        self.posz = posz

    mass = 0
    name = ""
#global variable for the universal constint
G = 6.7e-11

'''
calculates the magnitude of a vector
'''
def mag(x,y,z):
    i = x**2 + y**2 + z**2
    return i ** 0.5

'''
calculates the unit vector
'''
def solve_rhat(x,y,z):
    #calculates the value for each compentent then returns each value in a list
    xf = x/(mag(x,y,z))
    yf = y/mag(x,y,z)
    zf = z/mag(x,y,z)
    print("rhat = ", [xf,yf,zf])
    return [xf,yf,zf]

'''
calculates the magnitude of the force vector
'''
def solve_Fgravmag(G,m1,m2,rx,ry,rz):
    print("G: ",G)
    print("m1: ", m1)
    print("m2: ",m2)
    print("rx: ",rx)
    print("ry: ",ry)
    print("rz: ",rz)
    print("mag: ",mag(rx,ry,rz))
    i =  float(G) * ((float(m1) * float(m2)) / (mag(rx,ry,rz) ** 2))
    print("Fgrav",i)
    return i

'''
does the final calculation to get the total forces
'''
def get_forces_on(name, things):
    #values of the thing being looked at
    pos = []
    m = 0
    
    #each component for the final net force
    Fx = 0
    Fy = 0
    Fz = 0

    #looks for the thing that the user wants to know the forces on
    for i in things:
        if i.name == name:
            pos = [i.posx,i.posy,i.posz]
            m = i.mass

    #looks through all other things to add the forces the they create
    for j in things:
        if not check_same_pos(j,pos):
            #assume that i in mass 2 and j is mass 1
            #finds the vector between the two things
            r = [float(pos[0]) - float(j.posx), float(pos[1]) - float(j.posy), float(pos[2]) - float(j.posz)]
            #fins the magnitue of the force
            print(j.name,":")
            Fmag =  solve_Fgravmag(G, m, j.mass,r[0], r[1], r[2])
            #print(solve_rhat(r[0],r[1],r[2]))
            #takes each compontent and finds the magnitude and direction and adds it to the net forces in each component
            rHat = solve_rhat(r[0],r[1],r[2])
            Fx += Fmag * rHat[0]
            Fy += Fmag * rHat[1]
            Fz += Fmag * rHat[2]
    return [Fx,Fy,Fz]
            
#checks if two things have the same position     
def check_same_pos(thing, pos):
    return thing.posx == pos[0] and thing.posy == pos[1] and thing.posz == pos[2]

def get_input():
    pos = []
    #make sure that the input for the position is valid and keeps repeating the command until it is
    while not len(pos) == 3:
        pos = []
        last = 1
        inp = input("Enter the position of an object (in the form \"<x,y,z>\") or next if you are done adding objects: ")
        if inp == "next":
            return False
        for i in range(len(inp)):
            #looks indetween the commas for values in the string the the user input
            if inp[i] == "," or inp[i] == ">":
                pos.append(inp[last:i])
                last = i + 1
            #checks to see if the input is valid
    
    return pos
    


if __name__ == "__main__":
    inp = ""
    #list that hold all the objects that the user adds
    things = []
    #changes the universal constaint depending on the type of force
    good_to_go = False
    while not(good_to_go):
        inp = input("type g for calculations using gravity and e for calculations using electric force: ")
        if inp == "g" or inp == "e":
            good_to_go = True
    if inp == "g":
        G = -6.7e-11
        str = "mass"
    elif inp == "e":
        G = 9e9
        str = "charge"
    
    print("add the objects you wold like to use in the simulation")
    #gets the values for the objects being added
    #loops until the user wants to move on
    while inp != "next":
        pos = []
        pos = get_input()
        if not pos:
            break
        
        things.append(thing(pos[0],pos[1],pos[2]))
        #adds the mass and name to the object that is being added
        mass_in = "why"
        #make sure that the mass is a number and not a word
        
        mass_in = input("Enter the "+str+" of the object: ")
        things[len(things)-1].mass = float(mass_in)
        things[len(things)-1].name = input("Enter the name of this object: ")


    #get the force of all othe objects acting on an object

    inp = input("what object do you want to know the forces on ")
    
    print(get_forces_on(inp, things))
    




            


