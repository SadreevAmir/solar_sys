# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """
    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """
    #print(line)
    param = list(line.split())
    star.R = float(param[1])
    star.color = param[2]
    star.m = float(param[3])
    star.x = float(param[4])
    star.y = float(param[5])
    star.Vx = float(param[6])
    star.Vy = float(param[7])
    #print(param)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.

    **planet** — объект планеты.
    """
    #print(line)
    param = list(line.split())
    planet.R = float(param[1])
    planet.color = param[2]
    planet.m = float(param[3])
    planet.x = float(param[4])
    planet.y = float(param[5])
    planet.Vx = float(param[6])
    planet.Vy = float(param[7])
    #print(param)


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    print('write_space_objects_data_to_file')
    with open(output_filename, 'a') as out_file:
        for a in space_objects:
            if a.obj.type == 'star':
                line = 'Star'
            if a.obj.type == 'planet':
                line = 'Planet'
            line = line + ' ' + str(a.obj.R) + ' ' + a.obj.color + ' ' + str(a.obj.m) + ' ' + str(a.obj.x) + ' ' +\
                   str(a.obj.y) + ' ' + str(a.obj.Vx) + ' ' + str(a.obj.Vy)
            print(1)
            out_file.write(line)
            out_file.write("\n")



if __name__ == "__main__":
    print("This module is not for direct call!")
