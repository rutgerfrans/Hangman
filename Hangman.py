# De Imports
import random
import os
import sys

# Plaatjes Galgje
plaatje_0 = '\n======================\nStatus:\n\nN/A\n\n'
plaatje_1 = '\n======================\nStatus:\n|\n|\n|\n|\n|_ _'
plaatje_2 = '\n======================\nStatus:\n___\n|\n|\n|\n|\n|_ _'
plaatje_3 = '\n======================\nStatus:\n___\n|/\n|\n|\n|\n|_ _'
plaatje_4 = '\n======================\nStatus:\n___\n|/ |\n|\n|\n|\n|_ _'
plaatje_5 = '\n======================\nStatus:\n___\n|/ |\n|  0\n|\n|\n|_ _'
plaatje_6 = '\n======================\nStatus:\n___\n|/ |\n|  0\n|  |\n|\n|_ _'
plaatje_7 = '\n======================\nStatus:\n___\n|/ |\n|  0\n| /|\n|\n|_ _'
plaatje_8 = '\n======================\nStatus:\n___\n|/ |\n|  0\n| /|\\\n|\n|_ _'
plaatje_9 = '\n======================\nStatus:\n___\n|/ |\n|  0\n| /|\\\n| /\n|_ _'
plaatje_10 = '\n======================\nStatus:\n___\n|/ |\n|  0\n| /|\\\n| / \\\n|_ _'

# De Lijsten
LijstBot = ['afsnauwen','wijnglas','stoeptegel','puzzel','bestek','woordenboek','camera','laptoptas','wolkenkrabber','accu','koplamp','laser','apenstaart','kunststof','drugs']
Lijstplaatje = [plaatje_0,plaatje_1,plaatje_2,plaatje_3,plaatje_4,plaatje_5,plaatje_6,plaatje_7,plaatje_8,plaatje_9,plaatje_10]
Lijst = []

Hoofd_Menu = 'y'


# de functies
# in deze functies staan stukjes code die in het programma door herhaalt worden.
# ik gebruik deze functies, om niet telkens een zelfde stuk code overnieuw te schrijven.
def functie_1():
    # Het Vervangen van het woord met '_', zodat deze streepjes later kunnen vervangen worden met de juist geraden letters.
    for x in range(len(woord)):
            Lijst[0][x] = '_'
def functie_2():
    # Dit is een command om in het commandlineinterface het scherm te ''clearen'' waardoor je gelijk het volgend opkomende scherm te zien krijgt.
    os.system('cls')
def functie_3():
    # Hier word het te raden woord in een lijst gezet. dit woord wordt met de command ''list'' in letters gesplits. voorbeeld: lijst = [['w','o','o','r','d']]
    Lijst.append(list(woord))
def functie_4():
    # Dit is een print de de speler vraagt of er nog een keer gespeeld wilt worden.
    print('======================\nWil je nog een keer spelen?')
def functie_5():
    # Dit is een input die de speler het spel uit begeleidt.    
    input('======================\nTot ziens!\n======================\nPress [Enter]')
def functie_6():
    # Deze commands worden aan het einde van het spel gebruikt om de lijsten te deleten zodat bij een nieuw spel ook nieuwe woorden te raden zijn.oude 
    del Lijst[0]
    del LijstGebruikteLetters[1]
    

    
# Dit is het hoofdmenu, waar 1 variabelen wordt toegekend aan een waarde die later gebruikt gaat worden, een lijst die aangemaakt wordt, een functie die refereerd naar een stukje-
# code die begint bij lijn 27. (met de benodigde toelichting.)
# Verder wordt er een Bolean value aangeduidt ''WoordRaden'', deze wordt later gebruikt om een while loop in te komen.
# Ook is er een print die het hoofdmenu visueel laat zien.
# De input is om de speler een keuze te laten maken. Daar onder staat 'Menu.lower()', dit is om de invoer naar kleine letters om te zetten.
while Hoofd_Menu == 'y':
    Fout = 0
    LijstGebruikteLetters = [[]]
    functie_2()
    WoordRaden = True
    print('\n======================\nHoofdMenu:\n[1] 1 speler\n[2] 2 spelers\n[S] Stop\n======================')
    Menu = input('Optie: ')
    Menu.lower()
    
    # menu 1
    # Dit menu betreedt je als je bij het hoofdmenu als optie '1' kiest.
    # Bij dit menu speel je tegen de computer. Je speelt dus in je eentje.
    # Hier worden twee variabelen toegekend aan een waarden, die later in de code gebruikt worden.
    # de 'rng' is een random integer gegenereert door de command 'random.randint(0,14)'. later wordt deze integer toegekend aan een woord in de lijst 'LijstBot'.
    # daar onder staan drie functie die refereren naar een stuk code die beginnen bij lijn 27.(daar staat ook de benodigde uitleg)
    if Menu == '1':
        EindIndex = 0
        LijstPlaatjeIndex = 0
        rng = random.randint(0,14)
        woord = LijstBot[rng]
        functie_3()
        functie_2()      
        functie_1()
        
    # menu 2
    # Dit menu betreedt je als je bij het hoofdmenu als optie '2' kiest.
    # In dit menu speel je met twee spelers. De een moet het woord verzinnen de ander moet het raden.
    # Hier worden twee variabelen toegekend aan een waarden, die later in de code gebruikt worden.
    # Onder de variabelen staat een input die de eerste speler een verzonnen woord laat kiezen die door speler 2 geraden moet worden.
    # Het stukje code 'woord.lower()' zorgt ervoor dat alle ingevoerde letters 'kleine' letters worden.
    # daar onder staan drie functie die refereren naar een stuk code die beginnen bij lijn 27.(daar staat ook de benodigde uitleg)
    elif  Menu == '2':
        EindIndex = 0
        LijstPlaatjeIndex = 0
        woord = input('======================\nVoer een woord in: ')
        woord.lower()
        functie_3()
        functie_2()      
        functie_1()
        
    # menu S
    # Dit menu betreedt je als je bij het hoofdmenu als optie 's' kiest.
    # In dit menu krijg je de keuze om het spel te verlaten.
    # De eerste functie refereert naar de stukjes code die beginnen bij lijn 27. (met de benodigde uitleg)
    # De input print een tekst of je het spel wilt verlaten.
    # de command 'Hoofd_Menu.lower()' maakt de ingevoerde letters klein.
    # als er 'y' wordt ingetypt wordt het spel verlaten met de command sys.exit()
    elif  Menu == 's':
        functie_2()
        Hoofd_Menu = input('======================\nWil je het spel echt verlaten?\n[Y/N]:')
        Hoofd_Menu.lower()
        if Hoofd_Menu == 'y':
            sys.exit()

            
    # spel
    # Dit is het stuk code wat betreedt wordt zodra er menu 1 of 2 gekozen is.

    # Dit is een while loop met daaronder een print, deze geven het eerste 'grafische scherm weer'.
    # Je blijft in de while loop zolang q kleiner is dan de lengte van de lijst.
    # Terwijl je in de loop zit print de while loop een voor een de inhoud van de lijst.
    # Met het command 'end=' '' laat ik de letters naast elkaar printen ipv onder elkaar.
    # Onder de while loop staat een print die de tot nu toe gebruikte letters print met ernaast het plaatje met het eerste galgje erin.
    q = 0
    while q < len(Lijst[0]):
        print(Lijst[0][q], end=' ')
        q = q + 1
    print('\n======================\nGebruikte letters:\n', plaatje_0)

    # Dit is een whileloop waar het spel daadwerkelijk begint.
    # Er worden hier twee variabelen een waarde toegekent die later in de code gebruikt worden.
    while WoordRaden == True:
        y = 0
        GebruikteLetters = 1
        
        # lose
        # Als het aantal gemaakte fouten 10 bereikt betreedt je deze if statement.
        # Als eerste krijg je een print tezien die aangeeft dat je 'GameOver' bent en wat het teradenwoord was.
        # Daarna is er een functie waarvan de uitleg begint bij lijn 27.
        # Daarna volgt er een input die vervolgens door de command 'Hoofd_Menu.lower()' uncaptioned wordt.
        # Daarna volgt er een functie waarvan de uitleg bij lijn 27 wordt toegelicht.
        # Dan wordt de variabelen 'WoordRaden' toegekend aan False zodat je uit de while loop komt.
        # Als er bij functie_2 'n' wordt ingetypt wordt je met functie_5 het spel uitgelijdt.
        # Met functie zes worden de lijsten gedelete voor een eventueel volgend spelletje. (zie toelicthing bij lijn 27)
        if Fout == 10:
            print('======================\nGameOver!\nHet te raden woord was: ', woord)
            functie_4()
            Hoofd_Menu = input('[Y/N]: ')
            Hoofd_Menu.lower()
            functie_2()
            WoordRaden = False
            functie_6()
            if Hoofd_Menu == 'n':
                functie_5()
            
        # Win
        # Als het aantal goede antwoorden de lengte van het teradenwoord heeft bereikt betreedt je deze if statement.
        # Als eerste krijg je een print tezien die aangeeft dat je het woord 'geraden' hebt.
        # Daarna is er een functie waarvan de uitleg begint bij lijn 27.
        # Daarna volgt er een input die vervolgens door de command 'Hoofd_Menu.lower()' uncaptioned wordt.
        # Daarna volgt er een functie waarvan de uitleg bij lijn 27 wordt toegelicht.
        # Dan wordt de variabelen 'WoordRaden' toegekend aan False zodat je uit de while loop komt.
        # Als er bij functie_2 'n' wordt ingetypt wordt je met functie_5 het spel uitgelijdt.
        # Met functie zes worden de lijsten gedelete voor een eventueel volgend spelletje. (zie toelicthing bij lijn 27)
        elif EindIndex == len(woord):
            print('\n======================\nGeraden!')
            functie_4()
            Hoofd_Menu = input('[Y/N]: ')
            Hoofd_Menu.lower()
            functie_2()
            WoordRaden = False
            functie_6()
            if Hoofd_Menu == 'n':
                functie_5()
                    
        # Spel spelende
        # Deze if statement wordt betreden zolang het aantal goedgeraden letters kleiner is dan de lengte van het teraden woord.
        # Eerst krijg je een input te zien met de vraag welke letter je wilt raden.
        # Daarna wordt die letter toegevoegd aan de lijst 'LijstGebruikteLetters' met de command 'append'.
        # Dan wordt het scherm ververst met functie_2.
        elif EindIndex < len(woord):
            letter = input('\n======================\nletter:')
            LijstGebruikteLetters.append(letter)
            functie_2()

            # Hier gaan we een foorloopje in met de de tijdelijke variabelen x met de range in de lengte van het teradenwoord.
            for x in range(len(woord)):
                
                # Juiste letter
                # Als de juiste letter geraden wordt, wat wordt gecheckt met 'if woord[x] == letter:', dan wordt de index die de x op dat moment heeft in de 'Lijst' vervangen met de ingevoerde letter.
                # daarna krijgt 'EindIndex' ,ook wel aantal goed geraden letters, een 1 erbij. dit zodat als deze variabelen even groot is als de lengte van het woord je kunt winnen.
                if woord[x] == letter:
                    Lijst[0][x] = letter
                    EindIndex = EindIndex + 1
                    
            # Foute Letter
            # Als je een foute letter hebt, wat woord gecheckt met 'if letter not in woord:', dan krijgt de variabelen 'LijstPlaatjeIndex' een 1 erbij. zodat het volgende galgplaatje getoont kan worden.
            # Daarna krijgt de variabelen Fout een waarde extra zodat als deze de lengte van de lijst van 'LijstPlaatje' bereikt, je verliest
            if letter not in woord:
                LijstPlaatjeIndex = LijstPlaatjeIndex + 1
                Fout = Fout + 1


            # het interface printen
            # met behulp van deze twee while loopjes word het interface gemaakt.
            # de eerste whileloop lijkt erg veel op de eerste op lijn 110.
            # Hier wordt simpel weg, zolang de y kleiner is dan de lengte van de lijst, het woordt geprint met de missende letters. voorbeeld _ _ E _ E N
            # Met het command 'end=' '' laat ik de letters naast elkaar printen ipv onder elkaar.
            while y < len(Lijst[0]):
                print(Lijst[0][y], end=' ')
                y = y + 1
                
            # Dit is een simpele print met de tekst 'Gebruikte letters'.
            print('\n======================\nGebruikte letters:')

            # Dit is de tweede whileloop van het interface.
            # Deze whileloop laat simpel weg de gebruikte letters zien. Zolang de variabelen 'GebruikteLetters' kleiner is dan de lengte van de lijst 'LijstGebruikteLetters' 
            # Met het command 'end='-'' laat ik de letters naast elkaar printen ipv onder elkaar.
            while GebruikteLetters < len(LijstGebruikteLetters):
                print(LijstGebruikteLetters[GebruikteLetters], end='-')
                GebruikteLetters = GebruikteLetters + 1

            # Deze print maakt het interface af.
            # Deze print laat simpel weg de status zien van het galgje.
            print(Lijstplaatje[LijstPlaatjeIndex])
