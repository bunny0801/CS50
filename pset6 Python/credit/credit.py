#variables
#1st sum
c1 = 0
#2nd sum
c2 = 0

while True:
    try:
        n = str(input("Number: "))
        if len(n) == 13 or len(n) == 14 or len(n) == 15 or len(n) == 16:
            break
    except ValueError:
        continue

for i in range(len(n)-2, -1, -2):
    s = int(n[i])*2
    s = s//10 + s%10
    c1 = c1 + s

for i in range(len(n)-1, -1, -2):
    c2 = c2 + int(n[i])

#total sum
c3 = c1+c2


for i in range(len(n)):
    if n[0] == "3" and (n[1] == "4" or n[1] == "7"):
        ct = "AMEX"
    elif n[0] == "5" and (n[1] == "1" or n[1] == "2" or n[1] == "3" or n[1] == "4" or n[1] == "5"):
        ct = "MASTERCARD"
    elif n[0] == "4":
        ct = "VISA"

if c3%10 != 0:
    print("INVALID")
else:
    print(ct)
