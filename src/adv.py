import textwrap
from room import Room
from player import Player
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

new_player = Player('Player1', room['treasure'])
# Player name
pl_name = new_player.name
# Current Room
current_room = new_player.current_room
# Room Name
rm_name = current_room.name
rm_description = textwrap.fill(text=current_room.description, width=30)
print(f"(Room Name:\n {rm_name},\n Room Descr:\n {rm_description})")

user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")


def is_valid_input(user_input):
    print(f"\n68 {user_input}\n")
    go_to = f"{user_input}_to"

    if hasattr(current_room, go_to):
        to_room = getattr(current_room, go_to)
        print('\nHeading to room\n', to_room)
        return to_room
    else:
        print(f"{user_input} is not a valid direction")
        user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")
        is_valid_input(user_input)


def print_room(room):
    room_details = f"Room: {room.name}\nDescription: {room.description}"
    return room_details


while user_input != 'q':
    if user_input in ['n', 's', 'e', 'w']:
        rm_name = is_valid_input(user_input)
        room_details = print_room(rm_name)
        print(f"{room_details}\n")
        user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")
        rm_name = is_valid_input(user_input)
        print(f"You're currently in room {rm_name}\n")
        # print('')
        break
    else:
        print(f"{user_input} is not a valid direction")
        user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")

if user_input == 'q':
    print('Goodbye')
