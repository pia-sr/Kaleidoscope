import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import snowflake as sn
from IPython.display import HTML
import copy
import math
from PIL import Image


#A list for the coordinates of each snowflake
snow_list = []
#A list for all the plotted coordinates
lines = []
rotate = False

    
def main():
    # user input
    global amount
    name = input("What's your name?")
    amount = int(input(name + ", how big do you want your kaleidosocope to be? You can choose from a number from 1 to 5\n"))
    while amount < 1 or amount > 5:
        amount = int(input("Please indicate the size of the kaleidoscope with a number from 1 to 5!"))
    colour = int(input("What colour do you want for your kaleidoscope?\n1 red,\n2 yellow,\n3 green,\n4 turquoise,\n5 blue or\n6 purple?\n"))
    while colour < 1 or colour > 6:
        colour = int(input("Please indicate which colour you would like with a number from 1 to 6! "))
    turn = input("Do you want the snowflake to rotate? Yes or No?\n")
    if  turn == "yes" or turn == "Yes":
        global rotate
        rotate = True
    speed = int(input("How fast from 1 to 10 do you want your kaleidoscope to change? "))
    while speed < 1 or speed > 10:
        speed = int(input("Please indicate your preferred speed with a number from 1 to 10! "))
   
    
    #Settings for the plot
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    plt.axis('off')

    #fills the snow-list with snowflakes
    snow_iterator(amount)
  
    
    #the plot is empty for the animation
    line, = ax.plot([],[])
    
    
    #the list will be filled with same amount of empty plots as needed in the end
    #c is used to change the values of the colours
    c = 0
    #A List of plots to have multiple lines
    #The colour gets lighter with each line 
    for flakes in snow_list:
        c += 1
        if colour == 1:
            l = ax.plot([],[], color = (1  ,1 - c*(1/(((amount * 2) +2))),1 - c*(1/(((amount * 2) +2)))))[0] # rot
        elif colour == 2:
            l = ax.plot([],[], color = (1,1,1 - c*(1/(((amount * 2) +2)))))[0] #gelb
        elif colour == 3: 
             l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))), 1,1 - c*(1/(((amount * 2) +2)))))[0] #grün
        elif colour == 4:
            l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))),1, 1))[0] #türkis
        elif colour == 5:
            l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))),1 - c*(1/(((amount * 2) +2))), 1))[0] #blau
        elif colour == 6:
            l = ax.plot([],[], color = (1,1 - c*(1/(((amount * 2) +2))), 1))[0] #lila
        lines.append(l)
    
    

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=10, interval=1100-(speed*100), blit= True)
    anim.save("kaleidoscope.gif", name)
    # for nomal python (doesn't work with jupyter lab)
    #plt.show()
    
    print("You can find your personalized kaleidoscope in this folder! Have fun :)")
    
    
# Function to create the coordinates for each snowflake
#Das kann vielleicht für die Rotation in die animate-function
def snow_iterator(x):
    for i in range(x):

        if(i>=3):
            snow_list.append([[[0.36- (2**(i*((2.1/(i+2))*i)))*0.35,0.15-(2**(i*((2.1/(i+2))*i)))*0.21],[0.54,0.45+(2**(i*((2.1/(i+2))*i)))*0.42],[0.72+(2**(i*((2.1/(i+2))*i)))*0.36,0.15-(2**(i*((2.1/(i+2))*i)))*0.21]],1])
            snow_list.append([[[0.42-(2**(i*((2.1/(i+2))*i)))*0.23,0.25],[0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.35+(2**(i*((2.1/(i+2))*i)))*0.21],[0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.15-(2**(i*((2.1/(i+2))*i)))*0.21]],1])

        else:
            snow_list.append([[[0.36- (i**(2))*0.35,0.15-(i**(2))*0.21],[0.54,0.45+(i**(2))*0.42],[0.72+(i**(2))*0.36,0.15-(i**(2))*0.21]],1])
            snow_list.append([[[0.42-(i**(2))*0.23,0.25],[0.6+(i**(2))*0.12,0.35+(i**(2))*0.21],[0.6+(i**(2))*0.12,0.15-(i**(2))*0.21]],1])

        
#Default for every line
def init():     
    for line in lines:
        line.set_data([],[])
    return lines



#Method to draw and animate each snowflake
def animate(i):  
    # change the points in snow_list to make the snowflake rotate
    if rotate == True:
        global snow_list
        # coordinates of the center
        x = 0.54
        y = 0.25
        new_snow_list = copy.deepcopy(snow_list)
        for pair in range(len(new_snow_list)):
            for point in range(len(new_snow_list[pair][0])):
                new_snow_list[pair][0][point][0] = ((snow_list[pair][0][point][0]-x) * math.cos(0.20943951)) + ((snow_list[pair][0][point][1]-y) * math.sin(0.20943951)) + x
                new_snow_list[pair][0][point][1] = -((snow_list[pair][0][point][0]-x) * math.sin(0.20943951)) + ((snow_list[pair][0][point][1]-y) * math.cos(0.20943951)) + y
        snow_list = copy.deepcopy(new_snow_list)
        
    xList = []
    yList = []
    for triangle, k in snow_list:
        if i < 7:
            k = i
        if i > 6:
            k = 10 - i
        
        data = np.array(sn.snow(triangle, k))
        x, y = np.split(data, 2, axis=1)        
        xList.append(x)
        yList.append(y)
        if(k == 0):
            x_sorted = np.sort(np.concatenate(xList).ravel())
            y_sorted = np.sort(np.concatenate(yList).ravel())
            plt.xlim(x_sorted[0]-((0.07*amount) * amount), x_sorted[-1]+ ((0.07*amount) * amount **2))
            plt.ylim(y_sorted[0]-(((2**-(6-amount)) * (4))*amount), y_sorted[-1] + 0.05)
    
    for lnum,line in enumerate(lines):
        line.set_data(xList[lnum], yList[lnum])
    
    
    return lines
        
    

if __name__ == "__main__":
    main()
       