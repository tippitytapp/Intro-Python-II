from room import Room
from player import *
from items import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# create items

item = {
    "candle": Item("Candle", "Use this candle to find your way through"),
    "book": Item("Book", "Books have plenty of knowledge, but you are on a quest for treasure, so burn it to keep warm"),
    "sword": Item("Sword", "Use this overly large sword to help fight your enemies"),
    "dagger": Item("Dagger", "Daggers are easy to hide, so you can get closer to your enemies and then take them OUT!!"),
    "goldpiece": Item("Gold Piece", "This is the only gold you are going to find here!!! I mean... what?!?!?!"),
    "helmet": Item("Kevlar Helmet", "This will keep your head not dead"),
    "armour": Item("Chainmail", "No not those stupid chain emails we hate, this is armour for your body.... And dont ask me how i know about emails and its only 1196AD")
}

# Link items to rooms

room["foyer"].items = [item["goldpiece"], item["book"]]
room["overlook"].items = [item["dagger"], item["sword"]]
room["narrow"].items = [item["goldpiece"]]
room["treasure"].items = [item["book"]]


#
# Main
#
# print(room['outside'].n_to.description)
# print(room["outside"].name)
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Describe the help text

needhelp = '''     \n   How to play: \n\n     Type \'n\' to move north\n     Type \'s\' to move south\n     Type \'w\' to move west\n     Type \'e\' to move east\n     Type \'q\' at any time to quit\n     Type \'h\' for help '''

def start_game():
    print('                    <<<<<< WELCOME TO TREASURE TRAIL >>>>>>\n')
    player = Player(name = input('                             What shall I call you?  '), current_room = room['outside'], items = [item["helmet"], item["armour"]])
    print('For help, type \'h\'')
    print(player)

    grabdrop = input(f'This room has: \n {player.current_room.printitems()} \n In your inventory you have:\n {player.printitems()} \n If you would like to pick up something from the room, type get [item], if you would like to leave some of your items behind, type drop [item], if you wish to continue without modifying your inventory, not recommened, but ok, just type ok')
    # while not(player.in_treasure):
    # room_items = player.current_room.printitems()
    while not(player.in_treasure):
        gamer_input = input( "\nWhich direction would you like to move?  ")
        print('\n')
        if gamer_input == 'q':
            print('\n     !! Thanks for playing !!\n')
            exit()
        if gamer_input == 'h':
            print(needhelp)
        if gamer_input == 'n':
            try:
                player.current_room = player.current_room.n_to
                if player.current_room.name == "Treasure Chamber":
                    print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                    print('You have found the treasure')
                    won_game = input('Would you like to play again? Type y for yes, n for no')
                    if won_game == 'y':
                        start_game()
                    else:
                        print('\n     !! Thanks for playing !!\n')
                        exit()
                else:
                    print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                    grabdrop = input(f'This room has: \n {player.current_room.printitems()} \n In your inventory you have:\n {player.printitems()} \n If you would like to pick up something from the room, type get [item], if you would like to leave some of your items behind, type drop [item], if you wish to continue without modifying your inventory, not recommened, but ok, just type ok')
                    # room_items
                    gamer_input
            except:
                print("There is no room to the north")
                gamer_input
        if gamer_input == 's':
            try:
                player.current_room = player.current_room.s_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop
                gamer_input                
            except:
                print('There is no room to the south.')
                gamer_input        
        if gamer_input == 'e':
            try:
                player.current_room = player.current_room.e_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop
                gamer_input                 
            except: 
                print('There is no room to the east.')
                gamer_input
        if gamer_input == 'w':
            try:
                player.current_room = player.current_room.w_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                grabdrop
                gamer_input
            except:
                print('There is no room to the west.')
                gamer_input                      

start_game()