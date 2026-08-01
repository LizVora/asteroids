import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        

        CircleShape(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS or self.radius == ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            astro_move1 = pygame.Vector2.rotate(self.velocity, angle)
            astro_move2 = pygame.Vector2.rotate(self.velocity, angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            astroid1.velocity = astro_move1
            astroid2.velocity = astro_move2
            astroid1.velocity *= 1.2
            astroid2.velocity *= 1.2
