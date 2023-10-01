import pygame
import sys
pygame.init()

WIDTH = 750
HEIGHT = 800
font = pygame.font.SysFont(None,80)
smaller_font = pygame.font.SysFont(None,50)
pos = None
number_entered = False
flag_submit = False
grid = [
        [0,9,0,0,0,2,7,0,5],
        [0,0,7,9,0,8,0,1,6],
        [6,0,0,3,7,0,0,9,4],
        [0,7,0,0,0,9,0,3,0],
        [8,2,0,0,0,6,4,0,0],
        [4,0,5,8,1,7,6,2,0],
        [0,0,0,0,2,3,8,0,0],
        [0,1,0,6,0,0,0,0,0],
        [0,0,0,7,9,4,1,0,3],
    ]
grid_original = [
        [0,9,0,0,0,2,7,0,5],
        [0,0,7,9,0,8,0,1,6],
        [6,0,0,3,7,0,0,9,4],
        [0,7,0,0,0,9,0,3,0],
        [8,2,0,0,0,6,4,0,0],
        [4,0,5,8,1,7,6,2,0],
        [0,0,0,0,2,3,8,0,0],
        [0,1,0,6,0,0,0,0,0],
        [0,0,0,7,9,4,1,0,3],
    ]
answer = [
    [3,9,1,4,6,2,7,8,5],
    [2,4,7,9,5,8,3,1,6],
    [6,5,8,3,7,1,2,9,4],
    [1,7,6,2,4,9,5,3,8],
    [8,2,9,5,3,6,4,7,1],
    [4,3,5,8,1,7,6,2,9],
    [9,6,4,1,2,3,8,5,7],
    [7,1,3,6,8,5,9,4,2],
    [5,8,2,7,9,4,1,6,3],
]


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def draw_background():
  global flag_submit
  if flag_submit:
    if grid == answer:
      pygame.draw.rect(win,pygame.Color('yellow'),pygame.Rect(15,15,720,100))
      text = font.render('Its Correct',True,pygame.Color('black'))
      win.blit(text,(235,40))
      tryText = smaller_font.render('Try',True,pygame.Color('black'))
      againText = smaller_font.render('Again',True,pygame.Color('black'))
      win.blit(tryText,(645,35))
      win.blit(againText,(630,65))
    else:
      # print('else')
      pygame.draw.rect(win,pygame.Color('yellow'),pygame.Rect(15,15,720,100))
      tryText = smaller_font.render('Try',True,pygame.Color('black'))
      againText = smaller_font.render('Again',True,pygame.Color('black'))
      text = font.render('Incorrect',True,pygame.Color('black'))
      win.blit(text,(235,40))
      win.blit(tryText,(645,35))
      win.blit(againText,(630,65))
  else:
    win.fill(pygame.Color('white'))
    pygame.draw.rect(win,pygame.Color('black'),pygame.Rect(15,15,720,720),10)
    i = 1
    while i*80 < 720:
      if i==3 or i==6:
          pygame.draw.line(win,pygame.Color('black'),(i*80+15,15),(i*80+15,730),10)
          pygame.draw.line(win,pygame.Color('black'),(15,i*80+15),(730,i*80+15),10)
          
      else:
          pygame.draw.line(win,pygame.Color('black'),(i*80+15,15),(i*80+15,730),4)
          pygame.draw.line(win,pygame.Color('black'),(15,i*80+15),(730,i*80+15),4)
      i+=1
    text = font.render('Submit',True,pygame.Color('black'))
    pygame.draw.rect(win,pygame.Color('yellow'),pygame.Rect(255,740,235,50))
    win.blit(text,(275,740))

def draw_numbers():
    global grid,flag_submit,grid_original
    if not flag_submit:
      for row in range(len(grid)):
          for col in range(len(grid[row])):
            number = grid[col][row]
            if grid_original[col][row]!=0:
              text = font.render(str(number),True,pygame.Color('blue'))
            else:
              text = font.render(str(number),True,pygame.Color('black'))
              
            if number != 0:
              #col == 8 is used to center the text in the last row
              if col==8:
                  win.blit(text,((row*80)+40,(col*80)+30))
              else:  
                  win.blit(text,((row*80)+40,(col*80)+35))
    


def insert(pos,key):
  if pos[0]>=0 and pos[0]<=8 and pos[1]>=0 and pos[1]<=8:
    if grid_original[pos[1]][pos[0]] != 0 :
        return
    else:
        if grid[pos[1]][pos[0]] ==  key:
          grid[pos[1]][pos[0]] = 0
        else:
          grid[pos[1]][pos[0]] = key




def game_loop():
  global pos,flag_submit,grid
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        pos = pygame.mouse.get_pos()
        if pos[0]>=625 and pos[0]<=730 and pos[1]>=32 and pos[1]<=94:
          flag_submit = False
          grid = [
                  [0,9,0,0,0,2,7,0,5],
                  [0,0,7,9,0,8,0,1,6],
                  [6,0,0,3,7,0,0,9,4],
                  [0,7,0,0,0,9,0,3,0],
                  [8,2,0,0,0,6,4,0,0],
                  [4,0,5,8,1,7,6,2,0],
                  [0,0,0,0,2,3,8,0,0],
                  [0,1,0,6,0,0,0,0,0],
                  [0,0,0,7,9,4,1,0,3],
              ]
        pos = ((pos[0]-15)//80,(pos[1]-15)//80)
        if (pos[0]>=3 and pos[0]<=5) and pos[1]==9:
          flag_submit = True
        print(pos)
        
    if event.type == pygame.KEYDOWN and not number_entered:
      insert(pos,event.key-48)
            # insert()
  draw_background()
  draw_numbers()
  # if grid == answer:
  #   pygame.draw.rect(win,pygame.Color('black'),pygame.Rect(15,15,100,100))
  # else:
  #   pygame.draw.rect(win,pygame.Color('black'),pygame.Rect(15,15,720,100))
     
  pygame.display.update()
  
while True:
  game_loop()