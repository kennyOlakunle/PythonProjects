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
