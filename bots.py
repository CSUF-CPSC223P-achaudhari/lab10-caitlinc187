import json
import threading
import time

f = open('inventory.dat', 'r')
file_contents = json.load(f)
f.close()

def bot_clerk(list):
    cart = []
    robot_fetchers = [threading.Lock(),threading.Lock(),threading.Lock()]
    f_list = []

    def get_item(bot, item):
        with robot_fetchers[bot]:
            time.sleep(file_contents[item][1])
            cart.append([item, file_contents[item][0]])

    for i, id in enumerate(list):
        ff_list = threading.Thread(target=get_item, args=(i%3, id))
        f_list.append(ff_list)
        
    for f in f_list:
        f.start()

    for f in f_list:
        f.join()

    return cart

def bot_fetcher(items, cart, lock):
    f_list = []

    def get_item(bot, item):
        with lock:
            cart.append([item, file_contents[item][0]])

    for i, id in enumerate(list):
        ff_list = threading.Thread(target=get_item, args=(i%3+1, id))
        f_list.append(ff_list)

    for f in f_list:
        f.start()

    for f in f_list:
        f.join()

    return cart

