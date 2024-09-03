from circleshape import CircleShape
from constants import *
import pygame, random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        circle = pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return circle

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            smaller_asteroid_1_velocity = self.velocity.rotate(random_angle)
            smaller_asteroid_2_velocity = self.velocity.rotate(-random_angle)
            smaller_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            smaller_asteroid_1 = Asteroid(self.position[0], self.position[1], smaller_asteroid_radius)
            smaller_asteroid_2 = Asteroid(self.position[0], self.position[1], smaller_asteroid_radius)
            smaller_asteroid_1.velocity = smaller_asteroid_1_velocity * 1.2
            smaller_asteroid_2.velocity = smaller_asteroid_2_velocity * 1.2