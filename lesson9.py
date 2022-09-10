import threading
import time


def item_number():
    numbers = [_ for _ in range(1, 11)]
    numbers.reverse()
    for item in numbers:
        print(f'Поток: {threading.current_thread()}, Значение: {item} \n')
        time.sleep(1)


for i in range(2):

    t1 = threading.Thread(target=item_number)
    t2 = threading.Thread(target=item_number)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

