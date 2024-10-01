# **The Mysterious Castle Adventure**
## **SP23-BAI-047**
## **Game Overview**
**The Mysterious Castle Adventure** is a Python-based text adventure game where you find yourself trapped in an ancient, mysterious castle. Your goal is to explore different rooms, collect items (keep in mind that not every item is necessary to pick up), solve riddles, and escape. Along the way, you must interact with objects, solve puzzles, and befriend a dog to unlock a secret passage that leads to freedom.

## **How to Play**

### **1. Navigation:**
Use the following commands to move between rooms:
- `go north`
- `go south`
- `go east`
- `go west`
- `go up`
- `go down`

### **2. Looking Around:**
To get a description of your current room and see the items available, use:
- `look`

To examine specific items or objects in the room, use:
- `examine <item>` (replace `<item>` with the name of the item)

### **3. Managing Items:**
To collect or drop items, use the following commands:
- `take <item>`: To collect an item from the room.
- `drop <item>`: To drop an item from your inventory.
- `inventory`: To see the list of items you're currently holding.

### **4. Using Items:**
To interact with items, use:
- `use <item>`: To use an item from your inventory.

### **5. Solving Puzzles:**
Some rooms contain riddles or puzzles. Use the command:
- `solve riddle`: To solve a puzzle related to an object, such as the pantry or bookshelf.
- Pay attention to the hints provided in item descriptions or riddle prompts.

### **6. Game Progress:**
You can save and load your game progress with these commands:
- `save`: Save your current game state.
- `load`: Load a previously saved game.
- `quit`: Exit the game.

## **Special Features**

1. **Puzzles and Riddles**: The game features interactive riddles that you must solve to progress. Each room may have items or objects tied to a puzzle, and solving the riddle opens new pathways or unlocks key items.
   
2. **Dynamic Interactions**: You must untie a dog in the dungeon by befriending it with bread before it will trust you enough to help. This adds a layer of strategy and interaction beyond simple exploration.

3. **Item Usage**: Various items such as a key, bread, and a knife are essential for progressing through the game. Items can be used to solve puzzles, unlock doors, and calm the dog.

---


### **Complete Gameplay Walkthrough**

```
> look
You are at the entrance of an ancient, mysterious castle.
To the north, you see a door to the Grand Hall.

> go south
You can't go to south.

> go north
You are in the Grand Hall. There are doors leading to the Library and the Basement.
You see the following items here: torch

> take torch
You have taken the torch.

> go east
You are in a dusty old library filled with ancient books. You see a strange bookshelf that has only one book in it.
You see the following items here: book, pen

> take book
You can’t take the book. The bookshelf is locked. (Hint: Try to examine the bookshelf).

> examine bookshelf
You see the bookshelf is locked. "Solve riddle to unlock it" is written on the bookshelf.

> solve riddle
They belong to me; they belong to you;
They can make you feel happy or make you feel blue;
They never end until the day you do.

> memories
That’s not the correct answer. Please try again. (Enter q if you don’t want to solve it.)

> q
You don’t want to solve the riddle for now.

> go west
You are in the Grand Hall. There are doors leading to the Library and the Basement.

> go west
You are in the Basement. A locked door leads further down.
You see the following items here: key, rope

> take key
You have taken the key.

> go down
The door is locked. You have to unlock it first.

> use key
You used the key to unlock the door to the Dungeon.

> go down
You have entered the Dungeon. It’s cold and there’s a feeling of dread. You see a large dog tied to a post with a thick rope.

> use bread
You don’t have bread in your inventory.

> go up
You are in the Basement.

> go east
You are in the Grand Hall.

> go north
You are in the kitchen. The smell of freshly baked bread fills the air, but the room feels eerily quiet. There is a pantry to the north.
You see the following items here: bread, knife

> take bread
You have taken the bread.

> go down
You can't go to down.

> go south
You are in the Grand Hall.

> go west
You are in the Basement.

> go down
You have entered the Dungeon. It’s cold and there’s a feeling of dread. You see a large dog tied to a post with a thick rope.

> use bread
You offer the bread to the dog. He hesitates for a moment, then sniffs it before eating it hungrily. He seems to calm down.

> use knife
You use the knife to untie the dog.
Dog now looks at you as a friend.

> go up
You are in the Basement.

> go east
You are in the Grand Hall.

> go north
You are in the kitchen. The smell of freshly baked bread fills the air, but the room feels eerily quiet. There is a pantry to the north.

> examine pantry
The pantry door is locked. You notice a strange mark on the door, shaped like a dog’s paw.

> use dog’s paw
You place the dog's paw on the mark. Strange symbols appear on the pantry door. The symbols become clear and form a riddle.

> solve riddle
So beautiful and cold,
So young and yet so old,
Alive but always dead,
Still hungry when has fed,
Will die if it is bled,
Or you cut off its head.

> ghost
That’s not the correct answer. Please try again. (Enter q if you don’t want to solve it.)

> vampire
Correct! The pantry door creaks open, revealing a secret passage. You step through and escape the castle! Congratulations!!
```


## **How to Run the Game**

1. **Clone or download** the game repository from GitHub.
   ```bash
   git clone https://github.com/your-username/mysterious-castle-adventure.git
   ```

2. Navigate to the game folder.
   ```bash
   cd mysterious-castle-adventure
   ```

3. Run the game using Python.
   ```bash
   python3 game.py
   ```

4. Follow the game instructions to explore, solve puzzles, and escape the castle.

