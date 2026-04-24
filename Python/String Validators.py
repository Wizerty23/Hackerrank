if __name__ == '__main__':
    s = input()

def alnum(string):
    return any(char.isalnum() for char in string)

print(alnum(s))

def has_alp(string):
    return any(char.isalpha() for char in string)

def has_num(string):
    return any(char.isdigit() for char in string)

def has_lower(string):
    return any(char.islower() for char in string)

def has_upper(string):
    return any(char.isupper() for char in string)

print(has_alp(s))
print(has_num(s))
print(has_lower(s))
print(has_upper(s))