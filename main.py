cvičení 1:

vek = (-6)

if vek >= 18:
    print("Dospělý")
elif vek >= 15:
    print("Dospívající")
elif vek > 0:
    print("Dítě")
elif vek <= 0:
    print("neplatný věk")

cvičení 2:

x = input("pozice:" )
y = int( input() )

if x == "dalnice":
    if y <= 130:
        print("OK")
    else:
        print("Vysoká rychlost")
elif x == "mimo_obec":
    if y <= 90:
        print("OK")
    else:
        print("Vysoká rychlost")
elif x == "obec":
    if y <= 50:
        print("OK")
    else:
        print("Vysoká rychlost")