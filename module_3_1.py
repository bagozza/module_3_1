calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return tuple([len(string), string.upper(), string.lower()])


def is_contains(string, list_to_search):
    count_calls()
    list_to_search_lower = []
    for string_to_search in list_to_search:
        list_to_search_lower.append(string_to_search.lower())

    if string.lower() in list_to_search_lower:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
