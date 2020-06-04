from room import Room
from player import *
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

needhelp = '''     \n   How to play: \n\n     Type \'n\' to move north\n     Type \'s\' to move south\n     Type \'w\' to move west\n     Type \'e\' to move east\n     Type \'q\' at any time to quit\n     Type \'h\' for help '''

def start_game():
    print('                    <<<<<< WELCOME TO TREASURE TRAIL >>>>>>\n')
    player = Player(name = input('                             What shall I call you?  '), current_room = room['outside'])
    print(player)
    print(needhelp)

    # while not(player.in_treasure):
    while not(player.in_treasure):
        gamer_input = input( "\nWhich direction would you like to move?  ")
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
                    gamer_input
            except:
                print("There is no room to the north")
                gamer_input

        if gamer_input == 's':
            try:
                player.current_room = player.current_room.s_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                gamer_input                
            except:
                print('There is no room to the south.')
                gamer_input        
        if gamer_input == 'e':
            try:
                player.current_room = player.current_room.e_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                gamer_input                 
            except: 
                print('There is no room to the east.')
                gamer_input
        if gamer_input == 'w':
            try:
                player.current_room = player.current_room.w_to
                print(f' You are now in {player.current_room.name}, {player.current_room.description}')
                gamer_input
            except:
                print('There is no room to the west.')
                gamer_input                      

start_game()