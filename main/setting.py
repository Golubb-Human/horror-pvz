import datetime
import pygame

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
backGround = pygame.image.load("textures\\background.png")

incrementOfPeahooter = datetime.timedelta(
    days=0,
    seconds=1.425,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0
)