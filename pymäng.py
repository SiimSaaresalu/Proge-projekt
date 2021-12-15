import pygame

pygame.init()

# see osa võtab tekstifailist teksti ja paneb need sõnastikku valikud kirja kujul
# STSEENINIMI: põhitekst, esimese valiku tekst: (järgmine taust, järgmise stseeni nimi), teise valiku tekst: (järgmine taust, järgmise stseeni nimi)

f = open("lizetekst.txt", encoding="utf-8")
read = f.readlines()
valikud = dict()
for rida in read:
    reasisu = rida.strip().split("/")
    if reasisu[0] == 'AAR-LÕPP' or reasisu[0] == 'KAINE-LÕPP' or reasisu[0] == 'EKSMAT-LÕPP' or reasisu[0] == 'MÄNG-LÕPP' or reasisu[0] == 'BLACKOUT-LÕPP':
        valikud[reasisu[0]] = reasisu[1]
    else:
        valikud[reasisu[0]] = (reasisu[1], reasisu[2], reasisu[3], reasisu[4], reasisu[5], reasisu[6], reasisu[7])
praegune_stseen = "ALGUS"

#ekraan

ekraan_laius = 1280
ekraan_pikkus = 720
screen = pygame.display.set_mode((ekraan_laius, ekraan_pikkus))

pygame.display.set_caption('Tudengi päev Tartus')
icon = pygame.image.load('images.png')
pygame.display.set_icon(icon)

#taustapildid

taustapildid = {'Korter': pygame.transform.scale(pygame.image.load('korter.jpg'), (1280, 720)),
                'Pood': pygame.transform.scale(pygame.image.load('pood.jpg'), (1280, 720)),
                'AAR': pygame.transform.scale(pygame.image.load('AAR.jpg'), (1280, 720)),
                'Trepp-esik': pygame.transform.scale(pygame.image.load('trepp ees.jpg'), (1280, 720)),
                'Trepp-põhi': pygame.transform.scale(pygame.image.load('trepp pohi.jpg'), (1280, 720)),
                'Gen-ees': pygame.transform.scale(pygame.image.load('gen ees.jpg'), (1280, 720)),
                'Gen-sees1': pygame.transform.scale(pygame.image.load('gen sees1.jpg'), (1280, 720)),
                'Gen-sees2': pygame.transform.scale(pygame.image.load('gen sees2.jpg'), (1280, 720)),
                'Must': pygame.transform.scale(pygame.image.load('must.jpg'), (1280, 720))}
taust = taustapildid['Korter']

#stseeni teksti vormindus

def tekst_kõne(font : str, suurus : int, tekst : str, värv,x,y, bold : bool):
    font = pygame.font.Font(font, suurus)
    font.set_bold(bold)
    taust = (255, 255, 255)
    tekst = font.render(tekst, True, värv, taust)
    tekstRect = tekst.get_rect()
    tekstRect.center = (x,y)
    screen.blit(tekst, tekstRect)
valik1_kast = pygame.Rect(400, 170, 380, 20)
valik2_kast = pygame.Rect(492, 210, 197, 20)
hoid = False    

#põhiprogramm

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(taust, (0, 0))
    tekst_kõne('ARIALUNI.ttf', 20, valikud[praegune_stseen][0], (0, 0, 0), 550, 140, False)
    tekst_kõne('ARIALUNI.ttf', 16, valikud[praegune_stseen][1], (0, 0, 0), 590, 180, False)
    tekst_kõne('ARIALUNI.ttf', 16, valikud[praegune_stseen][4], (0, 0, 0), 590, 220, False)
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()
    klõps = pygame.mouse.get_pressed()
    if klõps[0]:
        if hoid == False:
            if valik1_kast.collidepoint(mpos):
                taust = taustapildid[valikud[praegune_stseen][3]]
                praegune_stseen = valikud[praegune_stseen][2]
            if valik2_kast.collidepoint(mpos):
                taust = taustapildid[valikud[praegune_stseen][6]]
                praegune_stseen = valikud[praegune_stseen][5]
            hoid = True
    else:
        hoid = False
    pygame.display.update()