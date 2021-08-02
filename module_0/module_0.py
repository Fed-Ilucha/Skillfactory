import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток
       результат = 101 попытка'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return count # выход из цикла, если угадали
        
        
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       результат = 33 попытки
       к сожалению при падает с ошибкой кадый раз на числе 76, хотя одиночный вызов с числом 76 работает корректно'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали   


def game_core_v3(number):
    '''на первом шаге предполагаемый диапазон 0-100, а предположение - середина диапазона.
       Далее пока не угадаем, на основе ответа больше или меньше, на каждом шагу уменьшаем предполагаемый диапазон вдвое,
       а предположение на каждом шаге это середина нового диапазона
       результат = 5 попыток'''
    bounds =[1,101]
    predict = (bounds[0]+bounds[1])//2
    count = 1
    while predict !=number :
        count+=1
        if number > predict: 
            bounds = [predict,bounds[1]] 
        elif number < predict: 
            bounds = [bounds[0],predict]
        predict = (bounds[0]+bounds[1])//2  
        #print(f"попытка {count}")
        #print(f"границы {bounds}")    
        #print(f"предположение {predict}")
    return(count) # выход из цикла, если угадали   
 
def game_core_v4(number):  
    '''реализуем то же самое с помощью рекурсии, будет красивее 
      почему то при вызове в score_game падает каждый раз при попытке угадать 76, просто вызов game_core_v4(76) 
      работает корректно'''
   
    def recursion(number, count, bounds):
        predict = (bounds[0]+bounds[1])//2
        #print(f"попытка {count}")
        #print(f"границы {bounds}")    
        #print(f"предположение {predict}")
        #print(f"искомое {number}")
        if number == predict:
            return count
        elif number > predict:
            recursion(number, count+1, [predict, bounds[1]] )
        elif number < predict:
            recursion(number, count+1, [bounds[0], predict])
        
        
    return recursion(number, 1, [1,101])

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)
score_game(game_core_v4)

game_core_v4(76)