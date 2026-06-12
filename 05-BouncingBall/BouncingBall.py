import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self, screen, x, y, speed_x, speed_y, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color
        
        
    def draw(self):
        # color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > self.screen.get_width() - self.radius:
            self.speed_x = -self.speed_x
        if self.x < self.radius:
            self.speed_x = -self.speed_x
        if self.y > self.screen.get_height() - self.radius:
            self.speed_y = -self.speed_y
        if self.y < self.radius:
            self.speed_y = -self.speed_y   
        
     
        
# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    ball1 = Ball(screen, 150, 100, 5, 5, 5, pygame.Color("yellow"))
    balls = []
    for k in range(100):
        radius = random.randint(1, 10)
        new_ball = Ball(screen, 
                    random.randint(radius, screen.get_width() - radius),
                    random.randint(radius, screen.get_height() - radius),
                    random.randint(1, 5),
                    random.randint(1, 5),
                    radius,
                    (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))    
        balls.append(new_ball)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        
        screen.fill(pygame.Color('gray'))
        ball1.draw()
        ball1.move()
        
        # for k in range(len(balls)):
        #     balls[k].move()
        #     balls[k].draw()
        
        for ball in balls:
            ball.move()
            ball.draw()
            
        # TODO: Move the ball
        # TODO: Draw the ball
        ball1.draw()
        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
