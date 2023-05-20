from my_classes.FurnitureStore import *  # Господи прости

a = Door(finish='matte', price=50000, material="wood", height=1800, width=600, make="SuperDver", model="Econom",
         use="outdoors")
print(a.get_id())

b = Floor(make='ЭлитПол', model='3030A', material='ламинат', d_type="класс 33",width=300, length=1000, price=800)
print(b.get_id())
