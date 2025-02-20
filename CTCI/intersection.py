class Point:

	def __init__(self, x: float, y: float) -> None:
		self.x = x
		self.y = y


	def getX(self) -> float:
		return self.x

	def getY(self) -> float:
		return self.y

class Line:

	def __init__(self, start: Point, end: Point):
		self.start = start
		self.end = end


		deltaY = self.end.getY() - self.start.getY()
		deltaX = self.end.getX() - self.start.getX()

		self.slope = deltaY / deltaX
		self.yintercept = self.end.getY() - slope * self.end.getX()


	def getSlope(self) -> float:
		return self.slope

	def getYIntercept(self) -> float:
		return self.yintercept

def inBetween(start: float, mid: float, end: float) -> bool:
	if start > end:
		return end <= middle and middle <= start
	else:
		return start <= middle and middle <= end


def isPointInBetween(start1: Point, start2: Point, end1: Point) -> bool:
	return inBetween(start1.getX(), start2.getX(), end1.getX()) and inBetween(start1.getY(), start2.getY(), end1.getY())

def intersect(start1: Point, end1: Point, start2: Point, end2: Point) -> Point:
	if start1.getX() > end1.getX():
		a = start1
		start1 = end1
		end1 = a

	if start2.getX() > end2.getX():
		a = start2
		start2 = end2
		end1 = a

	if start1.getX() > start2.getX():
		a = start1
		start1 = start2
		start2 = a

		b = end1
		end1 = end2
		end2 = b

	line1 = Line(start1, end1)
	line2 = Line(start2, end2)

	if line1.getSlope() == line2.getSlope():
		if line1.getYIntercept() == line2.getYIntercept() and isPointInBetween(start1, start2, end1):
			return start2

		return None

	x = (line2.getYIntercept() - line1.getYIntercept()) / (line1.getSlope() - line2.getSlope())
	y = x * line1.getSlope() + line1.getYIntercept()
	intersection = Point(x, y)


	if isPointInBetween(start1, intersection, end1) and isPointInBetween(start2, intersection, end2):
		return intersection

	return None


start1 = Point(2, 4)
end1 = Point(2, 10)
start2 = Point(2, 4)
end2 = Point(2, 10)

print(intersect(start1 , end1, start2, end2))










