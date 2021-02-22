while True:
    start = int(input("start: "))
    if start >= 9:
        break

while True:
    end = int(input("end: "))
    if end > start:
        break

years = 0

while start < end:
    start = start + int(start/3) - int(start/4)
    years = years + 1

print(years)
