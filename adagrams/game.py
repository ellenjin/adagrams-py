# testing
from random import randint

HAND_SIZE = 10
LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}
SCORE_CHART = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') : 1,
    ('D', 'G') : 2,
    ('B', 'C', 'M', 'P') : 3,
    ('F', 'H', 'V', 'W', 'Y') : 4,
    ('K') : 5,
    ('J', 'X') : 8,
    ('Q', 'Z') : 10
}

# Build a hand of 10 letters for the user
def draw_letters():
    letters = []
    total_pool = []
    
    for letter in LETTER_POOL:
        for how_many in range(LETTER_POOL[letter]):
            total_pool.append(letter)
    
    for i in range(HAND_SIZE):
        r = randint(0, len(total_pool) - 1)
        this_letter = total_pool.pop(r)
        letters.append(this_letter)

    return letters

# Input can be made from user's hand
def uses_available_letters(word, letter_bank):
    letter_bank_copy = []
    word = word.upper()

    for letter in letter_bank:
        letter_bank_copy.append(letter)

    for character in word:
        if not character in letter_bank_copy:
            return False
        letter_bank_copy.remove(character)
    return True

def score_word(word):
    word = word.upper()
    score = 0
    
    for character in word: 
        for key in SCORE_CHART:
            if character in key:
                score += SCORE_CHART[key]
                break 
    
    if len(word) >= 7:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    winning_word = ""
    high_score = 0
    highest = []

    for word in word_list:
        score = score_word(word)

        if score < high_score:
            continue
        if score > high_score:
            high_score = score
            highest.clear()
        highest.append((word, score))
    
    if len(highest) > 1:
        highest = tiebreaker(highest)
        return highest
    
    return highest[0]

def tiebreaker(word_list): # word_list passed in with elements being tuples (word, score)
    top_choices = []
    current_shortest_length = 11
    
    for word_score_pair in word_list: 
        current_length = len(word_score_pair[0])
        if current_length == 10:
            return word_score_pair
        if current_length < current_shortest_length:
            current_shortest_length = current_length
            top_choices.clear()
        top_choices.append(word_score_pair)

    return top_choices[0]