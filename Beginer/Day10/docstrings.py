def format_name(f_name, l_name):
    """
    This function get a first and last name with unregular formating and capitalize it
    """
    return f'{f_name.capitalize()} {l_name.capitalize()}'


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(format_name(first_name, last_name))




