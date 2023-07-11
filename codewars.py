string = 'Hello'
def rotate(string):
    rotated_strings = []
    for i in range(0,len(string)+1):
        rotated_string = string[i:] + string[:i]
        rotated_strings.append(rotated_string)
    print(rotated_strings)
    return rotated_strings
rotate(string)