zmrzlin = ["vanilková", "jahodová", "pistáciová", "citronová", "meruňková"]
velik = ["mini", "malá", "střední", "velká"]
cena = (20, 25, 30, 35)
cara = "=" *35
carajedna = "-" *35

druhy = '''
1 - vanilková
2 - jahodová
3 - pistáciová
4 - citronová
5 - meruňková
'''
velka = '''
1 - mini
2 - malá
3 - střední
4 - velká
'''

print("VÍTEJTE V NAŠÍ CUKRÁRNĚ")
print(carajedna)
print("Dnešní nabídka zmrzliny")
print(cara)
print(druhy)
print(cara)
print(velka)

print(cara)

zmrzlina = input("DRUH ZMRZLINY ČÍSLO:")
velikost = input("ZADEJTE ZVOLENOU VELIKOST:")
jmeno = input("ZADEJTE JEMÉNO:")

print(cara)

druh_zmrzliny = zmrzlin[int(zmrzlina) -1]
velikost_zmrzliny = velik[int(velikost ) -1]
finální_cena = cena[int(velikost) -1]



print("PŘÍCHUŤ ZMRZLINY:", druh_zmrzliny)
print("VELIKOST ZMRZLINY:", velikost_zmrzliny)
print("CENA ZMRZLINY:", finální_cena, ", -Kč")
print("ZÁKAZNÍK:", jmeno)

print(cara)

print("Děkujeme za Váš nákup \n Těšíme se na vaší další návštěvu")




