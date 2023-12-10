def nextTo(setOfParens):
	newSet = set()

	for item in setOfParens:
		newSet.add(item+"()")
		newSet.add("()"+item)

	return newSet

def wrap(setOfParens):
	newSet = set()

	for item in setOfParens:
		newSet.add("("+item+")")

	return newSet


def parents(n):
	if n == 1:
		return {"()"}

	else:
		nextToSet = nextTo(parents(n-1))
		wrapSet = wrap(parents(n-1))

		wrapSet.update(nextToSet)

		return wrapSet

print(parents(3))