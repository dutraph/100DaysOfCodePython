def win():
    print('''
                _.--.
            _.-'_:-'||
        _.-'_.-::::'||
   _.-:'_.-::::::'  ||
 .'`-.-:::::::'     ||
/.'`;|:::::::'      ||_
||   ||::::::'     _.;._'-._
||   ||:::::'  _.-!oo @.!-._'-.
|'.  ||:::::.-!()oo @!()@.-'_.|
'.'-;|:.-'.&$@.& ()$%-'o.'U|||
  `>'-.!@%()@'@_%-'_.-o _.|'||
   ||-._'-.@.-'_.-' _.-o  |'||
   ||=[ '-._.-U/.-'    o |'|||
   || '-.]=|| |'|      o  |'||
   ||      || |'|        _| ';
   ||      || |'|    _.-'_.-'
   |'-._   || |'|_.-'_.-'
    '-._'-.|| |' `_.-'
        '-.||_/.-'
    ''')


def game_over():
    print('''
         _.--""--._
        /  _    _  |
     _  ( (_\  /_) )  _
    { \._\   /\   /_./ }
    /_"=-.}______{.-="_|
     _  _.=("""")=._  _
    (_'"_.-"`~~`"-._"'_)
     {_"            "_}
    ''')


def fire():
    print('''
                   (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ''')


def beast():
    print('''
    
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
    
    ''')


def fish():
    print('''
               .'|_.-
         .'  '  /_
      .-"    -.   '>
   .- -. -.    '. /    /|_
  .-.--.-.       ' >  /  /
 (o( o( o )       \_."  <
  '-'-''-'            ) <
(       _.-'-.   ._\.  _|
 '----"/--.__.-) _-  \|
AoS    "V""    "V"

    ''')


def game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    first_move = input("You're at a cross road. Where do you wanna go? type [left/right]: ").lower()
    if first_move == "left":
        second_move = input(
            "You've come to a lake, There is an island. Type [wait] for the boat or [swim] to swim across: ").lower()
        if second_move == "wait":
            last_move = input(
                "You arrive at the island unharmed. There is a house with 3 doors, Type [red/yellow/blue]: ").lower()
            if last_move == "red":
                print("Burned by fire, Game Over!")
                fire()
            elif last_move == "blue":
                print("Slayed by beats, Game Over!")
                beast()
            elif last_move == "yellow":
                print("You Win!!")
                win()
            else:
                print("Game Over!")
                game_over()
        else:
            print("Attacked by trout, Game Over!")
            fish()
    else:
        print("Fall into a hole, Game Over!")
        game_over()

    tries = input("Do you wanna try again? [y/n]: ")
    while True:
        if tries == "y":
            print()
            print()
            game()
        else:
            break


game()
