import pygame

pygame.init()

ekraan_laius = 800
ekraan_pikkus = 600
screen = pygame.display.set_mode((ekraan_laius, ekraan_pikkus))

taust = pygame.image.load('oige_pilt.jpg')
pygame.display.set_caption('Tudengi päev Tartus')
icon = pygame.image.load('images.png')
pygame.display.set_icon(icon)
 
tegelaneImg = pygame.image.load('mängTegelane.png')
tegelaneImg = pygame.transform.scale(tegelaneImg, (300, 540))
õnnelikTegelane = pygame.image.load('tegelaneÕnnelik.png')
õnnelikTegelane = pygame.transform.scale(õnnelikTegelane, (300, 540))
X = 250
Y = 50
#see on minu kommentaar
X_change = 0
Y_change = 0
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
valik1 = 590, 180
valik2 = 590, 220
vasak_klõps = False    
    
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(taust, (0, 0))
    tekst_kõne('ARIALUNI.ttf', 20, 'Tere hommikust! On reede, kell on 12 ning sul on valik:', (0, 0, 0), 550, 140, False)
    tekst_kõne('ARIALUNI.ttf', 16, 'a) kas sa lähed AARi tundi kus toimub kontrolltöö või;', (0, 0, 0), 590, 180, False)
    tekst_kõne('ARIALUNI.ttf', 16, 'b) läheb käiku plaan Netflix ', (0, 0, 0), 590, 220, False)
    hx, hy = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                vasak_klõps = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                vasak_klõps = False
    if vasak_klõps == True:
        if (hx, hy) == valik1:
            ()
        if (hx, hy) == valik2:
            ()
    player(X, Y)
    pygame.display.update()
