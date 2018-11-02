import json

#Словарь, где будет ключ=предмет и значение=средний балл по нему всего класса
d = {}
#Словарь, где будет ключ=ученик и значение=средний балл по всем предметам
pers = {}
#k1=счётчик учеников, k2=счётчик количества предметов
k1, k2 = 0, 0
data = ''

try:
    with open('class.json', 'r') as f:                                #Берём исходные данные
        data = json.loads(f.read())

    for name in data:
        k1 += 1
        k2 = 0
        for pred in data[name]:
            k2 += 1
            pers[name] = pers.get(name, 0) + int(data[name][pred])    #Считаем общее количество баллов по каждому ученику
            d[pred] = d.get(pred, 0) + int(data[name][pred])          #Считаем общее количество баллов по каждому предмету
        pers[name] = pers[name] / k2                                  #Считаем средний балл по каждому ученику

    for key, val in d.items():                                        #Считаем средний балл по каждому предмету
        d[key] = d[key] / k1

    with open('about_class.json', 'w') as f:                          #Записываем в файл Json данные по среднему баллу по предметами
        json.dump(d, f)

    with open('about_pupils.txt', 'w') as f:                          #Записываем в файл txt данные по среднему баллу по ученикам
        for name in pers.keys():
            f.write('У ученика {} средний балл по всем предметам: {} '.format(name, pers[name]))

            #Добавляем итог об успеваемости каждого ученика
            if pers[name] >= 4.5:
                f.write('- Хорошая успеваемость.\n')
            elif 3.5 <= pers[name] < 4.5 :
                f.write('- Средняя успеваемость.\n')
            else:
                f.write('- Плохая успеваемость.\n')

except Exception as ex:
    print('Что-то не так с файлом!')