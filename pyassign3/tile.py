#!/usr/bin/env python3

"""tile.py: A module that can print all the solutions to pave a wall(m*n) using tiles(a*b) and visualize one of them in the turtle module.

__author__ = "Xuefeng Wang"
__pkuid__  = "1800011707"
__email__  = "wang-xuefeng@pku.edu.cn"
"""

import turtle

def paved(m, n, a, b, x, y, visited):
    """Returns: bool value of the whether the region to be paved has already been partially paved or is out of the wall.
    Parameter m: the length of the wall
    Parameter n: the width of the wall
    Parameter a: the length of the tile
    Parameter b: the width of the tile
    Parameter x: the row number of the corner that has the smallest sequence number of the tile to be paved
    Parameter y: the column number of the corner that has the smallest sequence number of the tile to be paved
    Parameter visited: the list that records the state of every 1*1 square in the wall in which 1 represents paved and 0 represents unpaved
    """
    if x+b <= n and y+a <= m:
        for i in range(x, x+b):
            for j in range(y, y+a):
                if visited[i*m+j] == 1:
                    return True
        return False
    else:
        return True

def paving(m, a, b, x, y, visited, a_tile, ans):
    """Pave a tile onto the wall. Record the 1*1 square in the tile newly paved and append the tile to the answer list.
    Parameter m: the length of the wall
    Parameter a: the length of the tile
    Parameter b: the width of the tile
    Parameter x: the row number of the corner that has the smallest sequence number of the tile to be paved
    Parameter y: the column number of the corner that has the smallest sequence number of the tile to be paved
    Parameter visited: the list that records the state of every 1*1 square in the wall in which 1 represents paved and 0 represents unpaved
    Parameter a_tile: the list consisting of all the sequence numbers of the tile newly paved
    Parameter ans: one solution to pave the wall
    """
    for i in range(x, x+b):
        for j in range(y, y+a):
            visited[i*m+j] = 1
            a_tile.append(i*m+j)
    ans.append(tuple(a_tile))

def tile(m, n, a, b, visited, alls=[], ans=[], x=0, y=0):
    """Returns: all the solutions to pave the wall
    Parameter m: the length of the wall
    Parameter n: the width of the wall
    Parameter a: the length of the tile
    Parameter b: the width of the tile
    Parameter visited: the list that records the state of every 1*1 square in the wall in which 1 represents paved and 0 represents unpaved
    Parameter alls: the list consisting of all the solutions to pave the wall
    Parameter ans: one solution to pave the wall
    Parameter x: the row number of the corner that has the smallest sequence number of the tile to be paved
    Parameter y: the column number of the corner that has the smallest sequence number of the tile to be paved
    """
    a_tile=[]
    if a == b:
        if not paved(m, n, a, b, x, y, visited):
            paving(m, a, b, x, y, visited, a_tile, ans)
            if 0 in visited:
                p = visited.index(0)
                tile(m, n, a, b, visited, alls, ans, x = p//m, y = p%m)
            else:
                alls.append(ans)
    else:
        ans_1 = ans[:]
        a_tile_1 = a_tile[:]
        visited_1 = visited[:]
        if not paved(m, n, a, b, x, y, visited):
            paving(m, a, b, x, y, visited, a_tile, ans)
            if 0 in visited:
                p = visited.index(0)
                tile(m, n, a, b, visited, alls, ans, x = p//m, y = p%m)
            else:
                alls.append(ans)

        if not paved(m, n, b, a, x, y, visited_1):
            paving(m, b, a, x, y, visited_1, a_tile_1, ans_1)
            if 0 in visited_1:
                q = visited_1.index(0)
                tile(m, n, a, b, visited_1, alls, ans_1, x = q//m, y = q%m)
            else:
                alls.append(ans_1)

    return alls

def visualization(m, n, subject):
    """Visualize a selected solution in turtle module
    Parameter m: the length of the wall
    Parameter n: the width of the wall
    Parameter subject: the solution to be visualized
    """
    wn = turtle.Screen()
    flash = turtle.Turtle()
    zoom = turtle.Turtle()
    flash.speed(0)
    zoom.speed(0)
    flash.shape("blank")
    zoom.shape("blank")
    flash.pensize(4)
    zoom.color("blue")
    size = (120000/(m*n))**0.5
    f = m*size/2
    g = n*size/2
    
    for partition in subject:
        corner1 = min(partition)
        corner2 = max(partition)
        x1 = (corner1 % m)*size-f
        y1 = (corner1 // m)*size-g
        x2 = (1 + corner2 % m)*size-f
        y2 = (1 + corner2 // m)*size-g
        flash.up()
        flash.goto(x1, y1)
        flash.down()
        flash.goto(x2, y1)
        flash.goto(x2, y2)
        flash.goto(x1, y2)
        flash.goto(x1, y1)
    
    for row in range(1, n):
        zoom.up()
        zoom.goto(-f, row*size-g)
        zoom.down()
        zoom.fd(size*m)
    zoom.lt(90)
        
    for column in range(1, m):
        zoom.up()
        zoom.goto(column*size-f, -g)
        zoom.down()
        zoom.fd(size*n)
    
    for i in range(n):
        for j in range(m):
            zoom.up()
            zoom.goto(size*(j+0.54)-f, size*(i+0.34)-g)
            zoom.down()
            zoom.write(str(i*m+j), align="center", font=("Times New Roman", int(0.24*size)))
    turtle.done()
                    
def main():
    """main module
    """
    m = int(input("Please enter the length of the wall:"))
    n = int(input("Please enter the width of the wall:"))
    a = int(input("Please enter the length of the tile:"))
    b = int(input("Please enter the width of the tile:"))
    visited = [0]*(m*n)
    alls = tile(m, n, a, b, visited)
    num = len(alls)
    print("There are", num, "ways to pave this wall.")
    for i in alls:
        print(i)
    if num != 0:
        choice = turtle.numinput("Visualization", "Enter the sequence number of the paving method you want to display: (0 - "+str(num-1)+")", 0, minval=0, maxval=num-1)
        subject = alls[int(choice)]
        visualization(m, n, subject)
    else:
        print("No solution can be visualized.")

if __name__ == '__main__':
    main()
