import utilities
import v2_ClassProductions
import v2_ClassExpressions

# ObjectIntersectionOf ::= 'ObjectIntersectionOf(' ManyClassExpressions ')'
# ObjectUnionOf ::= 'ObjectUnionOf(' ManyClassExpressions ')'
# ObjectComplementOf ::= 'ObjectComplementOf(' ClassExpression ')'
# ObjectOneOf ::= 'ObjectOneOf(' ManyClasses ')'

class_expr_for_object_expr = {
    "ObjectIntersectionOf": v2_ClassExpressions.many_class_expressions,
    "ObjectUnionOf": v2_ClassExpressions.many_class_expressions,
    "ObjectComplementOf": v2_ClassExpressions.class_expression,
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
