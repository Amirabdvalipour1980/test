import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))

x = 400
y = 300
a = 0
b = 0
xr = 350
yr = 550
breaks = []
row = [True] * 7

print(breaks)
print(row)

s = [[0,0,0],[0,0,0],[0,0,0]]
n=False
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      print("Mouse button is pressed")
      x,y=pygame.mouse.get_pos()
      print(x,y)
      for i in range(3):
        for j in range(3):
          if x>i*200 and x<(i+1)*200 and y>j*200 and y<(j+1)*200 and s[i][j]==0:
            if n:
              s[i][j]=1
            else:
              s[i][j]=2
            n=not n

  if s[0][0] != 0 and s[1][0] != 0 and s[2][0] != 0 and s[0][1] != 0 and s[0][2] != 0 and s[1][2] != 0 and s[2][1] != 0 and s[1][1] != 0 and s[2][2] != 0:
     s = [[0,0,0],[0,0,0],[0,0,0]]
  screen.fill((0, 0, 0))
  ###############

  for j in range(112, 54, 22): 
   for i in range(10, 700, 110):
    pygame.draw.rect(screen, (200, 0, 100), (i, j, 100, 40))
      
   
  pygame.draw.line(screen,(255,98,255),(200,0),(200,600),1)
  pygame.draw.line(screen,(255,98,255),(400,0),(400,600),1)
  pygame.draw.line(screen,(255,98,255),(0,200),(600,200),1)
  pygame.draw.line(screen,(255,98,255),(0,400),(600,400),1)        

  for i in range(3):
    for j in range(3):
      if s[i][j]==1:
        pygame.draw.circle(screen,(255,98,255),(i*200+100, j*200+100), 50)

      if s[i][j]==2:
          pygame.draw.line(screen,(255,98,255),(i*200+100-50,j*200+100-50),(i*200+100+50,j*200+100+50),1)
          pygame.draw.line(screen,(255,98,255),(i*200+100-50,j*200+100+50),(i*200+100+50,j*200+100-50),1) 


  pygame.display.update()