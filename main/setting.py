import datetime
import pygame

marginLeftOfListOfPlants = 10
marginTopOfListOfPlants = 5
widthOfListOfPlants = 50
heightOfListOfPlants = 70

marginLeftOfGrid = 20
marginTopOfGrid = marginTopOfListOfPlants + heightOfListOfPlants + 10
widthOfGrid = 50
heightOfGrid = 50

marginLeftOfIconOfListOfPlants = 4
marginTopOfIconOfListOfPlants = 9
widthOfIconOfListOfPlants = 40
heightOfIconOfListOfPlants = 40

backGroundOfSeedPackSurf = pygame.image.load("C:\\Users\\Azat\\Desktop\\horror-Pvz\\horror-pvz\\main\\textures\\backGroundOfSeedPack.png")
peashooterSurf = pygame.image.load("C:\\Users\\Azat\\Desktop\\horror-Pvz\\horror-pvz\\main\\textures\\peashooter.png")

incrementOfPeahooter = datetime.timedelta(
    days=0,
    seconds=1.425,
    microseconds=0,
    milliseconds=0,
    minutes=0,
    hours=0,
    weeks=0
)