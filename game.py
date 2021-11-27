""" угадай число"""

import numpy as np
number = np.random.randint(1,101)# загадываем число
count = 0

while True:
      
    count += 1
    predict_number = int(input('угадай число от 1 до 100' ) )
    if predict_number > number:
        print('число должно быть меньше')
    elif predict_number < number:
        print('число должно быть больше')  
    else:
        print(f'вы угадали число {number}  за {count}  попыток')
        break
                             
         
