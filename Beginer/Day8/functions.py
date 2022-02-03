# def greet(name):
#     print(f"Hello {name}")
#
#
# user = input("Whats your name? ")
# greet(user)
#

def greet_with(name, location):
    print(f'Hello {name} from {location} ')


n = input("whats your name: ")
locate = input("whats your location: ")

greet_with(location=locate, name=n)