class Box:

	def __init__(self, width, height, depth):
		self.w = width
		self.h = height
		self.d = depth


def is_larger(box1, box2):
	# floating point comparison should be done differently
	if box1.h > box2.h and box1.d > box2.d:
		return True

	return False

def calculate_stack(list_of_boxes, box, height):
	for i in range(len(list_of_boxes)):
		if is_larger(box, list_of_boxes[i]):
			if i == len(list_of_boxes) - 1:
				return height + list_of_boxes[i].h
			else:
				return calculate_stack(list_of_boxes[i+1:], list_of_boxes[i], height+list_of_boxes[i].h)

	return height

def sort_by_width(list_of_boxes):
	if len(list_of_boxes) == 1:
		return list_of_boxes

	mid = len(list_of_boxes) // 2

	left_part = sort_by_width(list_of_boxes[:mid])
	right_part = sort_by_width(list_of_boxes[mid:])


	i = 0
	j = 0

	result = []

	while i < len(left_part) and j < len(right_part):
		if left_part[i].w >= right_part[j].w:
			result.append(left_part[i])
			i += 1

		else:
			result.append(right_part[j])
			j += 1

	while i < len(left_part):
		result.append(left_part[i])
		i += 1

	while j < len(right_part):
		result.append(right_part[j])
		j += 1

	return result



def get_height(list_of_boxes: list) -> float:
	sorted_boxes = sort_by_width(list_of_boxes)

	result = -1

	for i in range(len(sorted_boxes)):
		if i == len(sorted_boxes) - 1:
			if result < sorted_boxes[i].h:
				return sorted_boxes[i].h
			else:
				return result

		a = calculate_stack(sorted_boxes[i+1:], sorted_boxes[i], sorted_boxes[i].h)
		if a > result:
			result = a

	return result


boxes = [Box(4, 5, 6), Box(5, 3, 1), Box(7, 5, 9), Box(14, 25, 46), Box(7, 9, 10), Box(3, 4, 8), Box(1, 3, 3)]

sorted_boxes = get_height(boxes)

print(sorted_boxes)






def create_stack(list_of_boxes, box, idx, stackMap):
	if idx >= len(list_of_boxes):
		return 0

	bottom = list_of_boxes[idx]

	height = 0

	if box is None or is_larger(box, bottom):
		if stackMap[idx] == 0:
			stackMap[idx] = create_stack(list_of_boxes, bottom, idx+1, stackMap)
			stackMap[idx] += bottom.h

		height = stackMap[idx]

	height_without = create_stack(list_of_boxes, box, idx+1, stackMap)

	return max(height, height_without)

def get_height2(list_of_boxes):
	return create_stack(list_of_boxes, None, 0, [0] * len(list_of_boxes))

print(get_height2(boxes))


	