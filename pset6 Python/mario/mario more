while True:
    h = int(input("Height: "))
    if h > 0 and h < 9:
        break

for i in range(0,h):
    for j in range(0,h):
        if i + j < h-1:
            print(" ", end ="")

    for j in range(0,i+1):
        print("#", end ="")

    for j in range((h*2)+2):
        if j == ((h*2)+2)/2:
            print(" ", end ="")
        elif j == (((h*2)+2)/2)+1:
            print(" ", end ="")
    while j > (((h*2)+2)/2)+1:
        for j in range(0,i+1):
            print("#", end ="")
    print()
