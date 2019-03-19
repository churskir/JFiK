DEBUG = True

o_colon = "("
c_colon = ")"


def report_error(line, expected, found):
    line += 1
    if found is None:
        print("Error in line %d: Expected '%s', found nothing" % (line, expected))
    else:
        print("Error in line %d: Expected '%s', found '%s'" % (line, expected, found))
    exit(1)


def check_opening_colon(file_reader):
    word = file_reader.pop_first()
    if not word == "(":
        report_error(file_reader.get_line_index(), "(", word)


def check_closing_colon(file_reaer):
    word = file_reaer.pop_first()
    if not word == ")":
        report_error(file_reaer.get_line_index(), ")", word)
