import utilities
import v2_ClassExpressions
import v2_ClassProductions

word_to_axiom_validator = {
    "SubClassOf": v2_ClassExpressions.two_class_expressions,
    "EquivalentClasses": v2_ClassExpressions.many_class_expressions,
    "DisjointClasses": v2_ClassExpressions.many_class_expressions,
    "SameIndividual": v2_ClassProductions.many_classes_productions,
    "DifferentIndividuals": v2_ClassProductions.many_classes_productions
}


def detect_and_validate_axiom(file_reader):
    word = file_reader.pop_first()
    if utilities.DEBUG:
        print("detect_axiom")
        print("Validating %s" % word)
    try:
        return validate(file_reader, word_to_axiom_validator[word])
    except KeyError:
        expected = []
        for key in word_to_axiom_validator:
            expected.append(key)
        return utilities.report_error(file_reader.get_line_index(), expected, word)


def validate(file_reader, content_validation):
    if utilities.DEBUG:
        print("validate")
    return utilities.check_opening_colon(file_reader) and content_validation(file_reader) and utilities.check_closing_colon(file_reader)
