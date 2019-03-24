from utilities import *
from v2_ClassProductions import many_classes_productions

# ObjectIntersectionOf ::= 'ObjectIntersectionOf(' ManyClassExpressions ')'
# ObjectUnionOf ::= 'ObjectUnionOf(' ManyClassExpressions ')'
# ObjectComplementOf ::= 'ObjectComplementOf(' ClassExpression ')'
# ObjectOneOf ::= 'ObjectOneOf(' ManyClasses ')'

# class_expr_for_object_expr = {
#     "ObjectIntersectionOf": ManyClassExpressions,
#     "ObjectUnionOf": ManyClassExpressions,
#     "ObjectComplementOf": ClassExpression,
#     "ObjectOneOf": many_classes_productions
# }

class_expr_for_object_expr = {
    "ObjectIntersectionOf": many_classes_productions,
    "ObjectUnionOf": many_classes_productions,
    "ObjectComplementOf": many_classes_productions,
    "ObjectOneOf": many_classes_productions
}


def detect_and_validate_object_expression(file_reader):
    if DEBUG:
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
        return report_error(file_reader.get_line_index(), keys, word)


def validate_object_expression(file_reader, parameters_validator):
    if DEBUG:
        print("validate_object_expression")
    return \
        check_opening_colon(file_reader) and \
        parameters_validator(file_reader) and \
        check_closing_colon(file_reader)
