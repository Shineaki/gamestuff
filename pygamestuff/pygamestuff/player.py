import pygame
from typing import Optional
from os.path import join

class Player(pygame.sprite.Sprite):
    def __init__(self, groups: Optional[pygame.sprite.Group]):
        super().__init__(groups)
        self.images = {
            "idle": [pygame.image.load(
                join("resources", "dungeon", "frames", f"elf_m_idle_anim_f{i}.png")).convert_alpha() for i in range(4)],
            "running": [pygame.image.load(
                join("resources", "dungeon", "frames", f"elf_m_run_anim_f{i}.png")).convert_alpha() for i in range(4)]}
        # self.images = [pygame.transform.scale(i, (i.width*2, i.height*2)) for i in self.images]
        self.image = self.images["idle"][0]
        self.rect = pygame.rect.Rect((0, 0), (16, 32))
        self.direction = pygame.Vector2(8, 8)
        self.speed = 100
        self.position = pygame.Vector2(80.0, 80.0)
        self.animation_timer = 0.0
        self.animation_idx = 0
        self.animation_state = "idle"

    def move(self, dir: pygame.Vector2):
        self.direction = dir
        if self.direction.length_squared() > 0:
            if self.animation_state != "running":
                self.animation_state = "running"
                self.animation_timer = 0.0
                self.animation_idx = 0
        else:
            if self.animation_state != "idle":
                self.animation_state = "idle"
                self.animation_timer = 0.0
                self.animation_idx = 0

    def update(self, dt: float):
        # self.rect.move()
        self.animation_timer += dt
        if self.animation_timer > 0.15:
            self.animation_timer -= 0.15
            self.animation_idx = (self.animation_idx + 1) % 4
        change = self.direction * self.speed * dt
        print(change)
        self.position += change
        self.rect.x = round(self.position.x - 8)
        self.rect.y = round(self.position.y - 16)
        self.image = self.images[self.animation_state][self.animation_idx]