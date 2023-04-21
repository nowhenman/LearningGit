#мы исходим из предположения, что пиксели квадратные
resolution = str(input('enter your screen resolution (separated with a space): '))
resolution = resolution.split()
first_resolution = int(resolution[0])
second_resolution = int(resolution[1])
ratio = first_resolution / second_resolution

screen_size = float(input('enter your screen size: '))

standard_ratio_height = first_resolution / 16 * 9
#дальше надо найти диагональ этой части (как?)

#a2 + b2 = c2
#для экрана 16:9 будет так: 337x2 = diag^2




#if ratio == (16 / 9):
    #print('16:9... classics')
#elif ratio < (16 / 9):
    #we have what I call a mac screen
    #print('you apple-loving scrum')
#else:
    #print('netflix n chill?')

#print(first_resolution, second_resolution, screen_size)
