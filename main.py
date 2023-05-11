import pygame

display_width = 1200
display_height = 800
def cow(x,y):
    screen.blit(cowimg, (x,y))

def gra(x,y):
    screen.blit(grass, (x,y))

def clo(x,y):
    screen.blit(cloud, (x,y))
    
def farmer(x,y): 
    screen.blit(joe, (x,y))

pygame.init()

screen = pygame.display.set_mode([display_width, display_height])
cowimg = pygame.image.load('cow3.png')
grass = pygame.image.load('grass2.png')
cloud = pygame.image.load('clouds.png')
joe = pygame.image.load('farmer joe.png')

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((135, 206, 235))
    cow(300, 400)
    gra(300, 580)
    clo(300, 0)
    farmer(400, 400)





    # Draw a solid blue circle in the center
    #pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
