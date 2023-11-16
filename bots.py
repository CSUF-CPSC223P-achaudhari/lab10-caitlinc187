import json
import threading
import time

f = open('inventory.dat', 'r')
file_contents = json.load(f)

def bot_clerk(list):
    cart = []
    lock = threading.Lock()
    robot_fetchers = [[],[],[]]
    f_list = []

    for i in range(len(list)):
        robot_fetchers[i%3].append([list[i], file_contents[list[i]][0], file_contents[list[i]][1]])
    for lists in robot_fetchers:
        ff_list = threading.Thread(target=bot_fetcher, args=(lists, cart, lock))
        f_list.append(ff_list)
        ff_list.start()
    for ff_list in f_list:
        ff_list.join()

    return cart

def bot_fetcher(items, cart, lock):
    for i in items:
        time.sleep(file_contents[i][1])
        with lock:
            cart.append([i, file_contents[i][0]])

