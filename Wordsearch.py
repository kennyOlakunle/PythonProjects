# Step 1: Understand the Requirements
# Before we start coding, let's outline what we want:

# Word List: A list of 10 football-related words.
# Grid Size: Decide on a grid size, such as 10x10 or 15x15.
# Word Placement: Words can be placed horizontally, vertically, diagonally, and in reverse.
# Fill Empty Spaces: Fill remaining grid spaces with random letters.
# User Interaction: Provide a way for users to find and highlight words.
# Display the Grid: Print the grid to the console or create a GUI.

# Step 2: Prepare the Word List
# Choose 10 football-related words. For example:

# GOALKEEPER
# DEFENDER
# MIDFIELDER
# STRIKER
# OFFSIDE
# PENALTY
# CORNER
# DRIBBLE
# TACKLE
# KICKOFF
# Ensure all words are uppercase for consistency.

# Step 3: Determine Grid Size
# Choose a grid size that can accommodate all words comfortably. A 15x15 grid should work well for 10 words. 
# However, you may adjust the grid size based on the length of your words and desired difficulty.

# Step 4: Create the Grid
# Create an empty 2D list (list of lists in Python) to represent the grid. 
# Initialize it with a placeholder character, such as an underscore _ or a space ' '.



# Step 1: Import Necessary Libraries
import random
import string


# Step 2: Define the List of Football Words
words = [
    "GOALKEEPER", "DEFENDER", "MIDFIELDER", "STRIKER", 
    "OFFSIDE", "PENALTY", "CORNER", "DRIBBLE", "TACKLE", "KICKOFF"
]



# Create an Empty Grid
grid_size = 15
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]



# Step 4: Define Directions for Word Placement
directions = [
    (0, 1),  # Horizontal, left to right
    (1, 0),  # Vertical, top to bottom
    (1, 1),  # Diagonal, top left to bottom right
    (0, -1), # Horizontal, right to left
    (-1, 0), # Vertical, bottom to top
    (-1, -1),# Diagonal, bottom right to top left
    (1, -1), # Diagonal, top right to bottom left
    (-1, 1)  # Diagonal, bottom left to top right
]



# Function to Place Words on the Grid

def place_word(grid, word):
    word_length = len(word)
    placed = False

    while not placed:
        # Randomly select a direction
        direction = random.choice(directions)
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)

        # Check if word fits in the selected direction
        end_row = row + direction[0] * (word_length - 1)
        end_col = col + direction[1] * (word_length - 1)

        if end_row < 0 or end_row >= grid_size or end_col < 0 or end_col >= grid_size:
            continue

        # Check if word overlaps with existing letters
        overlap = False
        for i in range(word_length):
            cell = grid[row + i * direction[0]][col + i * direction[1]]
            if cell != ' ' and cell != word[i]:
                overlap = True
                break

        if not overlap:
            # Place the word on the grid
            for i in range(word_length):
                grid[row + i * direction[0]][col + i * direction[1]] = word[i]
            placed = True



# Step 5: Place Words on the Grid
for word in words:
    place_word(grid, word)



# Step 6: Fill Empty Spaces with Random Letters
for row in range(grid_size):
    for col in range(grid_size):
        if grid[row][col] == ' ':
            grid[row][col] = random.choice(string.ascii_uppercase)



# Step 7: Display the Grid

for row in grid:
    print(' '.join(row))


