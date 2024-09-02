from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

from django.shortcuts import render
import random
import string

# Step 2: Define the List of Football Words
words = [
    "GOALKEEPER", "DEFENDER", "MIDFIELDER", "STRIKER", 
    "OFFSIDE", "PENALTY", "CORNER", "DRIBBLE", "TACKLE", "KICKOFF"
]

# Step 3: Create an Empty Grid
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

# Step 5: Function to Place Words on the Grid
def place_word(grid, word):
    word_length = len(word)
    placed = False
    
    while not placed:
        direction = random.choice(directions)
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        
        end_row = row + direction[0] * word_length
        end_col = col + direction[1] * word_length
        
        if 0 <= end_row < grid_size and 0 <= end_col < grid_size:
            # Check if the word can be placed
            can_place = True
            for i in range(word_length):
                new_row = row + direction[0] * i
                new_col = col + direction[1] * i
                if grid[new_row][new_col] not in (' ', word[i]):
                    can_place = False
                    break
            
            if can_place:
                for i in range(word_length):
                    new_row = row + direction[0] * i
                    new_col = col + direction[1] * i
                    grid[new_row][new_col] = word[i]
                placed = True

# Step 6: Place All Words on the Grid
for word in words:
    place_word(grid, word)

# Step 7: Fill the Remaining Empty Spaces
for row in range(grid_size):
    for col in range(grid_size):
        if grid[row][col] == ' ':
            grid[row][col] = random.choice(string.ascii_uppercase)




# Django View to Render the Grid
def index(request):
    return render(request, 'index.html', {'grid': grid, 'words': words})

# New view to handle word checking
def check_word(request):
    if request.method == 'POST':
        selected_word = request.POST.get('word').upper()
        reverse_selected_word = selected_word[::-1]

        # Check if the selected word or its reverse exists in the word list
        if selected_word in words or reverse_selected_word in words:
            return JsonResponse({'status': 'found', 'word': selected_word})
        else:
            return JsonResponse({'status': 'not_found', 'word': selected_word})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
