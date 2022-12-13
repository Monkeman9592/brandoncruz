from sense_hat import SenseHat
import time
import random

def main():  
    name = str(input("Enter name: "))
    



    senseHat = SenseHat()
    senseHat.low_light = True

    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    START_DELAY = 3
    MIN_VALUE = 0
    MAX_VALUE = 7
    SIZE = 8

    while True:
        # variables:
        gameOver = False
        growSnake = False
        generateRandomFood = False
        snakeMovementDelay = 0.5
        snakeMovementDelayDecrease = -0.02
        scorecount = 0 

        # start delay:
        time.sleep(START_DELAY)

        # set default snake starting position (values are chosen by preference):
        PosX = [3]
        PosY = [6]
        scorecount = [1]

        # generate random food position:
        while True:
            foodPosX = random.randint(0, 7)
            foodPosY = random.randint(0, 7)
            if foodPosX != PosX[0] or foodPosY != PosY[0]:
                break

        # set default snake starting direction (values are chosen by preference):
        movementX = 0
        movementY = -1

      
        while not gameOver:
            ## snake eats food:
            if  foodPosX == PosX[0] and foodPosY == PosY[0]:
                growSnake = True
                generateRandomFood = True
                snakeMovementDelay += snakeMovementDelayDecrease
            
            

            ## if snake bites itself:
            for i in range(1, len(PosX)):
                if PosX[i] == PosX[0] and PosY[i] == PosY[0]:
                    gameOver = True

            # game-over:
            if gameOver:
                break

            # joystick :
            events = senseHat.stick.get_events()
            for event in events:
                if event.direction == "left" and movementX != 1:
                    movementX = -1
                    movementY = 0
                elif event.direction == "right" and movementX != -1:
                    movementX = 1
                    movementY = 0
                elif event.direction == "up" and movementY != 1:
                    movementY = -1
                    movementX = 0
                elif event.direction == "down" and movementY != -1:
                    movementY = 1
                    movementX = 0

            # grow snake:
            if growSnake:
                growSnake = False
                PosX.append(0)
                PosY.append(0)
                scorecount.append(1)

            # move snake:
            for i in range((len(PosX) - 1), 0, -1):
                PosX[i] = PosX[i - 1]
                PosY[i] = PosY[i - 1]

            PosX[0] += movementX
            PosY[0] += movementY

            # check game borders:
            if PosX[0] > MAX_VALUE:
                PosX[0] -= SIZE
            elif PosX[0] < MIN_VALUE:
                PosX[0] += SIZE
            if PosY[0] > MAX_VALUE:
                PosY[0] -= SIZE
            elif PosY[0] < MIN_VALUE:
                PosY[0] += SIZE

            # spawn random food:
            if generateRandomFoodFlag:
                generateRandomFoodFlag = False
                retryFlag = True
                while retryFlag:
                    foodPosX = random.randint(0, 7)
                    foodPosY = random.randint(0, 7)
                    retryFlag = False
                    for x, y in zip(PosX, PosY):
                        if x == foodPosX and y == foodPosY:
                            retryFlag = True
                            break

            # update matrix:
            senseHat.clear()
            senseHat.set_pixel(foodPosX, foodPosY, RED)
            for x, y in zip(PosX, PosY):
                senseHat.set_pixel(x, y, GREEN)

            # snake speed (game loop delay):
            time.sleep(snakeMovementDelay)
main()