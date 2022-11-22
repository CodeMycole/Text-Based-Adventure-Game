# Mycole Eversole

# import time for introduction and final battle (You'll see :)  )
import time

# dictionary of rooms, directions, and items
rooms = {
    'limbo': {'south': 'lust', 'character': ''},
    'lust': {'north': 'limbo', 'east': 'gluttony', 'character': 'gowther'},
    'gluttony': {'north': 'greed', 'east': 'fraud', 'south': 'heresy', 'west': 'lust', 'character': 'merlin'},
    'greed': {'east': 'anger', 'south': 'gluttony', 'character': 'ban'},
    'anger': {'west': 'greed', 'character': 'meliodas'},
    'heresy': {'north': 'gluttony', 'east': 'violence', 'character': 'diane'},
    'violence': {'west': 'heresy', 'character': 'escanor'},
    'fraud': {'west': 'gluttony', 'north': 'treachery', 'character': 'king'}
}

# Dictionary of each room and it's matching circle of hell
room_circle = {
    'limbo': 'First Circle',
    'lust': 'Second Circle',
    'gluttony': 'Third Circle',
    'greed': 'Fourth Circle',
    'anger': 'Fifth Circle',
    'heresy': 'Sixth Circle',
    'violence': 'Seventh Circle',
    'fraud': 'Eighth Circle',
    'treachery': 'Ninth Circle'
}


# Creating player as an object to track room and characters obtained
class Player:
    room = 'limbo'
    characters = []


# Introduction for the game explaining narrative and controls Adding time so all the text doesn't appear at once
def game_intro():
    context = "Congratulations! You're dead and have been reincarnated into the anime world of " \
              "The Seven Deadly Sins! \nUnfortunately, there was a slight hick-up and you ended up " \
              "in a place called purgatory. \nIts the deepest part of hell...\n \n"

    hope = "Don't worry though! There is a way out! \nAll you have to do is gather all seven members of the " \
           "Seven Deadly sins, \nTraveling through all of Dante's nine circles of hell, \n" \
           "and defeat the group The Ten Commandments who wait for you at the gate in the ninth circle!\n \n"

    good_luck = "Try not to find them before you get all the members, otherwise you'll die \nGood Luck!\n \n"

    instructions = "Anime Themed Text Adventure Game \n \nGather all members of the Seven Deadly Sins, or die.\n" \
                   "Move commands: go north, go south, go east, go west\n" \
                   "Add character to party: get 'character'"

    for char in context:
        print(char, end='')
        time.sleep(0.015)
    time.sleep(3)

    for char in hope:
        print(char, end='')
        time.sleep(0.015)
    time.sleep(3)

    for char in good_luck:
        print(char, end='')
        time.sleep(0.015)
    time.sleep(3)

    print('_' * 50)

    print(instructions)
    print()

# Function for moving rooms
def move_rooms(player_choice):

    # Since players move involves go, we cut out the go
    direction = player_choice[3:]

    # We see if the direction is a way they can go by accessing our dictionary, and if so, we move to that room
    if direction in rooms[Player.room]:
        Player.room = rooms[Player.room][direction]

    # Otherwise we tell the user they can't and stay in the same room
    else:
        print("You can't move that way")


# Function for getting character to join party
def get_character(player_choice):

    # Again we start by removing the 'get' part of the player move
    character = player_choice[4:]

    # We then see if what they typed in is the character in that room, and if it is, add it to player party
    if character == rooms[Player.room]['character']:
        Player.characters.append(character)
        # Then remove the character from the room (dictionary)
        rooms[Player.room]['character'] = ''

    # This is so if the player tries to get the character again, they get a custom message
    elif character in Player.characters:
        print('You already collected {}!'.format(character.capitalize()))

    # Otherwise it will tell them there is nothing left to get in this room
    else:
        print("That is not an item in this room!")


# The part that makes the game work
def game_play():
    # once the game runs the status is in progress, and will continue to be until our while loop closes
    game_status = 'in progress'

    # Have the game run until the status changes to win or lose
    while game_status != 'won' and game_status != 'lost':

        # Tells the player where they are, and what characters they have found.
        print('You are in the {}: {}'.format(room_circle[Player.room], Player.room.capitalize()))
        print('Characters in party: {}'.format(Player.characters))

        # Checks to see if there is a character that has not been gathered in the current room
        if rooms[Player.room]['character']:
            print('You see {}'.format(rooms[Player.room]['character']).capitalize())
        print('-' * 30)

        # Asks the user to enter there move, either get item, or go direction
        choice = input('Enter your move: \n').lower()

        # This checks if the movement is valid, if it starts with go, we run the change rooms. if it starts with get,
        # get item, else invalid entry. The functions themselves will say if the get or go is not right.
        if choice[:2] == 'go':
            move_rooms(choice)
            print()
        elif choice[:3] == 'get':
            get_character(choice)
            print()
        else:
            print('invalid input')
            print()
            time.sleep(2)

        if Player.room == 'treachery':

            # If the player collected all 7 sins, they win the game when they get to treachery
            if int(len(Player.characters)) == 7:
                print("You are now in the ninth circle: Treachery!")
                print()
                print("You come face to face with The 10 Commandments!")
                print("The battle rages!!")
                time.sleep(5)
                print('You and the Seven Deadly Sins successfully defeated The 10 Commandments!')
                print('YOU WIN!')
                game_status = 'won'
            else:
                # If not then they lose!
                print("You are now in the ninth circle: Treachery!")
                print()
                print("You come face to face with The 10 Commandments!")
                print("The battle rages!!")
                time.sleep(5)
                print("OH NO!! You didn't collect all seven sins before finding the 10 commandments!")
                print("You died! Game over")
                game_status = 'lost'


# runs everything together
def main():
    game_intro()
    game_play()


main()
