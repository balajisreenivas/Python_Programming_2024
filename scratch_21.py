marks = [30,40,50]

marks.append(70)

print(len(marks))

print(sum(marks))

print(max(marks))

print(min(marks))

marks.insert(2,60)

print(marks[:5])

print(marks.index(50))

for mark in marks:
    print(mark)
