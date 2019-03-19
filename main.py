from validator import validate

def read_file(filename):
    f = open(filename, "r")
    lines = []
    words = []
    chars = ""
    for line in f.readlines():
        for char in line:
            if char.isspace() or not char.isalnum():
                if chars:
                    words.append(chars)
                    chars = ""
                if not char.isspace():
                    words.append(char)
            else:
                chars += char;
        lines.append(words)
        words = []
    f.close()
    return lines

# print(read_file("test1.txt"))
validate(read_file("test1.txt"))
