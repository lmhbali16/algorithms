def swap(l: list, a: int, b: int) -> None:
	l[a], l[b] = l[b], l[a]

def swap2(l: list, b: int, a: int) -> None:
	l[a] = l[a]-l[b]
	l[b] = l[a] + l[b]
	l[a] = l[b] -l[a]

a = [1,24,4,46,57,4]
print(a)
swap(a, 3, 5)
print(a)

swap2(a, 4, 2)
print(a)