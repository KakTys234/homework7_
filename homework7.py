# 1) Создаем список из 5 машин

cars = ["BMW", "MB", "LADA", "KIA", "HONDA"]

# 2) Создаем цикл for и выводим автомобили с надписью 'Я езжу на автомобиле марки'
# 3) Создаем целочисленную переменную cars_count = 0

cars_count = 0
for i in range(len(cars)):
    print('Я езжу на автомобиле марки', cars[i])

# 4) Увеличиваем переменную на 10
    
    cars_count += 10
    print(cars_count)

