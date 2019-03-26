import utilities
import v2_ClassProductions

# ObjectIntersectionOf ::= 'ObjectIntersectionOf(' ManyClassExpressions ')'
# ObjectUnionOf ::= 'ObjectUnionOf(' ManyClassExpressions ')'
# ObjectComplementOf ::= 'ObjectComplementOf(' ClassExpression ')'
# ObjectOneOf ::= 'ObjectOneOf(' ManyClasses ')'


# Returns False if failed
def class_expression(file_reader):
    word = file_reader.get(0)
    if utilities.DEBUG:
        print("class_expression")
        print("Interpreting '%s'" % word)
    if word == ':':
        return v2_ClassProductions.class_production(file_reader)
    return detect_and_validate_object_expression(file_reader)


# Returns False if failed
def two_class_expressions(file_reader):
    if utilities.DEBUG:
        print("two_class_expressions")
    return class_expression(file_reader) and class_expression(file_reader)


# Returns False if failed
def many_class_expressions(file_reader):
    if utilities.DEBUG:
        print("many_class_expressions")
    file_reader_copy = file_reader.copy()
    if two_class_expressions(file_reader):
        return True
    file_reader = file_reader_copy
    return class_expression(file_reader) and many_class_expressions(file_reader)


class_expr_for_object_expr = {
    "ObjectIntersectionOf": many_class_expressions,
    "ObjectUnionOf": many_class_expressions,
    "ObjectComplementOf": class_expression,
    "ObjectOneOf": v2_ClassProductions.many_classes_productions
}


def detect_and_validate_object_expression(file_reader):
    if utilities.DEBUG:
        print("detect_and_validate_object_expression")
    word = file_reader.pop_first()
    try:
        return validate_object_expression(
            file_reader,
            class_expr_for_object_expr[word]
        )
    except KeyError:
        keys = []
        for key in class_expr_for_object_expr:
            keys.append(key)
        return utilities.report_error(file_reader.get_line_index(), keys, word)


def validate_object_expression(file_reader, parameters_validator):
    if utilities.DEBUG:
        print("validate_object_expression")
    return \
        utilities.check_opening_colon(file_reader) and \
        parameters_validator(file_reader) and \
        utilities.check_closing_colon(file_reader)
