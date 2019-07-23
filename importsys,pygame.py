import pygame
#from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (50, 100, 100)

fish_image = pygame.image.load("saver.png")
fish_image = pygame.transform.smoothscale(fish_image,(200,100))

fish_rect = fish_image.get_rect()

fish_rect.center = (width/2, height/2)
speed = pygame.math.Vector2(10,10)

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
        clock.tick(60)
        screen.fill (color)
        screen.blit(fish_image, fish_rect)
        pygame.display.flip()
        movefish()

if __name__ == "__main__":
    main()