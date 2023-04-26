class Student1():
    full_name = 'John Doe'
    uni = 'sharaga'
    points = -9999


maga = Student1()
maga.full_name = 'Иван Михайлович Краснов'
maga.uni = 'МФТИ'
maga.points = 315

goga = Student1()
goga.full_name = "Лев Исаакович Эйдельман"
goga.uni = 'имени Баумана'
goga.points = 352

vaha = Student1()
vaha.full_name = 'Вахид Рамзанович Дудаев'
vaha.uni = 'МГУ'
vaha.points = 400

the_youth = [maga, goga, vaha]
rockstars = True
all_points = 0
for i in the_youth:
    if i.points < 20:
        rockstars = False
    all_points += i.points
print(rockstars, all_points)