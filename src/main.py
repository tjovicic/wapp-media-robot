import pyautogui, time, os.path

pyautogui.FAILSAFE = True

positions = []

def executeSteps():
    secsToWait = 2

    for position in positions:
        pyautogui.click(position)
        time.sleep(secsToWait)

def countdown(n):
    for i in range(n):
        print(f'{n-i}')
        time.sleep(1)

def recordSteps(numbOfSteps):
    for i in range(numbOfSteps):
        print(f'Set pointer to step {i+1}. You have 5 seconds after you press Enter')
        input()
        time.sleep(5)

        position = pyautogui.position()
        positions.append(position)
        pyautogui.click(position)

print('How many steps do you need?')
recordSteps(int(input()))

print('Was this OK? y/n')
response = input()

if response == 'y':
    print('Do you want to stop on a desired number of downloads or when we recognize the last picture: a/b')
    response = input()

    if response == 'a': 
        print('Input desired number of downloads:')
        n = int(input())

        print('We start in')
        countdown(5)

        for i in range(n):
            executeSteps()
    else:
        print('Input path to the png image on which you want to stop automating:')
        path = input()

        if not (os.path.isfile(path) and path.endswith('.png')):
            print('It is not a valid path')
            exit()

        print('We start in')
        countdown(5)

        isLast = (pyautogui.locateOnScreen(path) != None)
        while (not isLast):
            executeSteps()
            isLast = (pyautogui.locateOnScreen(path) != None)
        
