#Lucas Wenger
#Project 4 - Make a game 
#Due November 30, 2018
#Pseudo-Pokemon game - player earns money by battling trainers and attempts to catch all of the pokemon
#(Pokemon is owned by Nintendo)

'''
IMPORTED PACKAGES/FILES
'''
import sys
from PType import *
from Move import *
from HealingItem import *
from Pokeball import *
from Pokemon import *
from Trainer import *
from Player import *

'''
INITIALIZE PLAYER CLASS
'''
#Player class
Player = Player()

'''
TYPES
'''
#Implemented types
Normal = PType('Normal',None,None)
Grass = PType('Grass',None,None)
Fire = PType('Fire',Grass,None)
Grass.weakness = Fire
Water = PType('Water',Fire,Grass)
Grass.strength = Water
Fire.weakness = Water
Dragon = PType('Dragon',None,None)
Dragon.strength = Dragon
Dragon.weakness = Dragon

'''
MOVES
'''
#Implemented moves
Tackle = Move('Tackle',Normal,5,80) 
Burn = Move('Burn',Fire,8,60) 
VineWhip = Move('Vine Whip',Grass,5,100) 
Bubble = Move('Bubble',Water,6,90)
Scratch = Move('Scratch',Normal,6,70)
Outrage = Move('Outrage',Dragon,50,50)
HyperBeam = Move('Hyper Beam',Normal,100,20)

'''
HEALING ITEMS
'''
#Implemented player healing items
PlayerPotion = HealingItem('Potion','Potions',20,0,10) 

Player.healing_items.append(PlayerPotion)

'''
POKEBALLS
'''
#Implemented pokeballs
pokeball = Ball('Pokeball','Pokeballs',15,0,30)
masterball = Ball('Master Ball','Master Balls',1000,0,100)

Player.pokeball_bag.append(pokeball)
Player.pokeball_bag.append(masterball)

'''
POKEMON
'''
#Implemented Pokemon
PlayerCharmander = Pokemon('Charmander',1,Fire,20,[Tackle,Burn],40) 
PlayerBulbasaur = Pokemon('Bulbasaur',1,Grass,20,[Tackle,VineWhip],40) 
PlayerSquirtle = Pokemon('Squirtle',1,Water,20,[Tackle,Bubble],40)
PlayerPidgey = Pokemon('Pidgey',1,Normal,18,[Tackle,Scratch],30)
PlayerGyrados = Pokemon('Gyrados',1,Water,30,[Tackle,Bubble,HyperBeam],65)
PlayerDragonite = Pokemon('Dragonite',1,Dragon,50,[Outrage,HyperBeam,Scratch],80)

#WILD POKEMON BOX
wild_pokemon = [PlayerCharmander,PlayerBulbasaur,PlayerSquirtle,PlayerPidgey,PlayerGyrados,PlayerDragonite]

'''
TRAINERS
'''
#Implemented trainers and their equipment
JerryBulbasaur = Pokemon('Jerry\'s Bulbasaur',1,Grass,20,[Tackle,VineWhip],0) 
JerryPotion = HealingItem('Potion','Potions',15,2,10) 
Jerry = Trainer('Jerry',JerryBulbasaur,[JerryPotion],20)

CarlosCharmander = Pokemon('Carlos\' Charmander',1,Fire,20,[Tackle,Burn],0)
CarlosPotion = HealingItem('Potion','Potions',15,2,10)
Carlos = Trainer('Carlos',CarlosCharmander,[CarlosPotion],20)

SallySquirtle = Pokemon('Sally\'s Squirtle',1,Water,20,[Tackle,Bubble],0)
SallyPotion = HealingItem('Potion','Potions',15,2,10)
Sally = Trainer('Sally',SallySquirtle,[SallyPotion],20)

#TRAINER BOOKKEEPING
trainerlist = [Jerry,Carlos,Sally]

'''
FUNCTIONS
'''
def combat(trainer,player=None):
    if player==None:
        player = Player
    print("\nYou have encountered Pokemon Trainer " + trainer.name + "!")
    print(player.active_pokemon.name + " has entered combat with " + trainer.pokemon.name + "!\n")
    player.active_pokemon.temphealth = player.active_pokemon.maxhealth
    trainer.pokemon.temphealth = trainer.pokemon.maxhealth
    while player.active_pokemon.temphealth > 0 and trainer.pokemon.temphealth > 0:
        print(player.active_pokemon.name + " has " + str(player.active_pokemon.temphealth) + " health.")
        print(trainer.pokemon.name + " has " + str(trainer.pokemon.temphealth) + " health.")
        player.playerturn(trainer.pokemon)
        print('\n')
        if player.active_pokemon.temphealth <= 0 or trainer.pokemon.temphealth <= 0:
            break
        trainer.trainerturn(player)
    if player.active_pokemon.temphealth <= 0:
        print("You fainted!")
        if player.money == 0:
            print("You can't pay " + trainer.name + " anything. You walk home in disgrace.")
        elif player.money < trainer.reward:
            print("You can only pay " + trainer.name + " " + str(player.money) + " munny. You walk home in disgrace.")
            player.money = 0
        else:
            print("You pay " + trainer.name + " " + str(trainer.reward) + " munny. " + trainer.name + " thanks you and moves along.")
            player.money -= trainer.reward
    else:
        print("You win!")
        print(trainer.name + " pays you " + str(trainer.reward) + " munny and moves along.")
        player.money += trainer.reward

def catch(pokemon,player=Player):
    answer = ''
    print("A wild " + pokemon.name + " has appeared!")
    while True:
        print("What would you like to do?")
        print("1. Throw pokeball")
        print("2. Run away")
        while answer not in ['1','2']:
            answer = input("\nEnter a number.\n")
        if answer == '1':
            answer = ''
            while True:
                while answer not in range(1,len(player.pokeball_bag)+2):
                    for i in player.pokeball_bag:
                        print(str(player.pokeball_bag.index(i)+1) + ". " + i.name + " -- x" + str(i.amount))
                    print(str(player.pokeball_bag.index(i)+2) + ". " + "Return")
                    try:
                        answer = int(input("Which pokeball would you like to use? Enter a number.\n"))
                        break
                    except ValueError:
                        continue
                if answer in range(1,len(player.pokeball_bag)+1):
                    if player.pokeball_bag[answer-1].amount > 0:
                        player.pokeball_bag[answer-1].amount -= 1
                        catchchance = random.randint(0,100)
                        if catchchance <= player.pokeball_bag[answer-1].catchchance:
                            print("Congratulations! You caught " + pokemon.name + "!")
                            wild_pokemon.remove(pokemon)
                            player.pokemon_list.append(pokemon)
                            return
                        else:
                            print("It escaped from the " + player.pokeball_bag[answer-1].name + "!")    
                        answer = 0
                    else:
                        answer = 0
                        print("You don't have any " + player.pokeball_bag[answer-1].plural + " left!")
                elif answer == len(player.pokeball_bag)+1:
                    catch(pokemon)
                escapechance = random.randint(0,100)
                if escapechance <= pokemon.escapechance:
                    print("The pokemon escaped!")
                    return
        if answer == '2':
            print("You ran away!")
            return

def shop(player=Player):
    answer = ''
    print("\nSHOPKEEPER: Welcome to the Pokemon Shop! What would you like to buy?\n")
    print("1. Pokeballs")
    print("2. Healing Items")
    print("3. Leave shop")
    while answer not in ['1','2','3']:
        answer = input("\nEnter a number.\n")
    if answer == '1':
        answer = ''
        while answer not in range(1,len(player.pokeball_bag)+2):
            for i in player.pokeball_bag:
                print(str(player.pokeball_bag.index(i)+1) + ". " + i.name + " -- x" + str(i.amount) + "     " + str(i.cost) + " munny")
            print(str(player.pokeball_bag.index(i)+2) + ". " + "Return")
            print("\nYou have " + str(player.money) + " munny.\n")
            while True:
                try:
                    answer = int(input("What would you like to buy? Enter a number.\n"))
                    break
                except ValueError:
                    continue
            if answer in range(1,len(player.pokeball_bag)+1):
                if (player.money - player.pokeball_bag[answer-1].cost) >= 0:
                    player.pokeball_bag[answer-1].amount += 1
                    player.money -= player.pokeball_bag[answer-1].cost
                    answer = 0
                    print("Thank you!\n")
                else:
                    answer = 0
                    print("You don't have enough munny!")
            elif answer == len(player.pokeball_bag)+1:
                shop()
    elif answer == '2':
        answer = ''
        while answer not in range(1,len(player.healing_items)+2):
            for i in player.healing_items:
                print(str(player.healing_items.index(i)+1) + ". " + i.name + " -- x" + str(i.amount) + "      " + str(i.cost) + " munny")
            print(str(player.healing_items.index(i)+2) + ". " + "Return")
            print("\nYou have " + str(player.money) + " munny.\n")
            while True:
                try:
                    answer = int(input("What would you like to buy? Enter a number.\n"))
                    break
                except ValueError:
                    continue
            if answer in range(1,len(player.healing_items)+1):
                if (player.money - player.healing_items[answer-1].cost) >= 0:
                    player.healing_items[answer-1].amount += 1
                    player.money -= player.healing_items[answer-1].cost
                    answer = 0
                    print("Thank you!\n")
                else:
                    answer = 0
                    print("You don't have enough munny!")
            elif answer == len(player.healing_items)+1:
                shop()
    elif answer == '3':
        print("SHOPKEEPER: Thank you for your business! Come again!")
        return

def viewpokemon(pokemon,player=Player):
    print("\nWhat would you like to do?")
    print("1. View moves")
    print("2. Make active Pokemon")
    print("3. Return")
    answer = ''
    while answer not in ['1','2','3']:
        answer = input("\nEnter a number.\n")
    if answer == '1':
        for i in pokemon.moves:
            print(i.name)
        viewpokemon(pokemon)
    if answer == '2':
        player.active_pokemon = pokemon
        print(pokemon.name + " is now your active Pokemon!")
        viewpokemon(pokemon)
    if answer == '3':
        return

def viewall(player=Player):
    print("What would you like to view?\n")
    print("1. Pokemon")
    print("2. Healing Items")
    print("3. Pokeballs")
    print("4. Return")
    answer = ''
    while answer not in ['1','2','3','4']:
        print("Enter a number.\n")
        answer = input()
    if answer == '1':
        for i in player.pokemon_list:
            if i == player.active_pokemon:
                print(i.name + " (active pokemon)")
            else:
                print(i.name)
        print("\nWhich Pokemon would you like to view?")
        pokemon_list_names = [i.name for i in player.pokemon_list]
        while answer not in ['r'] and answer not in pokemon_list_names:
            answer = input("Enter the name of the Pokemon or enter 'r' to return.\n")
        if answer == 'r':
            viewall(player)
        else:
            for i in pokemon_list_names:
                if answer == i:
                    selectedpokemon = player.pokemon_list[pokemon_list_names.index(i)]
                    viewpokemon(selectedpokemon)
                    viewall()
    if answer == '2':
        for i in player.healing_items:
            print(i.name + " -- x" + str(i.amount))
        while answer not in ['r','m']:
            answer = input("Enter 'r' to return or 'm' to go back to the main menu.\n")
        if answer == 'r':
            viewall()
        if answer == 'm':
            return
    if answer == '3':
        for i in player.pokeball_bag:
            print(i.name + " -- x" + str(i.amount))
        while answer not in ['r','m']:
            answer = input("Enter 'r' to return or 'm' to go back to the menu.\n")
        if answer == 'r':
            viewall()
        if answer == 'm':
            return
    if answer == '4':
        return

'''
GAME
'''
print("PPPPPPPPPPPPPPPPP        OOOOOOOOO     KKKKKKKKK    KKKKKKKEEEEEEEEEEEEEEEEEEEEEEMMMMMMMM               MMMMMMMM     OOOOOOOOO     NNNNNNNN        NNNNNNNN")
print("P::::::::::::::::P     OO:::::::::OO   K:::::::K    K:::::KE::::::::::::::::::::EM:::::::M             M:::::::M   OO:::::::::OO   N:::::::N       N::::::N")
print("P::::::PPPPPP:::::P  OO:::::::::::::OO K:::::::K    K:::::KE::::::::::::::::::::EM::::::::M           M::::::::M OO:::::::::::::OO N::::::::N      N::::::N")
print("PP:::::P     P:::::PO:::::::OOO:::::::OK:::::::K   K::::::KEE::::::EEEEEEEEE::::EM:::::::::M         M:::::::::MO:::::::OOO:::::::ON:::::::::N     N::::::N")
print("  P::::P     P:::::PO::::::O   O::::::OKK::::::K  K:::::KKK  E:::::E       EEEEEEM::::::::::M       M::::::::::MO::::::O   O::::::ON::::::::::N    N::::::N")
print("  P::::P     P:::::PO:::::O     O:::::O  K:::::K K:::::K     E:::::E             M:::::::::::M     M:::::::::::MO:::::O     O:::::ON:::::::::::N   N::::::N")
print("  P::::PPPPPP:::::P O:::::O     O:::::O  K::::::K:::::K      E::::::EEEEEEEEEE   M:::::::M::::M   M::::M:::::::MO:::::O     O:::::ON:::::::N::::N  N::::::N")
print("  P:::::::::::::PP  O:::::O     O:::::O  K:::::::::::K       E:::::::::::::::E   M::::::M M::::M M::::M M::::::MO:::::O     O:::::ON::::::N N::::N N::::::N")
print("  P::::PPPPPPPPP    O:::::O     O:::::O  K:::::::::::K       E:::::::::::::::E   M::::::M  M::::M::::M  M::::::MO:::::O     O:::::ON::::::N  N::::N:::::::N")
print("  P::::P            O:::::O     O:::::O  K::::::K:::::K      E::::::EEEEEEEEEE   M::::::M   M:::::::M   M::::::MO:::::O     O:::::ON::::::N   N:::::::::::N")
print("  P::::P            O:::::O     O:::::O  K:::::K K:::::K     E:::::E             M::::::M    M:::::M    M::::::MO:::::O     O:::::ON::::::N    N::::::::::N")
print("  P::::P            O::::::O   O::::::OKK::::::K  K:::::KKK  E:::::E       EEEEEEM::::::M     MMMMM     M::::::MO::::::O   O::::::ON::::::N     N:::::::::N")
print("PP::::::PP          O:::::::OOO:::::::OK:::::::K   K::::::KEE::::::EEEEEEEE:::::EM::::::M               M::::::MO:::::::OOO:::::::ON::::::N      N::::::::N")
print("P::::::::P           OO:::::::::::::OO K:::::::K    K:::::KE::::::::::::::::::::EM::::::M               M::::::M OO:::::::::::::OO N::::::N       N:::::::N")
print("P::::::::P             OO:::::::::OO   K:::::::K    K:::::KE::::::::::::::::::::EM::::::M               M::::::M   OO:::::::::OO   N::::::N        N::::::N")
print("PPPPPPPPPP               OOOOOOOOO     KKKKKKKKK    KKKKKKKEEEEEEEEEEEEEEEEEEEEEEMMMMMMMM               MMMMMMMM     OOOOOOOOO     NNNNNNNN         NNNNNNN")
print("                                                        _____   __      __           _             ")
print("                                                       |  __ \  \ \    / /          (_)            ")
print("                                                       | |__) |  \ \  / ___ _ __ ___ _  ___  _ __  ")
print("                                                       |  ___/    \ \/ / _ | '__/ __| |/ _ \| '_ \ ")
print("                                                       | |         \  |  __| |  \__ | | (_) | | | |")
print("                                                       |_|          \/ \___|_|  |___|_|\___/|_| |_|")
#ASCII art generator: http://patorjk.com/software/taag/#p=testall&h=3&v=2&f=Crazy&t=P%20Version

user = ''
while user not in ['s','q']:
    user = input("Enter 's' to start the game or 'q' to quit:\n")
    if user == 's':
        continue
    elif user == 'q':
        sys.exit()
while user not in ['n','l']:
    user = input("Enter 'n' to start a new game or 'l' to load an old file:\n")
    #Load game
if user == 'l':
    raise NotImplementedError #ADD
    #New game
elif user == 'n':
        #INTRO
    print("POPLAR: Welcome to the world of Pokemon! My name is Professor Poplar, and I'll be your guide into this new and exciting adventure.")
    playername = input("First thing's first. What can I call you?\n")
    print("POPLAR: Nice to meet you " + playername + "! We are going to have a great adventure!")
    print("Are you familiar with Pokemon?")
    while user not in ['yes','no']:
        user = input("(enter 'yes' or 'no')\n")
    if user == 'no':
        print("POPLAR: Allow me to fill you in! Pokemon are creatures that share this world with us. You will find them all over the place, but they especially love to hide in tall grass.")
        print("You, " + playername + ", are a soon-to-be Pokemon trainer! You are about to begin a journey that will change your life.")
    elif user == 'yes':
        print("POPLAR: Well, then let's get right down to business!")

    while user not in ['Charmander','Bulbasaur','Squirtle','Florble the DESTROYER OF WORLDS, ETERNAL FUHRER, WITNESS OF ETERNITY, THE AEONS TORN']:
        print("\nWho would you like as your first Pokemon?")
        print("\nEnter 'Charmander' for the fire-type")
        print("Enter 'Bulbasaur' for the grass-type")
        print("Enter 'Squirtle' for the water-type")
        user = input("\n")
    print("You have chosen " + user + "!")
    print("\nPOPLAR: Excellent choice! " + user + " was always my favorite too.")
    if user == 'Charmander':
        Player.pokemon_list.append(PlayerCharmander)
        wild_pokemon.remove(PlayerCharmander)
    elif user == 'Bulbasaur':
        Player.pokemon_list.append(PlayerBulbasaur)
        wild_pokemon.remove(PlayerBulbasaur)
    elif user == 'Squirtle':
        Player.pokemon_list.append(PlayerSquirtle)
        wild_pokemon.remove(PlayerSquirtle)
    elif user == 'Florble the DESTROYER OF WORLDS, ETERNAL FUHRER, WITNESS OF ETERNITY, THE AEONS TORN':
        Player.pokemon_list.append(PlayerFlorble)
        wild_pokemon.remove(PlayerFlorble)
    Player.active_pokemon = Player.pokemon_list[0]
    print("Here, take some supplies! They'll help with your journey.\n")
    Player.money += 80
    print("You gained 80 munny!")
    PlayerPotion.amount += 2
    print("You gained 2 potions!")
    pokeball.amount += 4
    print("You gained 4 Pokeballs!")
    masterball.amount += 100
    print("\nAnd here's a little bonus while you're testing the game!")
    print("You gained 100 Master Balls!")
    print("\nPOPLAR: These pokeballs will help you catch pokemon in the wild!")
    print("I've taught you all I can. Go forth, " + playername + ", and become the best trainer of your generation!")
    print("Catch one of every Pokemon!")
    
#GAME MENU
while user != '6':
    print('-'*100)
    print("\nWHAT WOULD YOU LIKE TO DO?\n")
    print("1. Battle a Trainer")
    print("2. Wild Encounter")
    print("3. Shop")
    print("4. View Pokemon/Supplies")
    print("5. Multiplayer")
    print("6. Quit")
    print('-'*100)

    user = input("\n")
    
    if user == '1':
        trainernum = random.randint(0,len(trainerlist)-1)
        combat(trainerlist[trainernum])
    if user == '2':
        if wild_pokemon == []:
            print("You have caught all of the pokemon!")
        else:
            pokemonnum = random.randint(0,len(wild_pokemon)-1)
            catch(wild_pokemon[pokemonnum])
    if user == '3':
        shop()
    if user == '4':
        viewall()
    if user == '5':
        print("Multiplayer is currently under development.") #ADD
    if user == '6':
        sys.exit()

'''
TO DO:
- add multiplayer
- add level-up/experience
- add saving
- add evolution
- attack
- defense
- speed
- add story
- add "View Supplies"
- add sound

THINGS I LEARNED:
- classes
    Through this project, I have become very comfortable with classes. I remember when we first learned about them, I wondered how useful they would be.
    Now I understand how helpful they are not just in terms of capability, but for organization as well. 
- class interaction
    I understand the usefulness of having classes interact with each other. This allows for better organization and much more concise and readable code.
    I remember often looking at other people's code online and seeing something.something_else.a_third_thing and wondering what it was. Now I know :-).
- order
    I realized that the order in which you load classes and functions is especially important. Initially, I had some trouble initializing the Pokemon and Move classes
    because I was initializing the type class afterward. I realized that the former draws from the latter, so I needed to have the type class initialized first. 
- ASCII art generator
    I leared how to use an ASCII art generator and put it into Python. 
- ERROR CHECKING
    I had many more errors to sort out than I had anticipated. I have spent probably a solid hour or two at least just fixing bugs and errors. This did lead
    to a greater understanding of coding, but it helped me to realize the importance of frequent checking. If you have a bug and keep building, you may have to
    erase what you've coded since the bug if it draws from the bug. I have a new appreciation for debugging and will hopefully have more grace whenever
    I see a bug in a video game from now on. 
- organization
    With code even as large as this game's code, I realized how important it is to STAY ORGANIZED. Once I sorted all of my classes into separate modules and
    sorted my class initializations, it made my code so much easier to work with. Now I understand why video games have so many files; often less out of necessity
    and more out of workability and organization. 
- calling a function within itself
    We talked about this in class, but I have realized (especially in the viewall, viewpokemon, and shop functions how useul this can be. It saves cumulatively large amounts
    of coding to just be able to call a function from within the function itself.
- laying a solid foundation
    I realized the massive benefits of having a solid foundation for a game. For instance, I could have designed a game with 3 pokemon, but instead I designed one with
    however many pokemon are in the wild_pokemon list. Using variables instead of solid, immutable values is such a valuable tool. It allows me to add in new items
    or pokemon without much work, and that is definitely worth the extra work it takes to develop a solid and mutable foundation. 
- appreciation for game developers
    Making a game is hard. There are so many things to keep track of, so many variables, so many bugs to fix, and so many puzzle pieces to fit together.
    This has both helped video game developing feel like a possible task and given me an appreciation for the dedication and hard work it takes.
    Now I understand why it took 5 years to release Skyrim. With such a massive game, it really is a massive job!
'''
