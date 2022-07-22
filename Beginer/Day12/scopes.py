# Global scope
enemies = 1


def increase_enemies():
    # Local scope
    # global enemies  # Used to modify the variable scope (avoid doing this)
    # enemies = 2
    print(f'Enemies inside the function {enemies}')
    return enemies + 1


enemies = increase_enemies()
print(f'Enemies outside the function {enemies}')

# Defining Global constants

PI = 3.14159
URL = 'https://www.google.com'
