import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from shot import *
def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers=(shots,updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    player.cd = 0

    
    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        dt = (clock.tick(60)/1000)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                #print("Game over!")
                raise SystemExit("Game over!")
            for shot in shots:
                if shot.collision_check(asteroid):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()

if __name__ == "__main__":
    main()