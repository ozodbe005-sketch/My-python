talaba_0 = {
    'ism': 'alijon',
    'familiya': 'shamshiyev',
    'yosh': 22,
    'fakultet': 'matematika',
    'kurs': 4
}

print(talaba_0.items())  # .items() METODI Ushbu metod yordamida lug'at
# ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")

# .keys() METODIAgar lug'atdagi kalit so'zlarni ko'rish talab qilinsa,
# .keys() metodidan foydalanishimiz mumkin.

mahsulotlar = {  # Do'kondagi mahsulotlar
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.keys())

mahsulotlar = {  # Do'kondagi mahsulotlar
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.keys())


# .values() METODI Agar lug'atdagi qiymatlarni chiqarish talab qilinsa
#  .values() metodidan foydalanishimiz mumkin.

telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values():
    print(tel)


print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni
# saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi,
# va ularga indeks orqali murojat qilib bo'lmaydi. Shuningdek, set ichida bir hil elementlar bo'lmaydi.
toys = {'bus', 'car', 'bear', 'doll', 'car', 'puzzle', 'bus'}
print(toys)  # natija: {'car', 'puzzle', 'doll', 'bear', 'bus'}

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
