import math

def findHighPoint(given_map):
 
    max_height = 0
    x_cord = 0
    y_cord = 0
    ele_count = 0
    W = given_map.W
    H = given_map.H
    quality_score = W * H * (0.1/100)
    
    for x in range(0, W, math.floor(W/(W+H)* 68)):
        for y in range(0, H, math.ceil(H/(W+H)* 68)):
            temp_height = given_map.getElevation(x, y)
            
            ele_count += 1
    
            if temp_height > max_height:
                max_height = temp_height
                x_cord = x
                y_cord = y
    
    prev_point = [x_cord, y_cord]

    while ele_count != quality_score:
        north = [x_cord, min(y_cord + 1, H)]
        east = [min(x_cord + 1, W), y_cord]
        south = [x_cord, max(y_cord - 1, 0)]
        west = [max(x_cord - 1, 0), y_cord]
        
        points = [north, east, south, west]
        if prev_point in points:
            points.remove(prev_point)
        
        ele_count += len(points)
        if ele_count >= quality_score:
            break
        
        elevations = [given_map.getElevation(x[0], x[1]) for x in points]
        elevations.append(max_height)
        points.append([x_cord, y_cord])
        max_point = points[elevations.index(max(elevations))]
        
        if (max_point[0] == x_cord and max_point[1] == y_cord):
            break
        
        else:
            prev_point = [x_cord, y_cord]
            x_cord = max_point[0]
            y_cord = max_point[1]
            max_height = max(elevations)

    return [x_cord, y_cord]
