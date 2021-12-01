"""" Игра Угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def smart_predict(number: int = 1) -> int:
    """Угадывание числа производится с помощью поискового  диапазана , величина
       которого уменьшается в 2 раза при каждой итерации. Отслеживается максимальное
       и минимальное значение диапазона. Если при очередном вычислении значение 
       предполагаемого числа выходит за рамки диапазона, то ему (предполагаемому числу) 
       присваиваетсязначение границы диапазона ,уеличенное или уменьшенное на 1. 
       Таким образом , поисковый диапазон сужается вокруг искомого числа.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = 50 #предполагаемое число
    min = 0 # минимальое значение диапазона
    max = 100 # макимальное значение  диапазона
    
    

    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        
        elif number > predict_number:  # работа с минимумом диапазона
            if predict_number <= min:
                predict_number = min + 1
                min = predict_number
            else:
                min = predict_number
                predict_number += int(predict_number/2)
                       
        else:
            if predict_number >= max:   # работа с максимумом диапазона
                predict_number = max - 1
                max = predict_number
            else: 
                max = predict_number   
                predict_number -= int(predict_number/2)
                
        if count == 200: # аварийный выход из цикла
            print (count) 
            break       
    return count



def score_game(smart_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        smart_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(smart_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)