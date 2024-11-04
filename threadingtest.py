import threading, time
run = True

def worker():
    counter = 0
    while run:
        time.sleep(0.5)
        counter += 1
        print(f'{counter}')
        
def worker2():
    counter = 0
    while run:
        time.sleep(0.25)
        counter += 1
        print(f'{counter}')

threading.Thread(target=worker).start()
threading.Thread(target=worker2).start()

input("Press enter to quit\n")
run = False