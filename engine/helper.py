
import re
def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def remove_words (input_strings, words_to_remove):

    words = input_strings.split() #split the input string into a list of words
    
    #split the input string into a list of words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    #remove Unwanted words from the list
    resulted_string = ' '.join(filtered_words)

    return resulted_string

    