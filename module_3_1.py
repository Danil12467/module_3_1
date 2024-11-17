calls = 0

def string_info(s):
    global calls
    calls += 1
    length = len(s)
    upper_case = s.upper()
    lower_case = s.lower()
    return (length, upper_case, lower_case)

def is_contains(target_string, string_list):
    target_string_lower = target_string.lower()
    return any(target_string_lower == s.lower() for s in string_list)

print(string_info('Capybara')) 
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban' 'BanAn', 'uRbAn']))
print(is_contains('cycle', ['recycling', 'cyclic']))

print("Total calls:", calls)











