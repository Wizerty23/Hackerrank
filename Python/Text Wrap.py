import textwrap

def wrap(string, max_width):
    listed = textwrap.wrap(string, width=max_width)  #Returns it like a list
    return "\n".join(listed)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)