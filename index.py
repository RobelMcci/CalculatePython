import math

a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))
c = int(input("Entrez la valeur de c : "))

deltat = b*b - 4*a*c

if deltat > 0 :
    x1 = (-b - math.sqrt(deltat))/2*a
    x2 = (-b + math.sqrt(deltat))/2*a
    print ("L'équation   ax2+bx+c=0 a deux solutions distinctes")
    print("Les valeurs de X sont " , x1 , "et" , x2)

elif deltat == 0 :
    x = -b/2*a
    print("L'équation   ax2+bx+c=0 a une solution unique")
    print("La valeur de X est " , x)

else :
    print("Il n'y a pas de solution réelle")

