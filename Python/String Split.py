def split_and_join(line):
    x = ""
    for c in line:
        if c == " ":
            c = "-"
            x += c
        else:
            x += c
    return x

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)