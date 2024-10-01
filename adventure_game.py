# SP23-BAI-047

import json

# Defining rooms and their properties
rooms = {
    'Entrance': {
        'description': 'You are at the entrance of an ancient, mysterious castle.',
        'exits': {'north': 'Grand Hall'},
        'items': []
    },
    'Grand Hall': {
        'description': 'You are in the Grand Hall. There are doors leading to the Library and the Basement.',
        'exits': {'south': 'Entrance', 'east': 'Library', 'west': 'Basement', 'north': 'Kitchen'},
        'items': ['torch']
    },
    'Kitchen': {
        'description': 'You are in the kitchen. The smell of freshly baked bread fills the air, but the room feels eerily quiet. There is a pantry to the north.',
        'exits': {'south': 'Grand Hall'},
        'items': ['bread', 'knife'],
        'riddle': 'So beautiful and cold,\nSo young and yet so old,\nAlive but always dead,\nStill hungry when has fed,\nWill die if it is bled,\nOr you cut off its head.',
        'answer': 'vampire',
        'pantry_locked': True
    },
    'Library': {
        'description': 'You are in a dusty old library filled with ancient books. You see a strange bookshelf that has only one book in it.',
        'exits': {'west': 'Grand Hall'},
        'items': ['book', 'pen'],
        'riddle': 'They belong to me; they belong to you;\nThey can make you feel happy or make you feel blue;\nThey never end until the day you do.',
        'answer': 'thoughts',
        'puzzle_solved': False
    },
    'Basement': {
        'description': 'You are in a dark and damp basement. A locked door leads further down.',
        'exits': {'east': 'Grand Hall', 'down': 'Dungeon'},
        'door_is_locked': True,
        'items': ['key', 'rope']
    },
    'Dungeon': {
        'description': 'You have entered the Dungeon. It\'s cold and there\'s a feeling of dread. You see a large dog tied to a post with a thick rope. The dog growls menacingly at you, clearly unhappy with your presence. It’s clear the dog doesn’t trust you... yet.',
        'exits': {'up': 'Basement'},
        'items': ['dog'],
        'dog_is_friend': False,
        'dog_is_tied': True
    }
}

current_room = 'Entrance'
inventory = []
game_won = False
game_lost = False

def show_overview():
    print("""
Welcome to The Mysterious Castle Adventure!

Game Overview:
--------------
You are trapped inside an ancient castle and must find your way out by exploring different rooms, collecting useful items, solving puzzles, and eventually escaping the castle.

How to Play:
------------
1. **Navigation:** 
   - Move between rooms using commands like:
     - 'go north', 'go south', 'go east', 'go west', 'go down', 'go up'

2. **Looking Around:**
   - Examine your surroundings by using:
     - 'look': Describes the current room and any available items.
     - 'examine <item>': Look closely at an item or object in the room to gather more information. Write the name of item instead of <item>.

3. **Inventory Management:**
   - Pick up and manage items with:
     - 'take <item>': Collect an item from the current room. Write the name of item instead of <item>.
     - 'drop <item>': Drop an item you are carrying. Write the name of item instead of <item>.
     - 'inventory': Check the items in your inventory.

4. **Using Items:**
   - Interact with the environment using your items:
     - 'use <item>': Use an item in your inventory to interact with the environment or solve a puzzle. Write the name of item instead of <item>.

5. **Solving Puzzles:**
   - Solve riddles or unlock mechanisms by using the appropriate items:
     - 'solve riddle': Engage with puzzles that require solving (e.g., bookshelves or pantry doors).
     - Some items and objects will need to be examined to understand their function.

6. **Game Progress:**
   - Save and load your progress:
     - 'save': Save your current progress to return later.
     - 'load': Load a previously saved game.
     - 'quit': Exit the game.

Game Hints:
-----------
- Be thorough in examining each room. Some rooms hide puzzles or essential items you need to progress.
- Use your inventory wisely. Not every item is useful in all rooms.
- Pay attention to clues given in item descriptions to solve puzzles.
- The ultimate goal is to escape the castle by solving the mysteries within!

Good luck on your adventure!
""")

# Function to display the room description
def look():
    room = rooms[current_room]
    print(room['description'])
    if room['items']:
        print('You see the following items here:', ', '.join(room['items']))
    for direction, next_room in room['exits'].items():
        print(f'To {direction}, you see a door to {next_room}.')

# Handle player movement between rooms
def move(direction):
    global current_room
    room = rooms[current_room]
    if direction in room['exits']:
        # Check if the door is locked before allowing movement
        if direction == 'down' and current_room == 'Basement' and room['door_is_locked']:
            print('The door is locked. You have to unlock it first.')
        else:
            current_room = room['exits'][direction]
            print(f'You go to {direction}.')
            look()  # Automatically look around after moving
    else:
        print(f"You can't go to {direction}.")

# Function to display inventory
def show_inventory():
    if inventory:
        print('Your inventory contains:', ', '.join(inventory))
    else:
        print('Your inventory is empty.')

# Function to solve riddle
def solve_riddle():
    global game_won
    if current_room == 'Library':
        answer = input(rooms['Library']['riddle'])
        while rooms['Library']['answer'] not in answer.lower():
            answer = input('That\'s not the correct answer.Please try again. (Enter q if you dont want to solve it.)').lower()
            if answer == 'q':
                print('You dont want to solve the riddle for now.')
                break
        else:
            rooms['Library']['puzzle_solved'] = True
            print('Correct! The book is unlocked. You can take it.')

    elif current_room == 'Kitchen':
        print(rooms['Kitchen']['riddle'])
        answer = input('Solve the riddle: ')
        while rooms['Kitchen']['answer'] not in answer.lower():
            answer = input('That\'s not the correct answer.Please try again. (Enter q if you dont want to solve it.)').lower()
            if answer == 'q':
                print('You dont want to solve the riddle for now. Strange symbols disappear on the pantry door.')
                break
        else:
            rooms['Kitchen']['pantry_locked'] = False
            print("Correct! The pantry door creaks open, revealing a secret passage. You step through and escape the castle! Congratulations!!")
            game_won = True

    else:
        print('No riddle to solve here.')

# Examine specific items in the current room for more details
# Some items will give clues or hints
def examine(item):
    room = current_room    
    if item == 'book' and not rooms['Library']['puzzle_solved']:
        print("The book is inside the locked bookshelf, but you can read the title: 'Secrets of the Castle: A Guide to the Creatures Within.'")
    elif item == 'bookshelf' and not rooms['Library']['puzzle_solved']:
        print('You see the bookshelf is locked. \n"Solve riddle to unlock it." is written on bookshelf.')
    elif item == 'pantry' and current_room == 'Kitchen':
        print("The pantry door is locked. You notice a strange mark on the door, shaped like a dog’s paw.")
    else:
        print(f'nothing to examine about {item}.')

def use(item):
    global game_lost, game_won
    room = rooms[current_room]

    if item in inventory:

        # using knife to untie the dog.
        if item == 'knife' and current_room == 'Dungeon' and room['dog_is_tied']:
            print('You use knife untie the dog.')
            rooms['Dungeon']['dog_is_tied'] = False
            if not room['dog_is_friend']:
                print('Ohhh no, dog attacks you because you failed to calm him.')
                game_lost = True
            else:
                print('Dog now looks at you as a friend.')

        # using key to unclock the door of dungeon
        elif item == 'key' and current_room == 'Basement':
            print('You used the key to unlock the door to the dungeon.')
            rooms[current_room]['door_is_locked'] = False

        # using bread to the dog.
        elif item == 'bread' and current_room == 'Dungeon':
            print('You offer the bread to the dog. He hesitates for a moment, then sniffs it before eating it hungrily. He seems to calm down.')
            room['dog_is_friend'] = True   # dog now trusts the player and see him as a friend.
        
        # Using the book 
        elif item == 'book':
            print("The book is unlocked and you read the title: 'Secrets of the Castle: A Guide to the Creatures Within.'")
            print("There is an inscription on the cover: 'Only those who understand the creatures of this castle will find their way out.'")
            print("You notice faint text beneath the title: 'To earn the trust of the hound, offer him a taste of kindness.'")
            
        # Using the dog's paw on the pantry
        # used 'dog' in item, bcz player can use command: [use dog's paw]
        elif 'dog' in item and current_room == 'Kitchen':
            print("You place the dog's paw on the mark. Strange symbols appear on the pantry door. The symbols become clear and form a riddle.")
            solve_riddle()           
        # using bread to the dog.
        elif item == 'torch' and current_room == 'Basement':
            print('You use torch to illuminate the dark basement.')

        else:
            print(f'You cannot use {item} here.')

    else:
        print(f'You don\'t have {item} in inventory.')  
  
# Allow the player to take items from the room and add them to inventory
def take(item):
    room = rooms[current_room]
    if item in room['items']:
        # Prevent the player from taking certain items (e.g., locked book, tied dog)
        if item == 'dog' and room['dog_is_tied']:
            print('Dog is tied. You can not take it.')
        elif item == 'book' and not room['puzzle_solved']:
            print('You can\'t take book. The bookshelf is locked. (Hint: Try to examine the bookshelf).')
        else:
            room['items'].remove(item)
            inventory.append(item)
            print(f'You have taken the {item}.')
    else:
        print(f'There is no {item} to take in {current_room}.')

def drop(item):
    if item in inventory:
        inventory.remove(item)
        rooms[current_room]['items'].append(item)
        print(f'{item} has been successfully dropped.')
    else:
        print(f'No {item} found in inventory.')

# Load a previously saved game state from a file
def load():
    global current_room, inventory
    try:
        with open('savegame.json', 'r') as file:
            data = json.load(file)
            current_room = data['current_room']
            inventory = data['inventory']
            print("Game loaded.")
            look()
    except FileNotFoundError:
        print("No saved game found.")

# Function to save the game state
def save():
    with open('savegame.json', 'w') as file:
        json.dump({'current_room': current_room, 'inventory': inventory}, file)
    print("Game saved.")

# Main game loop handling player input and game progression
# Continue looping until the player wins or loses the game
def main():
    show_overview()
    look()

    print('What would you like to do?')

    while not game_won and not game_lost:
        command = input('\n\n> ').lower().split()
        if len(command) == 0:
            continue
        if command[0] == 'quit':
            print('Exiting the game. Thanks for playing.')
            break

        if command[0] == 'go' and len(command) > 1:
            move(command[1])
        elif command[0] == 'use' and len(command) > 1:
            use(command[1])
        elif command[0] == 'examine' and len(command) > 1:
            examine(command[1])
        elif command[0] == 'take' and len(command) > 1:
            take(command[1])
        elif command[0] == 'drop' and len(command) > 1:
            drop(command[1])
        elif command[0] == 'solve' and len(command) > 1:
            solve_riddle()
        elif command[0] == 'look':
            look()
        elif command[0] == 'inventory':
            show_inventory()
        elif command[0] == 'save':
            save()
        elif command[0] == 'load':
            load()
        else:
            print('Sorry, I\'m unable to understand. Please re-enter your command.')
            
if __name__ == "__main__":
    main()