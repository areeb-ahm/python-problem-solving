# Write function is_valid_username(username). Rules:

# Length between 5 and 15 chars (inclusive).
# Only letters, digits, underscore allowed.
# Must start with a letter.

# Return True/False.

def is_valid_username(username):
    if len(username) < 5 or len(username) > 15:
        return False
    elif not(username[0].isalpha()):
            return False
    else:
         for each_char in username:
            if not(each_char.isalnum()):
                if each_char != "_":
                    return False
            
    return True
    
print(is_valid_username("harry_92"))
print(is_valid_username("ab"))
print(is_valid_username("harry!92"))
print(is_valid_username("9harry"))
print(is_valid_username("har_ry!92"))