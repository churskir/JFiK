from utilities import *
from v2_ClassExpressions import *
from v2_ObjectExpressions import *

word_to_axiom_validator = {
    "SubClassOf": two_class_expressions,
    "EquivalentClasses": many_class_expressions,
    "DisjointClasses": many_class_expressions,
    "SameIndividual": many_classes_productions,
    "DifferentIndividuals": many_classes_productions
}


def detect_and_validate_axiom(file_reader):
    word = file_reader.pop_first()
    if DEBUG:
        print("detect_axiom")
        print("Validating %s" % word)
    try:
        return validate(file_reader, word_to_axiom_validator[word])
    except KeyError:
        expected = []
        for key in word_to_axiom_validator:
            expected.append(key)
        return report_error(file_reader.get_line_index(), expected, word)


def validate(file_reader, content_validation):
    if DEBUG:
        print("validate")
    return check_opening_colon(file_reader) and content_validation(file_reader) and check_closing_colon(file_reader)
