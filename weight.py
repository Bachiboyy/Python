talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))
weight = talents * 20 * 32 * 13.3 + pounds * 32 * 13.3 + lots * 13.3
print("The weight in modern units:  \n")
kilograms = weight // 1000
grams = weight % 1000
print(f"{kilograms:.0f} kilograms {grams:.2f} grams")
