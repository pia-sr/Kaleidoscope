import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import snowflake as sn
from IPython.display import HTML
import copy
import random

"""
Koch Snowflake Kaleidoscope

Final Project for Scientific Programming in Python in SS 2021

by Pia Schröter, Alina Krause and Paula Heigl
"""


# global variables
# list for the coordinates of each snowflake
snow_list = []
# list for all the plotted coordinates
lines = []

   
def main():
    # user input
    # set complexity of kaleidoscope / how many snowflakes
    global amount
    name = input("What's your name? \n")
    amount = int(input(name + ", how complex do you want the kaleidoscope to be? You can choose from a number from 1 to 5\n"))
    while amount < 1 or amount > 5:
        amount = int(input("Please indicate the complexity of your kaleidoscope with a number from 1 to 5!\n"))
    
    # set colour theme
    global colour
    colour = int(input("Okay, now what colour do you want for your kaleidoscope?\n1 red,\n2 yellow,\n3 green,\n4 grey,\n5 blue, \n6 purple or\n7 multicoloured?\n"))
    while colour < 1 or colour > 7:
        colour = int(input("Please indicate which colour you would like with a number from 1 to 6!\n"))
    
    # set rotation
    global rotate
    turn = input("Do you want the snowflake to rotate? Yes or No?\n")
    while not (turn == "yes" or turn == "Yes" or turn == "no" or turn =="No"):
        turn = input("Please answer with either 'yes' or 'no'!\n")
    if turn == "yes" or turn == "Yes":
        rotate = True
    else:
        rotate = False
        
    # set speed
    speed = int(input("How fast from 1 to 10 do you want your kaleidoscope to change, " + name + "? \n"))
    while speed < 1 or speed > 10:
        speed = int(input("Please indicate your preferred speed with a number from 1 to 10!\n"))
        
    print("I will generate your kaleidoscope now...")
   
    
    # settings for the plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    plt.axis('off')
    line, = ax.plot([],[]) # the plot is empty for the animation

    # fill snow_list with the coordinates relevant for the koch snowflakes
    snow_iterator(amount)
       
    # fill lines list with same amount of empty plots as triangles in snow_list
    for flakes in snow_list:
        l = ax.plot([],[])[0]
        lines.append(l)
    
    # generate the animation and safe as gif
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10, interval=1100-(speed*100), blit= True)
    anim.save("kaleidoscope.gif")
    #plt.show() # doesn't work in jupyter lab 
    
    print("You can find your personalized kaleidoscope in this folder! Have fun :)")
    
    
# function to create the coordinates for each snowflake
def snow_iterator(x):
    for i in range(x):
        if(i>=3):
            snow_list.append([[[0.36- (2**(i*((2.1/(i+2))*i)))*0.35,0.15-(2**(i*((2.1/(i+2))*i)))*0.21],[0.54,0.45+(2**(i*((2.1/(i+2))*i)))*0.42],[0.72+(2**(i*((2.1/(i+2))*i)))*0.36,0.15-(2**(i*((2.1/(i+2))*i)))*0.21]],1])
            snow_list.append([[[0.42-(2**(i*((2.1/(i+2))*i)))*0.23,0.25],[0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.35+(2**(i*((2.1/(i+2))*i)))*0.21],[0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.15-(2**(i*((2.1/(i+2))*i)))*0.21]],1])

        else:
            snow_list.append([[[0.36- (i**(2))*0.35,0.15-(i**(2))*0.21],[0.54,0.45+(i**(2))*0.42],[0.72+(i**(2))*0.36,0.15-(i**(2))*0.21]],1])
            snow_list.append([[[0.42-(i**(2))*0.23,0.25],[0.6+(i**(2))*0.12,0.35+(i**(2))*0.21],[0.6+(i**(2))*0.12,0.15-(i**(2))*0.21]],1])

        
# default for every line
def init():     
    for line in lines:
        line.set_data([],[])
    return lines


# change the coordinates of all points in snow_list by 12° around the center
def rotation():
    cx = 0.54 # coordinates of the center of the snowfalkes
    cy = 0.25
    radian = np.radians(12) # angle

    global snow_list
    new_snow_list = copy.deepcopy(snow_list)

    # iterate trough snow_list and rotate each coordinates by 12°
    for pair in range(len(new_snow_list)):
        for point in range(len(new_snow_list[pair][0])):
            new_snow_list[pair][0][point][0] = ((snow_list[pair][0][point][0]-cx) * np.cos(radian)) + ((snow_list[pair][0][point][1]-cy) * np.sin(radian)) + cx
            new_snow_list[pair][0][point][1] = -((snow_list[pair][0][point][0]-cx) * np.sin(radian)) + ((snow_list[pair][0][point][1]-cy) * np.cos(radian)) + cy

    snow_list = copy.deepcopy(new_snow_list)



# method to draw and animate each snowflake
def animate(i):  
    
    # change the points in snow_list in each frame to make the snowflake rotate
    if rotate == True:  
        rotation()
          
    # lists for x and y coordinates which are used for the plotting
    xList = []
    yList = []
    
    # iterate through each triangle coordinates
    for triangle, k in snow_list:
        # initially snowflake gets more and
        # after half of the frames it gets less branched
        if i < 7:
            k = i
        else:
            k = 10 - i
        
        # calculate the koch snowflakes
        data = np.array(sn.snow(triangle, k))
        x, y = np.split(data, 2, axis=1)        
        xList.append(x)
        yList.append(y)
        
        # sets the limit of the x- and y-axes for the given amount of snowflakes
        if(i == 0):
            x_sorted = np.sort(np.concatenate(xList).ravel())
            y_sorted = np.sort(np.concatenate(yList).ravel())
            plt.xlim(x_sorted[0]-((0.07*amount) * amount), x_sorted[-1]+ ((0.07*amount) * amount **2))
            plt.ylim(y_sorted[0]-(((2**-(6-amount)) * (4))*amount), y_sorted[-1] + 0.05)
    
    # set the colour for all lines
    for lnum,line in enumerate(lines):
        line.set_data(xList[lnum], yList[lnum])
        
        global colour
        
        if colour == 1:
            line.set_color(color = (1,random.uniform(0,0.3),random.uniform(0,0.7))) #rot
        elif colour == 2:
            line.set_color(color = (1,random.uniform(0.8,1),random.uniform(0.2,0.9))) #gelb
        elif colour == 3:
            line.set_color(color = (0,random.uniform(0.6,0.9),random.uniform(0.2,0.6))) #grün  
        elif colour == 4:
            val = random.uniform(0.1,0.9)
            line.set_color(color = (val,val,val)) #grau    
        elif colour == 5:
            line.set_color(color = (0,random.uniform(0.1, 0.3),random.uniform(0.5, 1))) #blau   
        elif colour == 6:
            line.set_color(color =(0.6,random.uniform(0,0.4), random.uniform(0,0.9))) #lila
        elif colour == 7:
            line.set_color(color = (random.uniform(0.2,0.9),random.uniform(0.2,0.9),random.uniform(0.2,0.9)))
        
    return lines
        
    

if __name__ == "__main__":
    main()
       