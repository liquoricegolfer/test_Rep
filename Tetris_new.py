import pygame
pygame.init()

WHITE = (255,255,255)
TURQUOISE = (64,224,208)
PINK = (0,0,254)
BLACK = (0,0,0)

display = pygame.display.set_mode ((1280,720))
pygame.display.set_caption("Tetris")

activegame= True

clock = pygame.time.Clock()

while activegame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activegame = False
            print("Quit")
            if event.key == pygame.K_RIGHT:
                print("RIGHT")
            elif event.key == pygame.K_LEFT:
                print("LEFT")
            elif event.key == pygame.K_UP:
                print("UP")
            elif event.key == pygame.K_DOWN:
                print("DOWN")
            elif event.key == pygame.K_SPACE:
                print("SPACE")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("MOUSE")

    display.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()