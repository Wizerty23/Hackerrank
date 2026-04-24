#It can be done with a python builtin function
#s = input("Write anything: ")
#print(s.swapcase())

#Done it with a function
def swap_case(s):
    x = ""
    for char in s: #You can iterate over a string
        if char.isupper() == True:
            x += char.lower()
        else:
            x += char.upper()
    return x

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)