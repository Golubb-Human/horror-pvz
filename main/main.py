import pygame
from setting import *

pygame.init()

width, height = 640, 480

sc = pygame.display.set_mode((width, height))

grid = list([list([1 for i in range(9)]) for j in range(5)])

listOfPlants = list([0 for i in range(9)])

listOfPlants[0] = 1
listOfPlants[1] = 2

plants = {1:(4,255,63), 2:(251,255,28)}

select = 0

while True:
    mousePos = pygame.mouse.get_pos()
    sc.fill((0, 0, 0))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                iX = (mousePos[0]-marginLeftOfListOfPlants)/(widthOfListOfPlants+marginLeftOfListOfPlants)
                if int(iX + 0.25) != int(iX)+1 and mousePos[1] > marginTopOfListOfPlants and mousePos[1] < marginTopOfListOfPlants + heightOfListOfPlants:
                    iX = int(iX)
                    select = listOfPlants[iX]
                else:
                    select = 0
    
    for i in range(len(listOfPlants)):
        if listOfPlants[i] != 0:
            pygame.draw.rect(sc, plants[listOfPlants[i]], (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1), 
                                                        marginTopOfListOfPlants, 
                                                        widthOfListOfPlants, 
                                                        heightOfListOfPlants))
        else:
            break
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if grid[i] != 0:
            pygame.draw.rect(sc, plants[grid[i][j]], (widthOfGrid * j + marginLeftOfGrid, 
                                                    marginTopOfGrid + heightOfGrid * i, 
                                                    widthOfGrid, 
                                                    heightOfGrid),
                            1)
        # else:
        #     break
    if select != 0:
        pygame.draw.rect(sc, plants[select], (mousePos[0]-widthOfListOfPlants/2, mousePos[1]-heightOfListOfPlants/2, widthOfListOfPlants, heightOfListOfPlants))
            
    pygame.display.update()
