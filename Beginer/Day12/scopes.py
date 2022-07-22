# Global scope
enemies = 1

def increase_enemies():
    # Local scope
    enemies = 2
    print(f'Enemies inside the function {enemies}')

increase_enemies()
print(f'Enemies outside the function {enemies}')