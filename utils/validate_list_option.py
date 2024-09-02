options = ('done', 'todo', 'in-progress')

def validate_list_option(option):
    if option not in options:
        return False
    return True