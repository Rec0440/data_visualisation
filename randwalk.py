from random import choice


class RandomWalk():
    '''Клас для генерування випадкових блукань'''

    def __init__(self, num_point=5000):
        '''Ініціалізує атрибути блукання'''
        self.num_point = num_point

        '''Всі блукання починаються з точки 0, 0'''
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Обчислює всі точки блукання'''

        '''Кроки генеруються до досягнення потрібної глибини'''
        while len(self.x_values) < self.num_point:
            '''Визначає напрямок і довжину кроків'''
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            '''Відкидання нульових переміщень'''
            if x_step == 0 and y_step == 0:
                continue

            '''Обрахування наступних значень x i y'''
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
