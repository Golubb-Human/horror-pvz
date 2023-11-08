import datetime
import pygame

pygame.init()

width, height = 640, 480

sc = pygame.display.set_mode((width, height))

marginLeftOfSunsNum = 10
marginTopOfSunsNum = 20

marginLeftOfListOfPlants = marginLeftOfSunsNum + 70
marginLeftOfListOfPlantsEvery = 10
marginTopOfListOfPlants = 5
widthOfListOfPlants = 50
heightOfListOfPlants = 70

marginLeftOfGrid = 130
marginTopOfGrid = marginTopOfListOfPlants + heightOfListOfPlants + 2
marginTopOfGrid2 = 10
widthOfGrid = 52
heightOfGrid = 68 - marginTopOfGrid2

marginLeftOfIconOfListOfPlants = 6
marginTopOfIconOfListOfPlants = 9
widthOfIconOfListOfPlants = 35
heightOfIconOfListOfPlants = 40

padingLeftOfCost = 5
padingTopOfCost = 47

leftCameraX = 44

backGroundOfSeedPackSurf = pygame.image.load("textures\\backGroundOfSeedPack.png")
stopMenuSurf = pygame.image.load("textures\\stopMenu.png")
peashooterSurf = pygame.image.load("textures\\peashooter.png")
sunflowerSurf = pygame.image.load("textures\\sunflower.png")
sunSurf = pygame.image.load("textures\\sun.png")
backGround = pygame.image.load("textures\\background.png")

alpha = 100
peashooterSurfAlpha = peashooterSurf.convert_alpha()
peashooterSurfAlpha.set_alpha(alpha)
sunflowerSurfAlpha = sunflowerSurf.convert_alpha()
sunflowerSurfAlpha.set_alpha(alpha)

incrementOfPeahooter = datetime.timedelta(seconds=1.425)
incrementOfSunflower = datetime.timedelta(seconds=24)
incrementOfSunDead = datetime.timedelta(seconds=7)

shootLength = 10

costOfPeaShooter = 100
costOfSunflower = 50

widthOfSun = 30
heightOfSun = 30

columns = 9
rows = 5

stopMenuWidth = 200
stopMenuHeight = 200

timeStop = False

sunsNumFont = pygame.font.SysFont('Comforter Brush Regular', 40)
costFont = pygame.font.SysFont('Comforter Brush Regular', 20)
menuFont = pygame.font.SysFont('Comforter Brush Regular', 20)
menuFont2 = pygame.font.SysFont('Comforter Brush Regular', 20)

producesOfSunflower = 25

sunsNum = 10000

menuText1 = "toMenu"
menuText2 = "back"

marginLeftOfTextMenu1 = 0
marginTopOfTextMenu1 = 60
marginLeftOfTextMenu2 = 0
marginTopOfTextMenu2 = 125

widthOfZombie = widthOfGrid
heightOfZombie = heightOfGrid * 1.8

damageOfPeashooter = 10
damageOfZombieDefault = 2

healthOfPeashooter = 20
healthOfSunflower = 20