import pygame
import random
#pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKE!!!")
clock = pygame.time.Clock()
blockSize = 25
apple = pygame.image.load



class Snake:
    def __init__(self):
        self.x, self.y = blockSize, blockSize
        self.xdirection = 1
        self.ydirection = 0
        self.head = pygame.Rect(self.x,self.y, blockSize, blockSize)
        self.body = [pygame.Rect(self.x-blockSize,self.y, blockSize, blockSize)]
        self.dead = False
    def update(self):
        for square in self.body:
            #if self.head.x == square.x and self.head.y == square.y:
                #self.dead = True
            if self.head.x not in range(0,500) or self.head.y not in range(0,500):
                self.dead = True
            #if square.x not in range(0,500) or square.y not in range(0,500):
                #self.dead = True

        if self.dead == True:
            #self.x, self.y = blockSize, blockSize
            #self.xdirection = 1
            #self.ydirection = 0
            pygame.quit()
        

        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y

        self.head.x += self.xdirection * blockSize
        self.head.y += self.ydirection * blockSize
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0,500)/blockSize) * blockSize
        self.y = int(random.randint(0,500)/blockSize) * blockSize
        self.rect = pygame.Rect(self.x,self.y, blockSize, blockSize)
    def update(self):
        pygame.draw.rect(screen, "red", self.rect)
    def newLocation(self):
        self.x = int(random.randint(0,500)/blockSize) * blockSize
        self.y = int(random.randint(0,500)/blockSize) * blockSize
        self.rect = pygame.Rect(self.x,self.y, blockSize, blockSize)

    
def drawGrid():
    screen.fill((144,238,144))
    for x in range(0,500, blockSize):
        for y in range(0,500, blockSize):
            rectangle = pygame.Rect(x,y,blockSize,blockSize)
            pygame.draw.rect(screen, (51, 153, 102), rectangle,1)

drawGrid()

snake = Snake()
apple = Apple()
def main():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.ydirection = 1
                    snake.xdirection = 0
                if event.key == pygame.K_UP:
                    snake.ydirection = -1
                    snake.xdirection = 0
                if event.key == pygame.K_RIGHT:
                    snake.ydirection = 0
                    snake.xdirection = 1
                if event.key == pygame.K_LEFT:
                    snake.ydirection = 0
                    snake.xdirection = -1
        
        snake.update()#updating size of snake body 

        screen.fill("black")
        drawGrid()#building the game again after updating snake so the body does not remain on grid
        
        apple.update()

        pygame.draw.rect(screen, (0,0,149), snake.head)

        for square in snake.body:
           pygame.draw.rect(screen, (0,0,149), square)

        if snake.head.x == apple.x and snake.head.y == apple.y:
            snake.body.append(pygame.Rect(snake.head.x, snake.head.y, blockSize, blockSize))
            apple.newLocation()


        pygame.display.update()
        clock.tick(10)

if __name__ == "__main__":
    main()
