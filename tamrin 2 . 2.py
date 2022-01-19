w = float(input("vazn khod ra vared kon(kg):"))
g = float(input("gad kod ra vared kon(m):"))

mbi = w / g**2

if mbi < 18.8:
    result = "underweight"

if 18.5 < mbi < 24.9:
    result = "normal"

if 25.5 < mbi < 29.9:
    result = "overweight"

if 30 < mbi < 34.9:
    result = "obese"

if 35 < mbi:
    result = "extremely obse"

print(result)
