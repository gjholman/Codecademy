letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create dictionary that maps the letters to points
letters_to_points = {key:value for key, value in zip(letters, points)}

# Add space / zero case to dictionary
letters_to_points[" "] = 0

player_to_words = {'player1' : ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}


def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points[letter]  
  return point_total


def player_to_points():
  for player, word_list in player_to_words.items():
    player_points = 0
    for word in word_list:
      player_points += score_word(word.upper())
    print(player + ' has ' + str(player_points) + ' points')

    
def play_word(player, word):
  player_to_words[player].append(word)
  
def update_point_totals():
  player_to_points()

update_point_totals()

play_word('player1', "UBIQUITOUS")

update_point_totals()


# This is following the codecademy path, although I would not organize my script this way
# I would make a separate function for determining an individual's score,
# and I would 
