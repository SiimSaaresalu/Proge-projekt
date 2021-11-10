import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

taust = pygame.image.load('oige_pilt.jpg')
pygame.display.set_caption('Tudengi päev Tartus')
icon = pygame.image.load('images.png')
pygame.display.set_icon(icon)
 
tegelaneImg = pygame.image.load('mängTegelane.png')
tegelaneImg = pygame.transform.scale(tegelaneImg, (300, 540))
tegelaneX = 250
tegelaneY = 50
tegelaneX_change = 0

def player(x, y):
    screen.blit(tegelaneImg, (x, y))
    
def tekst_kõne(font : str, suurus : int, tekst : str, värv,x,y, bold : bool):
    font = pygame.font.Font(font, suurus)
    font.set_bold(bold)
    taust = (255, 255, 255)
    tekst = font.render(tekst, True, värv, taust)
    tekstRect = tekst.get_rect()
    tekstRect.center = (x,y)
    screen.blit(tekst, tekstRect)
    
    
    
    
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(taust, (0, 0))
    tekst_kõne('ARIALUNI.ttf', 30, 'Aeg AARi õppima minna', (0, 0, 0), 450, 140, False)
    hx, hy = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                tegelaneX_change = -1
            if event.button == 3:
                tegelaneX_change = 1
        if event.type == pygame.MOUSEBUTTONUP:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                tegelaneX_change = 0
    tegelaneX += tegelaneX_change         
    if tegelaneX <=-70:
        tegelaneX = -70
    elif tegelaneX >= 605:
        tegelaneX = 605
    player(tegelaneX, tegelaneY)
    pygame.display.update()
