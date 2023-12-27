import pygame
from setting import *
import plants
import datetime
import level
import zombie
import random

def sortByPosition(List):
    List_ = List.copy()
    for i in range(len(List_)):
        for j in range(len(List_)-i-1):
            if List_[j].pos[0] > List_[j+1].pos[0]:
                List_[j], List_[j+1] = List_[j+1], List_[j]
    
    return List_


pygame.init()

pygame.font.init()

grid = list([list([0 for i in range(columns)]) for j in range(rows)])

listOfPlants = list([0 for i in range(columns)])

listOfPlants[0] = plants.peeShoter(20, peashooterSurf, shootLength, incrementOfPeahooter, (200, 200, 200), [0, 0], 100, peashooterSurfAlpha, costOfPeaShooter, healthOfPeashooter)
listOfPlants[1] = plants.sunFlower(sunflowerSurf, incrementOfSunflower, incrementOfSunDead, sunSurf, [0, 0], sunflowerSurfAlpha, costOfSunflower, producesOfSunflower, healthOfSunflower)

select = 0

tmpTime = datetime.datetime.now()

clock = pygame.time.Clock()

click = True

zombies = []
isFocus = True
timeStop = False

def stop():
    global timeStop
    global tmpTime
    global click
    global isFocus
    click = False
    if not pygame.key.get_focused():
        if isFocus:
            timeStop = True
            tmpTime = datetime.datetime.now()
            isFocus = False
    else:
        isFocus = True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                click = True
                
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                if not timeStop:
                    tmpTime = datetime.datetime.now()
                else:
                    for i in range(len(grid)):
                        for j in range(len(grid[i])):
                                try:
                                    grid[i][j].timeReset(tmpTime)
                                except Exception as e:
                                    # print(e)
                                    pass
                    
                    Level.timeStartWave = datetime.datetime.now()
                    Level.timeEndWave += datetime.datetime.now() - tmpTime
                    for i in range(len(zombies)):
                        zombies[i].time1 += datetime.datetime.now() - tmpTime
                        # grid[i][j].time2 += datetime.datetime.now() - tmpTime
                            
                timeStop = not(timeStop)

def drawList(listOfItems, WIDTH, HEIGHT, x, y, xMultiplier, yMultiplier = 0):
    for i in range(len(listOfItems)):
        if listOfItems[i] != 0:
            sc.blit(pygame.transform.scale(listOfPlants[i].color, (WIDTH, HEIGHT)), 
                                                        (xMultiplier * i + x, 
                                                         yMultiplier * i + y))
        else:
            break
def drawGrid(grid, WIDTH, HEIGHT, x, y, xMultiplier, yMultiplier):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            try:
                sc.blit(pygame.transform.scale(grid[i][j].color, (WIDTH, HEIGHT)), (x + xMultiplier*j, 
                                                                                    y + yMultiplier*i))
            except AttributeError:
                pass
def drawListOneTexture(texture, listOfItems, WIDTH, HEIGHT, x, y, xMultiplier, yMultiplier):
    for i in range(len(listOfItems)):
        if listOfItems[i] != 0:
            sc.blit(pygame.transform.scale(texture, (WIDTH, HEIGHT)), 
                                                        (xMultiplier * i + x, 
                                                         yMultiplier * i + y))
        else:
            break
def drawListCost(listOfItems, x, y, xMultiplier, yMultiplier = 0):
    for i in range(len(listOfItems)):
        if listOfItems[i] != 0:
            costSurface = costFont.render(str(listOfPlants[i].cost), False, (0, 0, 0))
            sc.blit(costSurface, (xMultiplier * i + x, yMultiplier * i + y))
        else:
            break
    
def toPut():
    global mousePos
    global select
    global sunsNum
    try:
        j1 = (mousePos[0] - marginLeftOfGrid) / widthOfGrid
        i1 = (mousePos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2)
        if i1 >= 0 and j1 >= 0 and i1 < rows and j1 < columns and grid[int(i1)][int(j1)] == 0:
            select.pos = [widthOfGrid * int(j1) + marginLeftOfGrid + widthOfGrid, 
                        (heightOfGrid+marginTopOfGrid2) * int(i1) + marginTopOfGrid + (heightOfGrid+marginTopOfGrid2)/2 - 13 ]
            grid[int(i1)][int(j1)] = select
            sunsNum -= select.cost
    except IndexError:
        pass
    select = 0

def choose(indexOfListhOfPlants):
    global select
    indexOfListhOfPlants = int(indexOfListhOfPlants)
    try:
        if select != 0:
            select = 0
        elif sunsNum >= listOfPlants[indexOfListhOfPlants].cost:
            if type(listOfPlants[indexOfListhOfPlants]) == plants.peeShoter:
                select = plants.peeShoter(damageOfPeashooter, peashooterSurf, shootLength, incrementOfPeahooter, (200, 200, 200), [0, 0], 100, peashooterSurfAlpha, costOfPeaShooter, healthOfSunflower)
            if type(listOfPlants[indexOfListhOfPlants]) == plants.sunFlower:
                select = plants.sunFlower(sunflowerSurf, incrementOfSunflower, incrementOfSunDead, sunSurf, [0, 0], sunflowerSurfAlpha, costOfSunflower, producesOfSunflower, healthOfSunflower)
    except:
        pass

def pickUpSuns():
    global mousePos
    global sunsNum
    for i in grid:
        for j in i:
            if type(j) == plants.sunFlower:
                if len(j.sun) == 2:
                    if mousePos[0] < j.sun[0] + widthOfSun and mousePos[0] >= j.sun[0] and mousePos[1] < j.sun[1] + heightOfSun and mousePos[1] >= j.sun[1]:
                        j.sun = []
                        sunsNum += j.produces

def onClick():
    global select
    global mousePos
    indexOfListhOfPlants = (mousePos[0]-marginLeftOfListOfPlants - marginLeftOfListOfPlantsEvery)/(widthOfListOfPlants+marginLeftOfListOfPlantsEvery)
    if int(indexOfListhOfPlants + 0.25) != int(indexOfListhOfPlants)+1 and mousePos[1] > marginTopOfListOfPlants and mousePos[1] < marginTopOfListOfPlants + heightOfListOfPlants and indexOfListhOfPlants >= 0 and indexOfListhOfPlants < len(listOfPlants):
        choose(indexOfListhOfPlants)
    else:
        if select != 0:
            toPut()
        else:
            pickUpSuns()

def events():
    global mousePos
    global zombies
    if (not timeStop):
        if not Level.end:
            ret = Level.update(zombieCosts)
            if ret != None:
                for i in ret:
                    iRand = random.randint(0, rows-1)
                    zombies.append(i(healthOfDefaultZombie, damageOfZombieDefault, intervalOfZombieDefault, (100,175,63), [width,  marginTopOfGrid + heightOfGrid * iRand + marginTopOfGrid2*(iRand+1)], speedOfZombieDefault))
        zombies = sortByPosition(zombies)
        
        mousePos = pygame.mouse.get_pos()
        sc.blit(backGround, (-leftCameraX, 0))
        sc.blit(pygame.transform.scale(backGroundOfListOfPlantsSurf, (widthOfBackGroundOfListOfPlants, heightOfBackGroundOfListOfPlants)), (marginLeftOfBackGroundOfListOfPlants, marginTopOfBackGroundOfListOfPlants))
        if click:
            onClick()

def drawMenu():
    sc.blit(pygame.transform.scale(stopMenuSurf, (stopMenuWidth, stopMenuHeight)), (width/2 - stopMenuWidth / 2,
                                                                                    height/2 - stopMenuHeight / 2)) 
    menuSurface1 = sunsNumFont.render(menuText1, False, (0, 0, 0))
    menuTextRect1 = menuSurface1.get_rect(center=(width / 2 + marginLeftOfTextMenu1,
                                                    height / 2 - stopMenuHeight / 2 + marginTopOfTextMenu1))
    sc.blit(menuSurface1, menuTextRect1)
    
    menuSurface2 = sunsNumFont.render(menuText2, False, (0, 0, 0))
    menuTextRect2 = menuSurface2.get_rect(center=(width / 2 + marginLeftOfTextMenu2,
                                                    height / 2 - stopMenuHeight / 2 + marginTopOfTextMenu2))
    sc.blit(menuSurface2, menuTextRect2)

while True:
    stop()
    
    events()
        
    if not timeStop:
        
        drawListOneTexture(backGroundOfSeedPackSurf,
                 listOfPlants, 
                 widthOfListOfPlants, 
                 heightOfListOfPlants, 
                 marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery, 
                 marginTopOfListOfPlants, 
                 marginLeftOfListOfPlantsEvery + widthOfListOfPlants, 
                 0)
        drawList(listOfPlants, 
                 widthOfIconOfListOfPlants, 
                 heightOfIconOfListOfPlants, 
                 marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery + marginLeftOfIconOfListOfPlants, 
                 marginTopOfListOfPlants + marginTopOfIconOfListOfPlants, 
                 marginLeftOfListOfPlantsEvery + widthOfListOfPlants)
        drawListCost(listOfPlants,
                 marginLeftOfListOfPlants + marginLeftOfListOfPlantsEvery + marginLeftOfCost, 
                 marginTopOfListOfPlants + marginTopOfCost, 
                 marginLeftOfListOfPlantsEvery + widthOfListOfPlants)
        drawGrid(grid, widthOfGrid, heightOfGrid, marginLeftOfGrid, marginTopOfGrid + marginTopOfGrid2, widthOfGrid, heightOfGrid + marginTopOfGrid2)
        for i in range(len(zombies)):
            try:
                zombies[i].update(grid)
                if zombies[i].life == False:
                    del zombies[i]
                else:
                    pygame.draw.rect(sc, zombies[i].color, (zombies[i].pos[0], zombies[i].pos[1] - heightOfGrid, widthOfZombie, heightOfZombie))
                    pygame.draw.rect(sc, (0, 0, 0), (zombies[i].pos[0], zombies[i].pos[1] - heightOfGrid, widthOfZombie, heightOfZombie), 2)
            except IndexError:
                pass
            
        for i in range(len(grid)):
            for j in range(len(grid[i])): 
                if grid[i][j] != 0:
                    if grid[i][j].life == False:
                        grid[i][j] = 0
                    else:
                        grid[i][j].update(sc, zombies)
                
        if select != 0:
            try:
                sc.blit(pygame.transform.scale(select.color, (widthOfGrid, heightOfGrid)), (mousePos[0]-widthOfListOfPlants/2, 
                                                                                    mousePos[1]-heightOfListOfPlants/2))
                
                j1 = ((mousePos[0] - marginLeftOfGrid) / widthOfGrid)
                i1 = ((mousePos[1] - marginTopOfGrid) / (heightOfGrid+marginTopOfGrid2))
                if i1 >= 0 and j1 >= 0 and i1 < rows and j1 < columns:
                    if grid[int(i1)][int(j1)] == 0:
                        sc.blit(pygame.transform.scale(select.colorAlpha, (widthOfGrid, heightOfGrid)), (marginLeftOfGrid + (int(j1) * widthOfGrid), 
                                                                                    marginTopOfGrid + marginTopOfGrid2 + (int(i1) * marginTopOfGrid2)+(int(i1) * heightOfGrid)))
            except:
                pass
        sunsNumSurface = sunsNumFont.render(str(sunsNum), False, (0, 0, 0))
        
        sc.blit(sunsNumSurface, (marginLeftOfSunsNum, marginTopOfSunsNum))
    else:
        drawMenu()
               
    pygame.display.update()