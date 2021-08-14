import numpy as np



def rotate(p, d):
    """Return point p Rotate counterclockwise around the origin d Coordinates of degree"""
    
    a = np.radians(d)
    m = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])
    return np.dot(p, m)

def koch_curve(p, q):
    """Line segment pq Generate koch curve, return to uvw Three points"""
    
    p, q = np.array(p), np.array(q)
    u = p + (q-p)/3 # The coordinates of the third point u
    v = q - (q-p)/3 # The coordinate of the third point V
    w = rotate(v-u, 60) + u # The coordinate of point w can be obtained by turning the line uv around the u point anticlockwise by 60 °
    
    return u.tolist(), v.tolist(), w.tolist()
    
def snow(triangle, k):
    """Given a triangle, a closed Koch snowflake is generated"""
    
    for i in range(k):
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