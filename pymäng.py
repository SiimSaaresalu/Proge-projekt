import pygame

pygame.init()

# see osa võtab tekstifailist teksti ja paneb info sõnastikku 

f = open("lizetekst.txt", encoding="utf-8")
read = f.readlines()
f.close()
valikud = dict()
for rida in read:
    reasisu = rida.strip().split("/")
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
                'Gen-sees2': pygame.transform.scale(pygame.image.load('gen sees2.jpg'), (1280, 720))}
taust = taustapildid['Korter']

#tegelane

def player(x, y):
    screen.blit(tegelaneImg, (x, y))

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
<<<<<<< Updated upstream
<<<<<<< Updated upstream
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
                print(valikud[praegune_stseen][1])
                taust = taustapildid[valikud[praegune_stseen][3]]
                praegune_stseen = valikud[praegune_stseen][2]
            if valik2_kast.collidepoint(mpos):
                print(valikud[praegune_stseen][4])
                taust = taustapildid[valikud[praegune_stseen][6]]
                praegune_stseen = valikud[praegune_stseen][5]
            hoid = True
    else:
        hoid = False
    pygame.display.update()
=======
=======
    if taust == taustapildid['Gen-sees2'] or taust == taustapildid["Gen-ees"] or taust == taustapildid["Gen-sees1"]:
        if not mixer.music.get_busy():
            mixer.init()
            mixer.music.load('Toto-Africa-_Official-HD-Video_.ogg')
            mixer.music.set_volume(0.5)
            mixer.music.play(start=140)
    elif taust == taustapildid["Trepp-esik"] or taust == taustapildid["Trepp-põhi"]:
        if not mixer.music.get_busy():
            mixer.init()
            mixer.music.load("The-Proclaimers-I_m-Gonna-Be-_500-Miles_-_Official-Music-Video_.ogg")
            mixer.music.set_volume(0.5)
            mixer.music.play()
    elif praegune_stseen not in {'TREPP-VEIN', 'TREPP-MIDAGI', 'GEN-VEIN', 'GEN-MIDAGI'} and mixer.music.get_busy():
        mixer.music.stop()
>>>>>>> Stashed changes
    if praegune_stseen in {'AAR-LÕPP','KAINE-LÕPP','EKSMAT-LÕPP','MÄNG-LÕPP','BLACKOUT-LÕPP'}:
        tekst_kõne('ARIALUNI.ttf', 20, valikud[praegune_stseen], (0, 0, 0), 550, 140, False)
#         tekst_kõne('ARIALUNI.ttf', 16, "Alusta mängu uuesti", (0, 0, 0), 590, 180, False)
        tekst_kõne('ARIALUNI.ttf', 16, "Sulge mäng", (0, 0, 0), 590, 220, False)
        mpos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
        klõps = pygame.mouse.get_pressed()
        if klõps[0]:
#             if hoid == False:
#                 if valik1_kast.collidepoint(mpos):
#                     taust = "Korter"
#                     praegune_stseen = "ALGUS"
                if valik2_kast.collidepoint(mpos):
                    pygame.quit()
                    quit()
                hoid = True
        else:
            hoid = False
    if praegune_stseen not in {'AAR-LÕPP','KAINE-LÕPP','EKSMAT-LÕPP','MÄNG-LÕPP','BLACKOUT-LÕPP'}:
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
>>>>>>> Stashed changes
