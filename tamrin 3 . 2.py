name = input("asm khod ra vared kon:")
family = input("famil khod ra vared kon:")
riazy = float(input("nomre drs riazy khod ra vared kon:"))
olom = float(input("nomre drs olom khod ra vared kon:"))
farsi = float(input("nomre drs farsi khod ra vared kon:"))

average = (riazy + olom + farsi) / 3

if average > 17:
    result = "greage" 

if 17 > average > 12:
    result = "normal"

if average < 12:
    result = "fail"

print(result)