from utilities import *


def class_production(file_reader):
    if DEBUG:
        print("class_production")
    word = file_reader.pop_first()
    if not word == ':':
        return report_error(file_reader.get_line_index(), ":", word)
    word = file_reader.pop_first()
    if not word[0].isalnum():
        return report_error(file_reader.get_line_index(), "word", word)
    return True


def two_classes_production(file_reader):
    if DEBUG:
        print("two_classes_production")
    class_production(file_reader)
    class_production(file_reader)


def many_classes_productions(file_reader):
    if DEBUG:
        print("many_classes_productions")
    if file_reader.get(4) == ':':
        class_production(file_reader)
        many_classes_productions(file_reader)
    else:
        two_classes_production(file_reader)
