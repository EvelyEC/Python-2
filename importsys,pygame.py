import pygame
#from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (50, 100, 100)


fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image,(200,100))

fish_rect = fish_image.get_rect()

fish_rect.center = (width/2, height/2)
speed = pygame.math.Vector2(0,0)

def movefish():
    global fish_image
    fish_rect.move_ip(speed)
    if fish_rect.top < 0 or fish_rect.bottom > height:
        speed [1] *=-1

        fish_image = pygame.transform.flip(fish_image, True,False)

    if fish_rect.left < 0 or fish_rect.right > width:
        speed [0] *=-1
        fish_image = pygame.transform.flip(fish_image, True,False)





def main():
    while True:
        global color
        clock.tick(60)
        screen.fill(color)
        screen.blit(fish_image, fish_rect)
        pygame.display.flip()
        movefish()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
                #main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                color = (255, 0, 0)
                speed[0] += -1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                speed[0] += 1
            if event.key == pygame.K_UP or event.key == ord('w'):
                speed [1] += -1
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                speed [1] += 1
            if event.key == pygame.K_SPACE:
                speed [1] += -1
            if event.key == event.key == ord('q'):
                speed [1] += -1
                speed [0] += -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                speed[0] = 0
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                speed[0] = 0
            if event.key == pygame.K_UP or event.key == ord('w'):
                speed [1] = 0
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                speed [1] = 0
            if event.key == pygame.K_SPACE:
                speed [1] += 1
            if event.key == ord('q'):
                speed[1] = 0
                speed[0] = 0
#                pygame.quit()
#                sys.exit()
                #main = False


if __name__ == "__main__":
    main()