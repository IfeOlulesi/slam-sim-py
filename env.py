import math
import pygame

class buildEnvironment:
  def __init__ (self, MapDimensions):
    pygame.init()

    self.pointCloud = []
    self.externalMap = pygame.image.load('plans/floorplan-1.png')
    self.mapHeight, self.mapWidth = MapDimensions
    
    # Set window name
    self.MapWindowName = 'RRT path planning'
    pygame.display.set_caption(self.MapWindowName)

    self.map = pygame.display.set_mode((self.mapWidth, self.mapHeight))
    self.map.blit(self.externalMap, (0,0)) # overlays the floorplan image

    # Colors in RGB format
    self.black = (0, 0, 0)
    self.white = (255, 255, 255)
    self.grey = (70, 70, 70)
    
    self.blue = (0, 0, 255)
    self.green = (0, 255, 0)
    self.red = (255, 0, 0)

  def AD2pos(self, distance, angle, robotPosition):
    x = distance * math.cos(angle) + robotPosition[0]
    y = -distance * math.sin(angle) + robotPosition[1]
    return (int(x), int(y))
  

  def dataStorage(self, data):
    print(len(self.pointCloud))

    for element in data:
      point = self.AD2pos(element[0], element[1], element[2])
      if point not in self.pointCloud:
        self.pointCloud.append(point)


  def show_sensorData(self):
    self.infomap = self.map.copy()

    for point in self.pointCloud:
      self.infomap.set_at((int(point[0]), int(point[1])), self.red)