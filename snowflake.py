import numpy as np

"""
Reference: https://programmer.group/use-matplotlib-to-draw-snowflakes-and-snow-scenes.html
"""


# generate the three additional points (u,v,w) for the koch curve of a line pq
def koch_curve(p, q):
    p, q = np.array(p), np.array(q)
    
    u = p + (q-p)/3 
    v = q - (q-p)/3 
    
    # w = turning the line uv around the u point anticlockwise by 60°
    angle = np.radians(60)
    w = np.dot(v-u, np.array([[np.cos(angle), np.sin(angle)],[-np.sin(angle), np.cos(angle)]])) + u
   
    return u.tolist(), v.tolist(), w.tolist()
    
    
# generate koch snowflake for a triangle with certain depth
def snow(triangle, depth):
    
    for i in range(depth):
        result = list()
        t_len = len(triangle)
        
        for j in range(t_len):
            p = triangle[j]
            q = triangle[(j+1)%t_len]
            u, v, w = koch_curve(p, q)
            result.extend([p, u, w, v])
            
        triangle = result.copy()
    
    triangle.append(triangle[0])
    return triangle