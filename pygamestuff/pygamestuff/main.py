import pygame
from pygamestuff.player import Player


def handle_input(player: Player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    keys = pygame.key.get_pressed()
    player_movement_direction = pygame.Vector2(0.0, 0.0)
    if keys[pygame.K_d]:
        player_movement_direction.x += 1.0
    if keys[pygame.K_a]:
        player_movement_direction.x -= 1.0
    if keys[pygame.K_s]:
        player_movement_direction.y += 1.0
    if keys[pygame.K_w]:
        player_movement_direction.y -= 1.0
    if player_movement_direction.length_squared() > 0:
        player_movement_direction = player_movement_direction.normalize()
    player.move(player_movement_direction)
    return True


if __name__ == "__main__":
    pygame.init()
    screen_size = pygame.Vector2(640, 360)
    screen = pygame.display.set_mode(
        screen_size#, flags=pygame.SCALED, vsync=1 #| pygame.FULLSCREEN, vsync=1
    )
    print("Hello")
    player_group = pygame.sprite.Group()
    player = Player(player_group)
    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(60) / 1000
        running = handle_input(player)

        # draw_surf = pygame.Surface(screen_size, pygame.SRCALPHA)

        screen.fill((50, 50, 50))
        player_group.update(dt)
        # camera_position = pygame.Vector2(
        #     screen.width / 2 - player.rect.x,
        #     screen.height / 2 - player.rect.y,
        # )
        # screen.blit(draw_surf, camera_position)
        # screen.blit(player.image, (screen.width / 2, screen.height / 2))
        screen.blit(player.image, player.rect)
        pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
        pygame.display.flip()

    pygame.quit()
