def is_word_guessed(secret_word, letters_guessed):
    secret_word = secret_word.lower()
    result = True
    is_in_both = True
    for element in letters_guessed:
        element = element.lower()
        for word in secret_word:
            result = is_in_both
            if element == word:
                is_in_both = True
            else:
                is_in_both = False
            result += is_in_both
    return secret_word, letters_guessed, result
a = is_word_guessed('word', ['W', 'o', 'N', 'D'])
print(a)
 
            
    
              