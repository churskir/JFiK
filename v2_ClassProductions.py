from utilities import *


def class_production(file_reader):
    word = file_reader.pop_first()
    if DEBUG:
        print("class_production")
        print("Validating '%s'" % word)
    if not word == ':':
        return report_error(file_reader.get_line_index(), ":", word)
    word = file_reader.pop_first()
    if DEBUG:
        print("Expecting '%s' to be a alphanumerical phrase" % word)
    if not word[0].isalnum():
        return report_error(file_reader.get_line_index(), "word", word)
    return True


def two_classes_production(file_reader):
    if DEBUG:
        print("two_classes_production")
    return class_production(file_reader) and class_production(file_reader)


def many_classes_productions(file_reader):
    if DEBUG:
        print("many_classes_productions")
    if file_reader.get(4) == ':':
        return class_production(file_reader) and many_classes_productions(file_reader)
    else:
        return two_classes_production(file_reader)
