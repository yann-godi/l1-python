def TempsEnSeconde(temps):
    """renvoi le temps (en jour, heure, minute, seconde) en seconde."""
    jour, heure, minute, seconde = temps
    return ((jour*24 + heure)*60 + minute)*60 + seconde 

temps = (1, 2, 3, 4)  
print(type(temps))
print(TempsEnSeconde(temps))

def secondeEnTemps(seconde):
     """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // seconde (24*60*60)
    seconde = seconde % (24*60*60)
    heure = seconde // (60*60)
    seconde = seconde % (60*60)
    minute = seconde // 60
    seconde = seconde % 60
    return (jour, heure, minute, seconde)


temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")



#fonction auxiliaire ici
def affiche_pluriel(valeur, mot):
    if (valeur != 0):
        print (valeur, end= " ")
        print (mot, end= "")
        if (valeur > 1):
            print ("s", end= "")
        print(" ", end= " ")



def afficheTemps(temps):
    affiche_pluriel(temps[0], "jour")
    affiche_pluriel(temps[1], "heure")
    affiche_pluriel(temps[2], "minute")
    affiche_pluriel(temps[3], "seconde")
    print (" ")

    
afficheTemps((1,0,14,23))  


def demandeTemps():
    jour = int(input("entrer un nombre de jours"))
    heure = int(input("entrer un nombre d'heures"))
    if (heure > 23):
        print("Nombre d'heure incorrecte")
        return
    minute = int(input("entrer un nombre de minutes"))
    if (minute > 59):
        print("Nombre de minute incorrecte")
        return
    seconde = int(input("entrer un nombre de secondes"))
    if (seconde > 59):
        print("Nombre de secondes incorrecte")
        return
    return (jour, heure, minute, seconde)

afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    return secondeEnTemps(TempsEnSeconde(temps1)) + TempsEnSeconde(temps2)

sommeTemps((2,3,4,25),(5,22,57,1))