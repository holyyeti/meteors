import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    field = AsteroidField()

    p = Player(
        SCREEN_WIDTH / 2, 
        SCREEN_HEIGHT / 2,
        PLAYER_RADIUS
    )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('#000000')
        for member in updatable:
            member.update(dt)
        for member in drawable:
            member.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            if asteroid.is_colliding(p):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if asteroid.is_colliding(bullet):
                    asteroid.split()
                    bullet.kill()

if __name__ == '__main__':
    main()