import pygame
from setting import *

pygame.init()

width, height = 640, 480

sc = pygame.display.set_mode((width, height))

grid = list([list([0 for i in range(9)]) for j in range(5)])

listOfPlants = list([0 for i in range(9)])

listOfPlants[0] = 1

textures = {1: peashooterSurf}

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
                    if listOfPlants[iX] == 1:
                        select = plants.peeShoter(20, peashooterSurf, 9, incrementOfPeahooter, (200, 200, 200), [0, 0], 100)
                else:
                    if select != 0:
                        try:
                            j1 = (mousePos[0] - marginLeftOfGrid) / widthOfGrid
                            i1 = (mousePos[1] - marginTopOfGrid) / heightOfGrid
                            if i1 >= 0 and j1 >= 0:
                                select.pos = [widthOfGrid * int(j1) + marginLeftOfGrid + widthOfGrid, 
                                            heightOfGrid * int(i1) + marginTopOfGrid + heightOfGrid/2 - 13 ]
                                print(select.pos)
                                grid[int(i1)][int(j1)] = select
                        except IndexError:
                            pass
                        select = 0
    
    for i in range(len(listOfPlants)):
        if listOfPlants[i] != 0:
            sc.blit(backGroundOfSeedPackSurf, (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1), 
                                                        marginTopOfListOfPlants))
            sc.blit(pygame.transform.scale(textures[listOfPlants[i]], (widthOfIconOfListOfPlants, heightOfIconOfListOfPlants)), 
                                                        (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1) + marginLeftOfIconOfListOfPlants * (i+1), 
                                                        marginTopOfListOfPlants + marginTopOfIconOfListOfPlants))
            # pygame.draw.rect(sc, plants[listOfPlants[i]], (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1), 
            #                                             marginTopOfListOfPlants, 
            #                                             widthOfListOfPlants, 
            #                                             heightOfListOfPlants))
        else:
            break
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # if grid[i] != 0:
            pygame.draw.rect(sc, (200, 200, 200), (widthOfGrid * j + marginLeftOfGrid, 
                                                    heightOfGrid * i + marginTopOfGrid, 
                                                    widthOfGrid, 
                                                    heightOfGrid), 1)
            try:
                sc.blit(pygame.transform.scale(grid[i][j].color, (widthOfGrid, heightOfGrid)), (widthOfGrid * j + marginLeftOfGrid, 
                                                                                              marginTopOfGrid + heightOfGrid * i))
                grid[i][j].update(sc)
            except Exception as e:
                # print(e, "x: ", j, "y: ", i)
                pass
            # else:
        #     break
    if select != 0:
        try:
            sc.blit(pygame.transform.scale(select.color, (widthOfGrid, heightOfGrid)), (mousePos[0]-widthOfListOfPlants/2, 
                                                                                mousePos[1]-heightOfListOfPlants/2))
        except:
            pass
            
    pygame.display.update()
