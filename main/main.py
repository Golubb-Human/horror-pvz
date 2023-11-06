import pygame
from setting import *
import plants

pygame.init()

grid = list([list([0 for i in range(columns)]) for j in range(rows)])

listOfPlants = list([0 for i in range(columns)])

listOfPlants[0] = 1
listOfPlants[1] = 2

textures = {1: peashooterSurf, 2: sunflowerSurf}

select = 0

sunsNums = 50

while True:
    mousePos = pygame.mouse.get_pos()
    sc.blit(backGround, (-leftCameraX, 0))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                iX = (mousePos[0]-marginLeftOfListOfPlants)/(widthOfListOfPlants+marginLeftOfListOfPlants)
                if int(iX + 0.25) != int(iX)+1 and mousePos[1] > marginTopOfListOfPlants and mousePos[1] < marginTopOfListOfPlants + heightOfListOfPlants:
                    iX = int(iX)
                    if listOfPlants[iX] == 1:
                        select = plants.peeShoter(20, peashooterSurf, shootLength, incrementOfPeahooter, (200, 200, 200), [0, 0], 100, peashooterSurfAlpha, costOfPeaShooter)
                    if listOfPlants[iX] == 2:
                        select = plants.sunFlower(sunflowerSurf, incrementOfSunflower, incrementOfSunDead, sunSurf, [0, 0], sunflowerSurfAlpha, costOfSunflower)
                else:
                    if select != 0:
                        try:
                            j1 = (mousePos[0] - marginLeftOfGrid) / widthOfGrid
                            i1 = (mousePos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2)
                            if i1 >= 0 and j1 >= 0 and grid[int(i1)][int(j1)] == 0:
                                select.pos = [widthOfGrid * int(j1) + marginLeftOfGrid + widthOfGrid, 
                                            (heightOfGrid+marginTopOfGrid2) * int(i1) + marginTopOfGrid + (heightOfGrid+marginTopOfGrid2)/2 - 13 ]
                                grid[int(i1)][int(j1)] = select
                        except IndexError:
                            pass
                        select = 0
    
    
    if select != 0:
        try:
            j1 = (mousePos[0] - marginLeftOfGrid) / widthOfGrid
            i1 = (mousePos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2)
            if i1 >= 0 and j1 >= 0 and i1 < rows and j1 < columns and grid[int(i1)][int(j1)] == 0:
                sc.blit(pygame.transform.scale(select.colorAlpha, (widthOfGrid, heightOfGrid)), (widthOfGrid * int(j1) + marginLeftOfGrid, 
                                                (heightOfGrid+marginTopOfGrid2) * int(i1) + marginTopOfGrid + marginTopOfGrid2))

        except IndexError:
            pass
    
    for i in range(len(listOfPlants)):
        if listOfPlants[i] != 0:
            sc.blit(backGroundOfSeedPackSurf, (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1), 
                                                        marginTopOfListOfPlants))
            sc.blit(pygame.transform.scale(textures[listOfPlants[i]], (widthOfIconOfListOfPlants, heightOfIconOfListOfPlants)), 
                                                        (widthOfListOfPlants * i + marginLeftOfListOfPlants * (i+1) + marginLeftOfIconOfListOfPlants * (i+1), 
                                                        marginTopOfListOfPlants + marginTopOfIconOfListOfPlants))
        else:
            break
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                sc.blit(pygame.transform.scale(grid[i][j].color, (widthOfGrid, heightOfGrid)), (widthOfGrid * j + marginLeftOfGrid, 
                                                                                                marginTopOfGrid + heightOfGrid * i + marginTopOfGrid2*(i+1)))
            except AttributeError:
                pass
           
    for i in range(len(grid)):
        for j in range(len(grid[i])): 
            try:
                grid[i][j].update(sc)
            except AttributeError:
                pass
            
    if select != 0:
        try:
            sc.blit(pygame.transform.scale(select.color, (widthOfGrid, heightOfGrid)), (mousePos[0]-widthOfListOfPlants/2, 
                                                                                mousePos[1]-heightOfListOfPlants/2))
        except:
            pass
            
    pygame.display.update()
