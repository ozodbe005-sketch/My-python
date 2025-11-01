# # # Input Function
import turtle
name = "Ozodbek"  # foydalanuvchi nomi va uning uzunligini hisoblash
length = len(name)
print(length)
print(len(input("What's your name?")))
username = input("What is your name? ")
length = len(username)
print(length)

Data Types in Python
len("Hello")
# print(len("Hello"))
# Output:4                           #  bularni hammasi string float integer boolean ga misollar

# Subscripting
print("Hello" [0])


# String
print("123"+"456")
# Output 123456

# Integer=Whole number
print(123+456)
# Output:579

# Large Integers (we use commas or underscores)
print("123,456,789")

# Float=Floating Point Number
print(3.4567)

# boolean
print(True)
print(False)

tip_calculator.py
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

rollercoaster.py
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

Arithmetic Operations
a = 10
b = 3
print(a + b)   # qo‘shish
print(a - b)   # ayirish
print(a * b)   # ko‘paytirish
print(a / b)   # bo‘lish (natija float)
print(a // b)  # butun bo‘lish
print(a % b)   # qoldiq
print(a ** b)  # daraja

# Nested Loops
for i in range(3):
    for j in range(2):
        print(i, j)


# Turtle Graphics

t = turtle.Turtle()

for i in range(4):
    t.forward(100)  # 100 px oldinga yur
    t.right(90)     # 90° o‘ngga buril

turtle.done()


# Heart Shape with Turtle Graphics

t = turtle.Turtle()
t.color("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.left(120)
t.circle(-90, 200)
t.forward(180)

t.end_fill()
t.hideturtle()
turtle.done()

# Star Shape with Turtle Graphics

t = turtle.Turtle()

for i in range(5):
    t.forward(100)
    t.right(144)

turtle.done()

# Colorful Pattern with Turtle Graphics
colors = ["red", "purple", "blue", "green", "orange", "yellow"]

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

for i in range(360):
    t.color(colors[i % 6])
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(61)

turtle.done()


# Rainbow Circle Pattern with Turtle Graphics


# pushtirang doira naqshi bilan

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("magenta")

for i in range(72):
    t.circle(100)
    t.right(5)

t.penup()
t.goto(0, -50)
t.pendown()
t.pencolor("yellow")

for i in range(36):
    t.forward(200)
    t.backward(200)
    t.right(10)

t.hideturtle()
turtle.done()


# Xatolar bilan ishlash


yosh = int(input("Yoshingiz nechida?"))

if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


# Juft sonni tekshirish dasturi
son = float(input("Juft son kiriting: "))
if son % 2 != 0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

# Chipta narhini hisoblash dasturi
yosh = int(input("Yoshingiz nechida?"))

if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x}={y}")
elif x < y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


# Mahsulotlar mavjudligini tekshirish dasturi
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
    print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# Foydalanuvchidan son olib, uning tub yoki tub emasligini aniqlash dasturi
son = int(input("Istalgan butun sonni kiriting: "))
tub = True  # dastlab tub deb hisoblaymiz
if son < 2:
    tub = False  # 2 dan kichik sonlar tub emas
else:
    for n in range(2, son):
        if son % n == 0:
            tub = False  # agar biror songa qoldiqsiz bo'linsa, tub emas
            break
if tub:
    print(f"{son} tub son")
else:
    print(f"{son} tub son emas")
