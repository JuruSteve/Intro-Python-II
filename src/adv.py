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

new_player = Player('Player1', room['outside'])
# Player name
pl_name = new_player.name
# Current Room
current_room = new_player.current_room
# Room Name
rm_name = current_room.name
rm_description = textwrap.fill(text=current_room.description, width=70)
print(f"\n\n(Room Name:\n {rm_name}\nRoom Descr:\n{rm_description})\n")

user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")

while user_input != 'q':
    go_to_direction = f"{user_input}_to"
    # if current_room has go_to_direction(s_to) attribute
    if hasattr(current_room, go_to_direction):
        # get the attribute
        to_room = getattr(current_room, go_to_direction)
        print('to_room', to_room)
        # if the attr is == None, prompt user to enter correct direction
        if to_room == None:
            to_room = go_to_direction
            print(f"Wrong way! {user_input} is not a valid direction.")
            user_input = input("Enter a direction (n, s, e, w, or q (quit)): ")
        # Else if attr exists update room
        else:
            rm_name = to_room
            # current room updated
            current_room = rm_name
            if hasattr(rm_name, 'description'):
                cr_description = getattr(current_room, 'description')
                print(f"Welcome to room {rm_name}")
                print('Description:', cr_description)
                user_input = input(
                    "Enter a direction (n, s, e, w, or q (quit)): ")
            else:
                print('Room has no further directions')
    else:
        print('False', rm_name)
        break
if user_input == 'q':
    print('Goodbye')
