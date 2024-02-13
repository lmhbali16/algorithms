def change_color(paint, original_colour, color, position):
	if len(paint) <= position[1] or position[1] < 0:
		return
	elif len(paint[0]) <= position[0] or position[0] < 0:
		return

	current_colour = paint[position[1]][position[0]]

	if current_colour == original_colour:
		paint[position[1]][position[0]] = color

		change_color(paint, original_colour, color, (position[0] + 1, position[1]))
		change_color(paint, original_colour, color, (position[0] - 1, position[1]))
		change_color(paint, original_colour, color, (position[0], position[1] + 1))
		change_color(paint, original_colour, color, (position[0], position[1] -1))



def pain_fill(paint, point, color):
	if len(paint) <= point[1] or point[1] < 0:
		return
	elif len(paint[0]) <= point[0] or point[0] < 0:
		return
	elif len(paint) == 0:
		return

	original_colour = paint[point[1]][point[0]]


	change_color(paint, original_colour, color, point)

paint = [[1,2,3,21,21,21,4,5,34,3,2], [1,2,4,5,21,21,21,5,3, 4,6], [2,3,4,2,3,21,21,21,21,4,2], [2,3,4,2,3,21,21,21,21,4,2]]

pain_fill(paint, (6, 1), 100)

for i in paint:
	print(i)