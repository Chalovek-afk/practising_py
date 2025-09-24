from vector import Vector

v1 = Vector([3, 4])      # вектор (3, 4) на плоскости
v2 = Vector([1, 0])      # единичный вектор по оси X

print("v1 =", v1.components)
print("v2 =", v2.components) 

print("Длина v1:", v1.length())
print("Длина v2:", v2.length()) 

v3 = v1 * 2
print("v1 * 2 =", v3.components) 

v4 = 3 * v2
print("3 * v2 =", v4.components)

dot = v1.scalar_product(v2)
print("v1 · v2 =", dot) 

angle_rad = v1.angle_with(v2)
angle_deg = v1.angle_with(v2, degrees=True)

print(f"Угол в радианах: {angle_rad:.4f}")   
print(f"Угол в градусах: {angle_deg:.2f}°") 