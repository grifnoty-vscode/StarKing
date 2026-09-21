m = float(input("Введіть масу пирога : ")) 
flour_kg = 0.28 * m
flour_g = flour_kg * 1000

print(f"Для приготування пирога масою {m} кг потрібно: {flour_kg} кг борошна або {flour_g} г борошна")
