oddelovac = "=" * 62
 
sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")
 
uzivatele = {
"tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
"petr": {"The Godfather", "The Dark Knight"},
"marek": {"The Dark Knight", "The Prestige"}
}
 
film_1 = {
"JMENO": "Shawshank Redemption",
"HODNOCENI": "93/100",
"ROK": 1994,
"REZISER": "Frank Darabont",
"STOPAZ": 144,
"HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
"Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
"Jeffrey DeMunn", "Larry Brandenburg"
)
}
 
film_2 = {
"JMENO": "The Godfather",
"HODNOCENI": "92/100",
"ROK": 1972,
"REZISER": "Francis Ford Coppola",
"STOPAZ": 175,
"HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
"Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
"John Marley", "Richard Conte"
)
}
 
film_3 = {
"JMENO": "The Dark Knight",
"HODNOCENI": "90/100",
"ROK": 2008,
"REZISER": "Christopher Nolan",
"STOPAZ": 152,
"HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
"Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
"Monique Gabriela", "Ron Dean", "Cillian Murphy"
)
}
 
film_4 = {
"JMENO": "The Prestige",
"HODNOCENI": "85/100",
"ROK": 2006,
"REZISER": "Christopher Nolan",
"STOPAZ": 130,
"HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
"Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
"David Bowie"
)
}

filmy = {
    film_1["JMENO"] : film_1,
    film_2["JMENO"] : film_2,
    film_3["JMENO"] : film_3,
    film_4["JMENO"] : film_4,
}
print(type(filmy))
print(len("filmy"))
uzivatel = input("Zadej jméno:")
if not uzivatel in uzivatele:
    print("Promintě nejste rgistrovaným uživatelem.")
    quit()
else :
    print("vítej, jsi přihlášen", oddelovac, sep="\n" )
    print("Vítejte v našm filmovém slovníku".upper().center(62), oddelovac, sep="\n")    
print(("| " + "| ".join(sluzby) + "|").center(62), oddelovac, sep="\n")

sluzba = input("Vyber sluzbu: ")
print(f"Vybral si sluzbu")