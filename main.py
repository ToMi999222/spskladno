pismeno = input("zadejte pismeno co chcete hledat: ")
slovo = input("zadejte slovo ve kterém chcete hledat: ")
a = int(input("zadejte číslo 1. : "))
b = int(input("zadejte číslo 2. : "))
x = int(input("zadejte číslo 3. : "))
y = int(input("zadejte číslo 4. : "))
if a == b or pismeno in slovo or (x is y and a + b > 15):
    print("true")
else:
    print("false")
