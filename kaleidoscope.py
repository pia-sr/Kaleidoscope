import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import snowflake as sn
from IPython.display import HTML


#Amount of snowflakes
amount = 4
#A list for the coordinates of each snowflake
snow_list = []
#A list for all the plotted coordinates
lines = []


    
def main():
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
        #l = ax.plot([],[], color = (1  ,1 - c*(1/(((amount * 2) +2))),1 - c*(1/(((amount * 2) +2)))))[0] #rote Version
        #l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))), 1,1 - c*(1/(((amount * 2) +2)))))[0] #blaue Version
        #l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))),1 - c*(1/(((amount * 2) +2))), 1))[0] #grüne Version
        l = ax.plot([],[], color = (1 - c*(1/(((amount * 2) +2))),1, 1))[0] #türkise Version
        #l = ax.plot([],[], color = (1,1 - c*(1/(((amount * 2) +2))), 1))[0] #lila Version
        #l = ax.plot([],[], color = (1,1,1 - c*(1/(((amount * 2) +2)))))[0] #gelbe Version
        lines.append(l)
    

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=6, interval=600, blit= True)
    anim.save("kaleidoscope.gif")
    
    
# Function to create the coordinates for each snowflake
#Das kann vielleicht für die Rotation in die animate-function
def snow_iterator(x):
    for i in range(x):
        
        if(i>=3):
            snow_list.append(([(0.36- (2**(i*((2.1/(i+2))*i)))*0.35,0.15-(2**(i*((2.1/(i+2))*i)))*0.21),(0.54,0.45+(2**(i*((2.1/(i+2))*i)))*0.42),(0.72+(2**(i*((2.1/(i+2))*i)))*0.36,0.15-(2**(i*((2.1/(i+2))*i)))*0.21)],1))
            snow_list.append(([(0.42-(2**(i*((2.1/(i+2))*i)))*0.23,0.25),(0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.35+(2**(i*((2.1/(i+2))*i)))*0.21),(0.6+(2**(i*((2.1/(i+2))*i)))*0.12,0.15-(2**(i*((2.1/(i+2))*i)))*0.21)],1))
            
        else:
            snow_list.append(([(0.36- (i**(2))*0.35,0.15-(i**(2))*0.21),(0.54,0.45+(i**(2))*0.42),(0.72+(i**(2))*0.36,0.15-(i**(2))*0.21)],1))
            snow_list.append(([(0.42-(i**(2))*0.23,0.25),(0.6+(i**(2))*0.12,0.35+(i**(2))*0.21),(0.6+(i**(2))*0.12,0.15-(i**(2))*0.21)],1))
            
    
#Default for every line
def init():     
    for line in lines:
        line.set_data([],[])
    return lines



#Method to draw and animate each snowflake
def animate(i):
    xList = []
    yList = []
    for triangle, k in snow_list:
        k = i
        data = np.array(sn.snow(triangle, k))
        x, y = np.split(data, 2, axis=1)        
        xList.append(x)
        yList.append(y)
        if(k == 0):
            x_sorted = np.sort(np.concatenate(xList).ravel())
            y_sorted = np.sort(np.concatenate(yList).ravel())
            plt.xlim(x_sorted[0]-((0.07*amount) * amount), x_sorted[-1]+ ((0.07*amount) * amount))
            plt.ylim(y_sorted[0]-(((2**-(6-amount)) * (4))*amount), y_sorted[-1])
    
    for lnum,line in enumerate(lines):
        line.set_data(xList[lnum], yList[lnum])
  
    return lines
        
    

if __name__ == "__main__":
    main()
       