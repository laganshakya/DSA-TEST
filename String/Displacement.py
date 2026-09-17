x = 0
y = 0
direc = input("Enter the direction (N/S/E/W): ")
for i in direc :
    if i.upper() == "N":
        y += 1
    elif i.upper() == "S":
        y -= 1
    elif i.upper() == "E":
        x += 1
    elif i.upper() == "W":
        x -= 1

# Find the displacement of the object from origin (if every block is 1 unit )

print("Displacement of the object from origin:", ((x**2) + (y**2))**0.5, "units")