import matplotlib.pyplot as plt
from randwalk import RandomWalk


while True:
    print()
    keep_runing = input('Make another walk? (y/n): ')
    if keep_runing == 'n':
        break

    '''Побудова випадкового блукання і нанесення точок на діаграму'''
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, c='red', s=2)
    plt.show()
