import matplotlib.pyplot as pyplot
from random import randint, seed

seed(1)

size_x = 10
size_y = 10

# each cell is represent by 2 bits which are top and left wall
# generating a random maze

maze = [[ randint(0,3) for i in range(size_x) ] for j in range(size_y) ]


scale = max(size_x, size_y) / 8

pyplot.figure(figsize=(size_x/scale, size_y/scale))
#pyplot.xticks([])
#pyplot.yticks([])
pyplot.style.use('dark_background')


def draw_line(x1, y1, x2, y2):
  pyplot.plot([x1, x2], [y1, y2], color='white')


def int_to_bool_list(num):
    return [bool(num & (1<<n)) for n in range(2)]


# maze's border
def drawMazeBorder():
  draw_line(0, 0, size_x, 0)
  draw_line(0, 0, 0, size_y)
  draw_line(size_x, 0, size_x, size_y)
  draw_line(0, size_y, size_x, size_y)
  
  
def draw_cell(x,y,walls):
    if walls[0]:
        draw_line(x,y,x,y+1)
    if walls[1]:
        draw_line(x,y,x+1,y)
        
def draw_maze():
    drawMazeBorder()   
    for index_line, line in enumerate(maze) :
        for index_cell, cell in enumerate(line):
            draw_cell(index_line,index_cell,int_to_bool_list(cell))


draw_maze()

#pyplot.show()
