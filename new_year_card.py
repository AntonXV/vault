from turtle import *
from random import randint


def get_color():
    """
    Функция для генерации рандомной цветовой схемы RGB
    -------------------
    Функция возвращает:
    rand_color : tuple - цифровые значения интенсивности цветов каналов R, G, B
    """
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    return rand_color


def snowflake(length, levels):
    """
    Функция для рисования фрактальной кривой Коха
    ----------
    Аргументы:
    length : int – длина отрезка
    levels : int – степень искривления прямой
    """
    if levels == 0:
        forward(length)
        return
    length /= 3
    snowflake(length, levels-1)
    left(60)
    snowflake(length, levels-1)
    right(120)
    snowflake(length, levels-1)
    left(60)
    snowflake(length, levels-1)


def draw(x=0, y=0):
    """
    Функция для рисования новогодней открытки
    ----------
    Аргументы:
    x, y : int – позиционные аргументы,
    необходимые для выполнения функции по нажатию на окно
    """
    reset()
    hideturtle()
    colormode(255)
    tracer(0)

    # Фон
    bgcolor('indigo')

    # Цепочка
    color('darkkhaki')
    pensize(15)

    penup()
    goto(0, 250)
    pendown()

    right(90)
    forward(100)

    # Крепёж цепочки
    pensize(1)

    right(90)
    back(20)

    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()

    # Шар
    color(get_color())

    penup()
    goto(0, 140)
    pendown()

    begin_fill()
    circle(250)
    end_fill()

    # Украшение зигзаг
    color(get_color())
    pensize(3)

    coords = [(176, 40), (-176, -260)]
    for e in coords:
        penup()
        goto(e)
        pendown()

        left(45)
        for i in range(5):
            forward(50)
            right(90)
            forward(50)
            left(90)
        left(135)

    # Украшение звёзды
    color(get_color())
    pensize(1)

    coords = [(-105, 80), (-105, -280)]
    for e in coords:
        penup()
        goto(e)
        pendown()

        setheading(0)
        for i in range(3):
            begin_fill()
            for i in range(5):
                forward(30)
                right(144)
            end_fill()
            penup()
            forward(90)
            pendown()

    # Украшение снежинки
    color(get_color())
    pensize(3)

    central_sf_type = randint(1, 5)
    lateral_sf_type = randint(1, 5)
    coords = [(-200, -85), (0, -110), (110, -135)]

    for i in range(3):
        penup()
        goto(coords[i])
        pendown()

        if i == 1:
            for j in range(7):
                for i in range(3):
                    snowflake(90, central_sf_type)
                    right(120)
                left(60)
        else:
            for i in range(3):
                snowflake(90, lateral_sf_type)
                right(120)

    # Надпись
    color('white')

    penup()
    goto(-310, 270)
    pendown()

    write("С НОВЫМ ГОДОМ!", font=('Arial', 50, "bold"))


def main():
    draw()
    # Возможность генерировать новый шар на открытке по нажатию на окно
    onscreenclick(draw)
    mainloop()


main()
