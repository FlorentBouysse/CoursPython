# Il existe plusieurs manières de gérer les erreurs
# sans que le script s'arrête : 
### If else
### Try except

# Ici pas d'erreur
a = 5;
b = 10;

print(a / b);


#######################################################################
#### TRY EXCEPT
#######################################################################

# Erreur, impossible de diviser par 0
# On va donc utiliser un try except et maintenant ça marche
# Seulement, on ne peut pas savoir si c'est réellement le problème,
# si on mets une chaine de caractère, nous aurons toujours la même 
# erreur
a = 5;
b = 0;
# b = "salut";

# print(a / b);

try:
    print(a / b);
except:
    print("Division par 0 impossible")

# Ici nous ajoutons "ZeroDivisionError" à "except" pour qu'il puisse 
# gérer l'erreur de type int, cela renverra toutefois une erreur de type 
# si on remplace la variable b = 0 par b = "salut"

# Else: est ici dans le cas où il n'y a pas d'erreur
# Finally: sera executé quoi qu'il arrive
a = 5;
c = 5;
# c = 0;
# c = "salut";

try:
    result =  a / c;
except ZeroDivisionError:
    print("Division par 0 impossble");
except TypeError:
    print("Chaine de caractère non autorisé !");
except NameError as e:
    print("Une des variables n'est pas défini: ", e);
else:
    print(result);
finally:
    print("Fin du script");


#######################################################################
#### IF ELSE
#######################################################################

i = 5;
j = 20;

if 'i' in locals() and 'j' in locals():
    if i != 0 and j !=0:
        if str(i).isdigit() and str(j).isdigit():
            print(i / j);
        else:
            print("Les variables doivent contenir des chiffres");
    else:
        print("Division par 0 impossible");
else:
    print("Une des variables n'est pas défini");