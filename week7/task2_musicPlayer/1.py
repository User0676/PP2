import pygame,os

size = 800
musics = []
pygame.init()
screen = pygame.display.set_mode([size,size])
clock = pygame.time.Clock()
player_icon = pygame.transform.scale(pygame.image.load('img\\player_mp3.jpg'), (800,800))
paused = True
left = right = mid = False
current = 0
for i in os.listdir("C:\\Users\\atakt\\Desktop\\PP2\\week7\\player\\playlist"):
    music = pygame.mixer.Sound("C:\\Users\\atakt\\Desktop\\PP2\\week7\\player\\playlist\\" + str(i))
    musics.append(music)

while True:
    key = pygame.key.get_pressed()


    if key[pygame.K_UP]:
        musics[current].play()
        paused = False

    if key[pygame.K_DOWN]:
        if paused == True:
            pygame.mixer.unpause()
            paused = False
        elif paused == False:
            pygame.mixer.pause()
            paused = True

    if key[pygame.K_RIGHT]:
        musics[current].stop()
        current += 1
        if current == len(musics) :
            current = 0
        musics[current].play()

    if key[pygame.K_LEFT]:
        musics[current].stop()
        current -= 1
        if current <= -1:
            current = len(musics) - 1
        musics[current].play()


    screen.blit(player_icon, (0,0))


    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


pygame.quit()