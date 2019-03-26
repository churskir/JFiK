import utilities


class FileReader:

    line_index = 0
    local_debug = True

    def __init__(self, file_path=None, lines=None, line_index=None):
        assert file_path is not None or (lines is not None and line_index is not None)
        if file_path is None:
            self.line_index = line_index
            self.lines = lines
            return
        f = open(file_path, "r")
        self.lines = []
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
                    chars += char
            self.lines.append(words)
            words = []
        f.close()
        if len(self.lines) == 0:
            print("File %s is empty" % file_path)
            exit(0)

    def copy(self):
        if utilities.DEBUG:
            print("Making copy of a file reader")
        return FileReader(lines=self.lines.copy(), line_index=self.line_index)

    def pop_first(self):
        if self.no_more_words():
            return None
        return self.__next()

    def get_line_index(self):
        return self.line_index

    def get(self, n):
        line_index = self.line_index
        try:
            while n >= len(self.lines[line_index]):
                n -= len(self.lines[line_index])
                line_index += 1
            return self.lines[line_index][n]
        except IndexError:
            return None

    def no_more_words(self):
        return self.__no_more_words_in_line() and self.__no_more_lines()

    def __no_more_words_in_line(self):
        if self.line_index < len(self.lines):
            return len(self.lines[self.line_index]) <= 0
        else:
            return False

    def __no_more_lines(self):
        return self.line_index >= (len(self.lines) - 1)

    def __next(self):
        if self.no_more_words():
            return None
        if self.__no_more_words_in_line():
            if self.local_debug:
                print("Increasing line_index, line_index=%s, lines=%s" % (self.line_index, self.lines))
            self.line_index += 1
        assert self.line_index < len(self.lines)
        assert len(self.lines[self.line_index]) > 0
        return self.lines[self.line_index].pop(0)

