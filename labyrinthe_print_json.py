import matplotlib.pyplot as pyplot
from random import randint, seed
import json


with open('labyrinthes.json') as file:
    data = json.load(file)

l = ' / '.join(list(data.keys()))
print(f'Liste des tailles : {l}')
size = input('choisissez une taille : ')
l = ' / '.join(list(data[size].keys()))
print(f'Liste des exemples : {l}')
ex = input('choisissez un exemple : ')

choice = data[size][ex]

seed(1)

size_x = size_y = int(size)

scale = max(size_x, size_y) / 8

pyplot.figure(figsize=(size_x/scale, size_y/scale))
#pyplot.xticks([])
#pyplot.yticks([])
pyplot.style.use('dark_background')


def draw_line(x1, y1, x2, y2):
  pyplot.plot([x1, x2], [y1, y2], color='white')


# maze's border
def drawMazeBorder():
  draw_line(0, 0, size_x, 0)
  draw_line(0, 0, 0, size_y)
  draw_line(size_x, 0, size_x, size_y)
  draw_line(0, size_y, size_x, size_y)
  
  
def draw_cell(x,y,walls):
    if walls[0]:
        draw_line(x,y+1,x+1,y+1)
    if walls[1]:
        draw_line(x+1,y,x+1,y+1)
    if walls[2]:
        draw_line(x,y,x+1,y)
    if walls[3]:
        draw_line(x,y,x,y+1)
        
        
def draw_maze(size, choice):
    #drawMazeBorder()   
    for i in choice:
        y = int(size) -1 - i['posX']
        x = i['posY']
        draw_cell(x,y,i['walls'])
            


draw_maze(size, choice)

#pyplot.show()
