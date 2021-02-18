start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(start_list, )
start_list[1] = '05'
start_list.insert(1, '"')
start_list.insert(3, '"')
start_list.insert(5, '"')
start_list.insert(7, '"')
start_list[12] = '+05'
start_list.insert(12, '"')
start_list.insert(14, '"')
print(start_list)

hole_string = ''
for idx in range(len(start_list)):
    if idx == 1 or idx == 2 or idx == 5 or idx == 6 or idx == 12 or idx == 13:
        hole_string += start_list[idx] + ''
    else:
        hole_string += start_list[idx] + ' '
print(hole_string)
