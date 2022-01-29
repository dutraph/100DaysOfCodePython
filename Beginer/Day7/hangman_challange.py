from random import choice
import lists


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


print(logo)
chosen_word = choice(lists.word_list)
display = []
lives = 6

for _ in range(len(chosen_word)):
    display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    if lives == 0:
        print("Last Try")
    else:
        print(f"Number of tries {lives}")
    guess = input("guess a letter: ").lower()
    if guess in display:
        print(f"You've already tried this one: {guess}, try another!")
    for position in range(len(chosen_word)):

        if chosen_word[position] == guess:
            display[position] = guess
            print(lists.stages[lives])

    if guess not in chosen_word:
        lives -= 1
        print(lists.stages[lives])
        if lives == 0 and "_" in display:
            print("Game Over!")
            print(f"The word was {chosen_word}")
            end_of_game = True

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

