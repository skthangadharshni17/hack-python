import math
ab = int(input())
bc = int(input())
angle_rad = math.atan(ab / bc)
angle_deg = math.degrees(angle_rad)
print(f"{round(angle_deg)}{chr(176)}")