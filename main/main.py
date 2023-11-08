import pygame
from setting import *
import plants
import datetime

pygame.init()

pygame.font.init()

grid = list([list([0 for i in range(columns)]) for j in range(rows)])

listOfPlants = list([0 for i in range(columns)])

listOfPlants[0] = plants.peeShoter(20, peashooterSurf, shootLength, incrementOfPeahooter, (200, 200, 200), [0, 0], 100, peashooterSurfAlpha, costOfPeaShooter)
listOfPlants[1] = plants.sunFlower(sunflowerSurf, incrementOfSunflower, incrementOfSunDead, sunSurf, [0, 0], sunflowerSurfAlpha, costOfSunflower, producesOfSunflower)

select = 0

tmpTime = 0

clock = pygame.time.Clock()

click = True

while True:
    click = False
    # pygame.display.set_caption(str(clock.get_fps()))
    if not pygame.key.get_focused():
        timeStop = True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                click = True
                
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if not timeStop:
                                tmpTime = datetime.datetime.now()
                        else:
                            try:
                               grid[i][j].time1 += datetime.datetime.now() - tmpTime
                               grid[i][j].time2 += datetime.datetime.now() - tmpTime
                               grid[i][j].time3 += datetime.datetime.now() - tmpTime
                            except Exception as e:
                                pass
                            
                timeStop = not(timeStop)
    if (not timeStop):
        
        mousePos = pygame.mouse.get_pos()
        sc.blit(backGround, (-leftCameraX, 0))
        if click:
            iX = (mousePos[0]-marginLeftOfListOfPlants - marginLeftOfListOfPlantsEvery)/(widthOfListOfPlants+marginLeftOfListOfPlantsEvery)
            if int(iX + 0.25) != int(iX)+1 and mousePos[1] > marginTopOfListOfPlants and mousePos[1] < marginTopOfListOfPlants + heightOfListOfPlants and iX >= 0 and iX < len(listOfPlants):
                iX = int(iX)
                try:
                    if select != 0:
                        select = 0
                    elif sunsNum >= listOfPlants[iX].cost:
                        if type(listOfPlants[iX]) == plants.peeShoter:
                            select = plants.peeShoter(20, peashooterSurf, shootLength, incrementOfPeahooter, (200, 200, 200), [0, 0], 100, peashooterSurfAlpha, costOfPeaShooter)
                        if type(listOfPlants[iX]) == plants.sunFlower:
                            select = plants.sunFlower(sunflowerSurf, incrementOfSunflower, incrementOfSunDead, sunSurf, [0, 0], sunflowerSurfAlpha, costOfSunflower, producesOfSunflower)
                except:
                    pass
            else:
                if select != 0:
                    try:
                        j1 = (mousePos[0] - marginLeftOfGrid) / widthOfGrid
                        i1 = (mousePos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2)
                        if i1 >= 0 and j1 >= 0 and grid[int(i1)][int(j1)] == 0:
                            select.pos = [widthOfGrid * int(j1) + marginLeftOfGrid + widthOfGrid, 
                                        (heightOfGrid+marginTopOfGrid2) * int(i1) + marginTopOfGrid + (heightOfGrid+marginTopOfGrid2)/2 - 13 ]
                            grid[int(i1)][int(j1)] = select
                            sunsNum -= select.cost
                    except IndexError:
                        pass
                    select = 0
                else:
                    for i in grid:
                        for j in i:
                            if type(j) == plants.sunFlower:
                                print(len(j.sun), mousePos, j.sun)
                                if len(j.sun) == 2:
                                    if mousePos[0] < j.sun[0] + widthOfSun and mousePos[0] >= j.sun[0] and mousePos[1] < j.sun[1] + heightOfSun and mousePos[1] >= j.sun[1]:
                                        j.sun = []
                                        sunsNum += j.produces
        
        
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
                sc.blit(backGroundOfSeedPackSurf, (widthOfListOfPlants * i + marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery * (i+1), 
                                                            marginTopOfListOfPlants))
                sc.blit(pygame.transform.scale(listOfPlants[i].color, (widthOfIconOfListOfPlants, heightOfIconOfListOfPlants)), 
                                                            (widthOfListOfPlants * i + marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery * (i+1) + marginLeftOfIconOfListOfPlants, 
                                                            marginTopOfListOfPlants + marginTopOfIconOfListOfPlants))
                
                costSurface = costFont.render(str(listOfPlants[i].cost), False, (0, 0, 0))
                sc.blit(costSurface, (widthOfListOfPlants * i + marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery * (i+1) + padingLeftOfCost, 
                                      marginTopOfListOfPlants + padingTopOfCost))
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
                if grid[i][j] != 0:
                    grid[i][j].update(sc)
                
        if select != 0:
            try:
                sc.blit(pygame.transform.scale(select.color, (widthOfGrid, heightOfGrid)), (mousePos[0]-widthOfListOfPlants/2, 
                                                                                    mousePos[1]-heightOfListOfPlants/2))
            except:
                pass
        sunsNumSurface = sunsNumFont.render(str(sunsNum), False, (0, 0, 0), (255, 255, 255))
        
        sc.blit(sunsNumSurface, (marginLeftOfSunsNum, marginTopOfSunsNum))
    else:
        sc.blit(pygame.transform.scale(stopMenuSurf, (stopMenuWidth, stopMenuHeight)), (width/2 - stopMenuWidth / 2,
                                                                                        height/2 - stopMenuHeight / 2)) 
               
    pygame.display.update()
