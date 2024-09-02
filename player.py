from circleshape import CircleShape
from shot import Shot
import pygame
from constants import *

class Player(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        triangle = pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return triangle
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= 2
        if keys[pygame.K_d]:
            self.rotation += 2
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        pygame.Vector2(0, 1).rotate(self.rotation)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED
        
