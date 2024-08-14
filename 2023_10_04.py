calls = 0
def count_calls():
    global calls
    calls+=1
def string_info(str):
    count_calls()
    result = (len(str),str.upper() , str.lower())
    return result
def is_contains(string , list_to_search):
    count_calls()
    low_list_to_search = [s.lower() for s in list_to_search]
    if string.lower() in low_list_to_search :
        result = True
    else:
        result = False
    return result
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)