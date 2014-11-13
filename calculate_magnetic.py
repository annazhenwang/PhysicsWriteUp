import sys, os, time, math, array
r= 57 #cm
U = 7 #kV
mass_charge = [ 1, 2,4, 8, 20, 28, 32, 40 ] # mass charge ratio
f = open("magnetic field.txt", "w")
for i in range(len(mass_charge)):
    B = math.sqrt(2)/1.0e-2*math.sqrt(1.67e-27/1.6e-19)*math.sqrt(1.0e3)*1/r*math.sqrt(mass_charge[i])*math.sqrt(U)
    print( "%g" % B)
    f.write(str(B)+ "\n")
f.close()