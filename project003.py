print("Welcome to the Treasure Land!\nYour mission is to find the treasure.")
print()
gender = input("Are you female or male? Type M or F.")
if gender == "M":
    title = "King"
else:
    title = "Queen"

path1 = input("""You got thrown away by the ocean on the seashore of an unknown land.
You don't have any memories except your name. 
Would you rather enter the gloomy jungle or travel along the seashore? 
Type 'seashore' or 'jungle'. """)

if path1 == "jungle":
    print("""Unfortunately, you've suddenly felt dizzy and collapsed on the ground,
    The last thing you remember is some weird people gathering over your body.
    YOU DIED, better luck next time!""")
else:
    print("""The seashore path took you to the old bunker entrance right next to the beach.""")
    print()
    path2 = input("""It looks highly suspicious and seem to have bloody marks on the door,
    After checking, you notice the doors are open. Do you want to come in? Y or N. """)
    if path2 == "N":
        print("""You stayed outside, surrounded by the dark trees and uncanny noises
        and decided to rest a bit. You never woke up. 
              Better luck next time!""")
    else:
        print("""You began to slowly move down the stairs through the dark. 
        At the very bottom you see 3 different doors- black, white and red,""")
        path3 = input("Which one would you choose? Type 'black', 'white' or 'red' ")
        if path3 == "black":
            print("""When you entered the room, the door quickly shutted behind you,
            Ahead of you, group of people stood in circle. Whene you came closer you got to see
            what was in the middle of them. It was a dead body of a female and a bunch of candles
            
            A person in the dark robe emerged from the crowd with the thorn crown.""")
            ending1 = input(f"Will you be our {title}? (Y or N) ")
            if ending1 == "Y":
                print("""Crowd left the room, leaving you with the dead womens body. 
                You heard door locking behind you. There is only silence now.""")
                print()
                print("Well done you got... some ending, I suggest trying again!")
            else:
                print("Crowd killed you viciously, now you lie with the dead woman, waiting for another pray of the cult.")

        elif path3 == "white":
            print("""These doors were actually an elevator doors. You see the buttons, 100 of them,
            but none of them is working.
            There is one person beside you though, sitting on the elevator floor, old man
            looking like a homeless person.
                  
            \"Will you spare me with some money child?\" but you only have $10 in your pocket.""")
            money = float(input("How much will you give to the old man? $"))
            if money <= 2.0:
                print("""Old man took out the knife and stabbed you to death. 
                      
                GAME OVER""")
            else:
                button = int(input("""Thank you so much dear child, which floor are you traveling to?
                (pick 1-100) """))
                if button >= 60:
                    print("""*YOU ARRIVED TO THE UPPER FLOOR SYSTEM, 
                    here the dreams come true*
                          
                    You suddenly felt so light, bid a farwell to the beggar, he looked sad,
                    and stepped into""" + str(button) + """.""")
                    print("""CONGRATULATIONS, you will be living in the dream for the rest of your life
                    at least it will be peacefull...""")
                else:
                    print("""The level you arrived on seemed somehow like a maze.
                    you bid a farwell to the beggar and he wished you good luck.
                          
                    GAME OVER, you will spend the rest of your live wondering through
                    the endless maze.""")
        elif path3 == "red":
            door = input("""Behind the black door was a loooong corridor, you decided to follow it.
            After 2 h you finally saw the end... another door? Would you open it? (Y or N) """)
            if door == "Y":
                print(""".... huh.... YOU WAKED UP!!!
                \"YOU FINALLY WAKED UP\" said your loved one standing over your hospital bed.
                It finally came back to you that you had an accident and was in coma,
                
                You found the treasure, real life.""")
            else:
                print("""You feel dizzy, decided to come back... but never did...
                GAME OVER.""")

        


                


