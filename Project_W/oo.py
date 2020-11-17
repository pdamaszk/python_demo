
import math
x1 = 2.4
x2 = 2.8

v1 = 3
v2 = 2

x= ((v1*x2)**2-(v2*x1)**2)/( (v1)**2-(v2)**2 )

# R = 6370000
# g = 9.81
# t = ((R/g)**(1/2))*math.pi/2
# v = -(g*R)**(1/2)
# print(t)
# print(v)



# todo ---------------------zad___ 02-05
# d = 5               # cm
# ro = 1              # kg/dm^3
# """-----------------------------"""
# d = d * 10**(-3)    # m
# ro = ro * 10**(3)  # kg/m^3
# m = 0.25            # kg
# g = 9.81            # m/s
# T = (((math.pi*m)/(ro*g))**(1/2))*4/d
# T2 = ((16*m*math.pi)/((d**2)*ro*g))**(1/2)
# print(d, m, ro, g)
# print(T)
# print(d, m, ro, g)
# print(T2)
# print(d, m, ro, g)
# print((math.sqrt((m*math.pi)/(ro*g))*4/d))
# print((math.sqrt((m*math.pi)/(ro*g)))*4/d)
# print((math.sqrt((16*m*math.pi)/(ro*g*d**2))))
# print()
# todo ---------------------zad___ 03-02

T0 = 273.16
T1 = 298.16
t0 = 3
alfa = 18.9*10**(-6)

t1 = t0*math.sqrt(1+alfa*(T1-T0))
print(alfa)
print(t1)



