import pygame
pygame.init()

WHITE = (255,255,255)
TURQUOISE = (64,224,208)
PINK (0,0,254)
BLACK = (0,0,0)

display = pygame.display.set_mode ((1280,720))
pygame.display.set_caption("Tetris")

spielaktiv = True

clock = pygame.time.Clock()

while spielaktiv:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hat Maus angeklickt")

    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

