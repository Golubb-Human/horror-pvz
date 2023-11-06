import datetime
import pygame

pygame.init()

width, height = 640, 480

sc = pygame.display.set_mode((width, height))

marginLeftOfListOfPlants = 10
marginTopOfListOfPlants = 5
widthOfListOfPlants = 50
heightOfListOfPlants = 70

marginLeftOfGrid = 130
marginTopOfGrid = marginTopOfListOfPlants + heightOfListOfPlants + 2
marginTopOfGrid2 = 10
widthOfGrid = 52
heightOfGrid = 68 - marginTopOfGrid2

marginLeftOfIconOfListOfPlants = 4
marginTopOfIconOfListOfPlants = 9
widthOfIconOfListOfPlants = 40
heightOfIconOfListOfPlants = 40

leftCameraX = 44

backGroundOfSeedPackSurf = pygame.image.load("textures\\backGroundOfSeedPack.png")
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
costOfSunflower = 100

widthOfSun = 20
heightOfSun = 20

columns = 9
rows = 5