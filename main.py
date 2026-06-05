# لعبة اكبر اصغر
import random

r = random.randint(1, 100)
print("مرحبا بك في لعبة اكبر اصغر")
while True:
    n = int(input("اختار بين 1 و 100: "))
    if n < r:
        print("اصغر")
    elif n > r:
        print("اكبر")
    else:
        print("مبروك! لقد خمنت الرقم الصحيح.")
        break