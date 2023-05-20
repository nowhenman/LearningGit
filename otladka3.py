from my_classes.FurnitureStore import *  # Господи прости

a = Door(finish='matte', price=50000, material="wood", height=1800, width=600, make="SuperDver", model="Econom",
         use="outdoors")
print(a.get_id())

b = Floor(make='ЭлитПол', model='3030A', material='ламинат', d_type="класс 33",width=300, length=1000, price=800)
print(b.get_id())

c = Window(make='Rehau', model=100572, height=1500, width=1500, price=10000, layers=2, panes=2, material='plastic')
print(c.get_id())

d = Wallpaper(make='ItalDesign', model='Floral B 1107', price=1500,
              design='Обои кремового цвета с легкой текстурированной поверхностью матовые', length=3000,
              material='флизелин', width=600)
print(d.get_id())
